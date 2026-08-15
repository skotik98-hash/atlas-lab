#!/usr/bin/env python3
"""Isolated R4 work-ownership durability tests. Uses temporary databases only."""

import gc
import json
import os
import sqlite3
import subprocess
import sys
import tempfile
import threading
import traceback
from datetime import datetime, timedelta, timezone
from pathlib import Path

import run_store
from run_store import (
    MAX_ATTEMPTS,
    acquire_lease,
    complete_attempt,
    enqueue_run,
    fail_attempt,
    get_attempt,
    get_run,
    heartbeat,
    list_attempts,
    reclaim_expired_leases,
)


LIVE_DATA = Path(__file__).resolve().parent / "data"
BOT_DIR = Path(__file__).resolve().parent
T0 = datetime(2026, 8, 15, 12, 0, 0, tzinfo=timezone.utc)
ITERATIONS = 80

REQUIRED_RUN_COLUMNS = {
    "id",
    "run_id",
    "work_type",
    "payload_json",
    "status",
    "attempt_count",
    "current_attempt_id",
    "created_at",
    "updated_at",
}

REQUIRED_ATTEMPT_COLUMNS = {
    "attempt_id",
    "run_id",
    "attempt_n",
    "status",
    "worker_id",
    "lease_until",
    "heartbeat_at",
    "started_at",
    "finished_at",
    "error",
}

REQUIRED_INDEXES = {
    "idx_runs_status_created",
    "idx_attempts_run_id",
    "idx_attempts_lease",
}

INIT_WORKER = r"""
import sys
from pathlib import Path

sys.path.insert(0, sys.argv[1])

import run_store

run_store.DB_PATH = Path(sys.argv[2])
run_store.fail_after_attempt_insert = False
run_store.initialize()
"""

ACQUIRE_WORKER = r"""
import json
import sys
from pathlib import Path

sys.path.insert(0, sys.argv[1])

import run_store

run_store.DB_PATH = Path(sys.argv[2])
run_store.fail_after_attempt_insert = False
worker_id = sys.argv[3]
ttl = int(sys.argv[4])

try:
    result = run_store.acquire_lease(worker_id, lease_ttl_seconds=ttl)
    attempt = result.get("attempt") or {}
    run = result.get("run") or {}
    print(
        json.dumps(
            {
                "ok": result["ok"],
                "reason": result["reason"],
                "attempt_id": attempt.get("attempt_id"),
                "attempt_n": attempt.get("attempt_n"),
                "run_id": run.get("run_id"),
                "worker_id": attempt.get("worker_id"),
            }
        )
    )
except Exception as exc:
    print(
        json.dumps(
            {
                "ok": False,
                "reason": "ERROR",
                "error": f"{type(exc).__name__}: {exc}",
            }
        )
    )
    raise SystemExit(1)
"""

RECLAIM_WORKER = r"""
import json
import sys
from pathlib import Path

sys.path.insert(0, sys.argv[1])

import run_store

run_store.DB_PATH = Path(sys.argv[2])
run_store.fail_after_attempt_insert = False
now = sys.argv[3]

try:
    items = run_store.reclaim_expired_leases(now=now)
    print(
        json.dumps(
            {
                "ok": True,
                "reason": "OK",
                "count": len(items),
                "items": items,
            }
        )
    )
except Exception as exc:
    print(
        json.dumps(
            {
                "ok": False,
                "reason": "ERROR",
                "error": f"{type(exc).__name__}: {exc}",
            }
        )
    )
    raise SystemExit(1)
"""


def ts(seconds=0):
    return (T0 + timedelta(seconds=seconds)).isoformat()


def count_fds_for(path):
    path = Path(path).resolve()
    if not path.exists():
        return 0

    count = 0
    try:
        names = os.listdir("/dev/fd")
    except OSError:
        return -1

    for name in names:
        fd_path = Path("/dev/fd") / name
        try:
            if os.path.samefile(fd_path, path):
                count += 1
        except OSError:
            continue

    return count


def count_open_fds():
    return len(os.listdir("/dev/fd"))


def assert_not_live(path):
    resolved = Path(path).resolve()
    live = LIVE_DATA.resolve()
    if resolved == live or live in resolved.parents:
        raise AssertionError(f"Refusing to use live database path: {resolved}")


def reset_hooks():
    run_store.fail_after_attempt_insert = False


def isolate(tmp_dir, name):
    folder = Path(tmp_dir) / name
    folder.mkdir(parents=True, exist_ok=True)
    db_path = folder / "runs.db"
    assert_not_live(db_path)
    run_store.DB_PATH = db_path
    reset_hooks()
    return db_path


class Results:
    def __init__(self):
        self.failed = []
        self.passed = []

    def check(self, name, ok, detail=""):
        if ok:
            self.passed.append(name)
            print(f"PASS  {name}" + (f"  {detail}" if detail else ""))
        else:
            self.failed.append(name)
            print(f"FAIL  {name}" + (f"  {detail}" if detail else ""))


def _read_schema(db_path):
    assert_not_live(db_path)
    raw = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    try:
        run_cols = {
            row[1] for row in raw.execute("PRAGMA table_info(runs)")
        }
        attempt_cols = {
            row[1] for row in raw.execute("PRAGMA table_info(attempts)")
        }
        indexes = {
            row[0]
            for row in raw.execute(
                """
                SELECT name
                FROM sqlite_master
                WHERE type = 'index'
                  AND name IS NOT NULL
                """
            )
        }
        integrity = raw.execute("PRAGMA integrity_check").fetchone()
        integrity_ok = (
            integrity is not None and str(integrity[0]).lower() == "ok"
        )
        return run_cols, attempt_cols, indexes, integrity_ok
    finally:
        raw.close()


def _count_lock_failures(failures):
    locked = 0
    for item in failures:
        blob = (item.get("stderr") or "") + (item.get("stdout") or "")
        if "database is locked" in blob or "OperationalError" in blob:
            locked += 1
    return locked


def _run_python_workers(code, extra_args, workers):
    processes = [
        subprocess.Popen(
            [sys.executable, "-c", code, str(BOT_DIR), *extra_args],
            cwd=str(BOT_DIR),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        for _ in range(workers)
    ]
    results = []
    failures = []
    for process in processes:
        stdout, stderr = process.communicate(timeout=60)
        if process.returncode != 0:
            failures.append(
                {
                    "code": process.returncode,
                    "stdout": stdout,
                    "stderr": stderr,
                }
            )
        else:
            results.append(stdout)
    return results, failures


def test_fresh_schema(results, tmp_dir):
    db_path = isolate(tmp_dir, "schema")
    run_store.initialize()
    run_cols, attempt_cols, indexes, integrity_ok = _read_schema(db_path)
    results.check(
        "fresh schema initialization",
        REQUIRED_RUN_COLUMNS <= run_cols
        and REQUIRED_ATTEMPT_COLUMNS <= attempt_cols
        and REQUIRED_INDEXES <= indexes
        and integrity_ok,
        f"run_cols={sorted(run_cols)} attempt_cols={sorted(attempt_cols)}",
    )


def test_concurrent_initialize(results, tmp_dir):
    configs = ((2, 5), (8, 5), (16, 5))
    total_failed_rounds = 0
    total_locked = 0
    total_nonzero = 0

    for workers, rounds in configs:
        failed_rounds = 0
        locked = 0
        nonzero = 0

        for round_id in range(rounds):
            db_path = isolate(tmp_dir, f"init-race-{workers}-{round_id}")
            if db_path.exists():
                raise AssertionError(f"pre-warmed DB is not allowed: {db_path}")
            outputs, failures = _run_python_workers(
                INIT_WORKER,
                [str(db_path)],
                workers,
            )
            nonzero += len(failures)
            locked += _count_lock_failures(failures)
            if failures:
                failed_rounds += 1
                results.check(
                    f"cold initialize {workers}p round {round_id}",
                    False,
                    failures[0]["stderr"][:400]
                    or failures[0]["stdout"][:400],
                )
                continue

            run_cols, attempt_cols, indexes, integrity_ok = _read_schema(
                db_path
            )
            results.check(
                f"cold initialize {workers}p round {round_id}",
                len(outputs) == workers
                and len(failures) == 0
                and REQUIRED_RUN_COLUMNS <= run_cols
                and REQUIRED_ATTEMPT_COLUMNS <= attempt_cols
                and REQUIRED_INDEXES <= indexes
                and integrity_ok,
                f"workers={len(outputs)} integrity_ok={integrity_ok}",
            )

        results.check(
            f"cold initialize {workers} processes had zero failures",
            failed_rounds == 0 and locked == 0 and nonzero == 0,
            f"failed_rounds={failed_rounds} locked={locked} nonzero={nonzero}",
        )
        total_failed_rounds += failed_rounds
        total_locked += locked
        total_nonzero += nonzero

    results.check(
        "concurrent cold initialize 2/8/16 had zero lock failures",
        total_failed_rounds == 0
        and total_locked == 0
        and total_nonzero == 0,
        f"failed_rounds={total_failed_rounds} locked={total_locked} nonzero={total_nonzero}",
    )


def _expect_value_error(fn):
    try:
        fn()
    except ValueError:
        return True
    return False


def test_canonical_offset_equivalence(results, tmp_dir):
    plus02 = "2026-08-15T14:00:00+02:00"
    minus05 = "2026-08-15T07:00:00-05:00"
    utc = "2026-08-15T12:00:00+00:00"
    zulu = "2026-08-15T12:00:00Z"
    expected = "2026-08-15T12:00:00+00:00"

    normalized = [
        run_store._as_iso(plus02),
        run_store._as_iso(minus05),
        run_store._as_iso(utc),
        run_store._as_iso(zulu),
        run_store._as_iso(datetime(2026, 8, 15, 14, 0, 0, tzinfo=timezone(timedelta(hours=2)))),
        run_store._as_iso(datetime(2026, 8, 15, 7, 0, 0, tzinfo=timezone(timedelta(hours=-5)))),
        run_store._as_iso(datetime(2026, 8, 15, 12, 0, 0, tzinfo=timezone.utc)),
    ]
    results.check(
        "equivalent +02:00/-05:00/+00:00/Z instants serialize identically",
        all(item == expected for item in normalized),
        f"normalized={normalized}",
    )

    samples = [
        plus02,
        minus05,
        utc,
        zulu,
        "2026-08-15T12:00:30+00:00",
        "2026-08-15T11:59:59+00:00",
        "2026-08-15T15:00:30-05:00",
        "2026-08-15T14:00:30+02:00",
    ]
    canon = [run_store._as_iso(item) for item in samples]
    parsed = [run_store._as_dt(item) for item in canon]
    lexical_matches = True
    for left_i, left in enumerate(canon):
        for right_i, right in enumerate(canon):
            if (left <= right) != (parsed[left_i] <= parsed[right_i]):
                lexical_matches = False
    results.check(
        "canonical UTC lexical order matches chronological order",
        lexical_matches and all(item.endswith("+00:00") for item in canon),
        f"canon={canon}",
    )

    isolate(tmp_dir, "offset-store")
    stored = []
    for index, stamp in enumerate((plus02, minus05, utc)):
        created = enqueue_run()
        acquired = acquire_lease(
            f"offset-{index}",
            lease_ttl_seconds=30,
            now=stamp,
        )
        attempt = acquired["attempt"]
        stored.append(
            (
                attempt["started_at"],
                attempt["heartbeat_at"],
                attempt["lease_until"],
            )
        )
        results.check(
            f"acquire with offset {stamp} stores canonical UTC",
            acquired["ok"]
            and attempt["started_at"] == expected
            and attempt["heartbeat_at"] == expected
            and attempt["lease_until"] == "2026-08-15T12:00:30+00:00"
            and get_run(created["run_id"])["updated_at"] == expected,
            f"started={attempt['started_at']} until={attempt['lease_until']}",
        )
    results.check(
        "offset acquires persist identical canonical timestamps",
        len(set(stored)) == 1,
        f"stored={stored}",
    )


def test_premature_reclaim_offset(results, tmp_dir):
    isolate(tmp_dir, "premature-reclaim")
    created = enqueue_run()
    acquired = acquire_lease(
        "worker-a",
        lease_ttl_seconds=30,
        now="2026-08-15T10:00:00-05:00",
    )
    attempt_id = acquired["attempt"]["attempt_id"]
    reclaim_now = "2026-08-15T12:00:00+00:00"
    reclaimed = reclaim_expired_leases(now=reclaim_now)
    run = get_run(created["run_id"])
    attempt = get_attempt(attempt_id)
    stolen = acquire_lease(
        "worker-b",
        lease_ttl_seconds=30,
        now=reclaim_now,
    )

    results.check(
        "premature reclaim with mixed offsets is impossible",
        acquired["ok"]
        and acquired["attempt"]["lease_until"] == "2026-08-15T15:00:30+00:00"
        and reclaimed == []
        and run["status"] == "LEASED"
        and run["current_attempt_id"] == attempt_id
        and attempt["status"] == "LEASED"
        and attempt["worker_id"] == "worker-a"
        and not stolen["ok"]
        and stolen["reason"] == "NO_ELIGIBLE_RUN",
        f"reclaimed={reclaimed} status={run['status']} steal={stolen.get('reason')}",
    )


def test_late_reclaim_offset(results, tmp_dir):
    isolate(tmp_dir, "late-reclaim")
    created = enqueue_run()
    acquired = acquire_lease(
        "worker-a",
        lease_ttl_seconds=30,
        now="2026-08-15T14:00:00+02:00",
    )
    attempt_id = acquired["attempt"]["attempt_id"]
    reclaim_now = "2026-08-15T12:01:00+00:00"
    reclaimed = reclaim_expired_leases(now=reclaim_now)
    run = get_run(created["run_id"])
    attempt = get_attempt(attempt_id)
    next_owner = acquire_lease(
        "worker-b",
        lease_ttl_seconds=30,
        now=reclaim_now,
    )

    results.check(
        "late reclaim with mixed offsets is impossible",
        acquired["ok"]
        and acquired["attempt"]["lease_until"] == "2026-08-15T12:00:30+00:00"
        and len(reclaimed) == 1
        and reclaimed[0]["attempt_id"] == attempt_id
        and reclaimed[0]["run_status"] == "PENDING"
        and run["status"] == "PENDING"
        and run["current_attempt_id"] is None
        and attempt["status"] == "EXPIRED"
        and next_owner["ok"]
        and next_owner["attempt"]["worker_id"] == "worker-b"
        and next_owner["attempt"]["attempt_n"] == 2,
        f"reclaimed={reclaimed} status={run['status']}",
    )


def test_utc_expiry_boundary(results, tmp_dir):
    isolate(tmp_dir, "expiry-boundary")
    created = enqueue_run()
    acquired = acquire_lease("owner", lease_ttl_seconds=30, now=ts(0))
    attempt_id = acquired["attempt"]["attempt_id"]

    before = reclaim_expired_leases(now=ts(29))
    hb_before = heartbeat(attempt_id, "owner", lease_ttl_seconds=1, now=ts(29))
    after_hb = get_attempt(attempt_id)
    hb_equal = heartbeat(attempt_id, "owner", lease_ttl_seconds=30, now=ts(30))
    equal = reclaim_expired_leases(now=ts(30))
    run = get_run(created["run_id"])
    attempt = get_attempt(attempt_id)

    isolate(tmp_dir, "expiry-boundary-after")
    created_after = enqueue_run()
    later = acquire_lease("owner-2", lease_ttl_seconds=30, now=ts(0))
    after = reclaim_expired_leases(now=ts(31))
    later_run = get_run(created_after["run_id"])
    later_attempt = get_attempt(later["attempt"]["attempt_id"])

    results.check(
        "lease_until > now remains valid",
        before == []
        and hb_before["ok"]
        and after_hb["status"] == "LEASED"
        and after_hb["lease_until"] == ts(30),
        f"before={before} hb={hb_before.get('reason')}",
    )
    results.check(
        "lease_until == now is expired",
        not hb_equal["ok"]
        and hb_equal["reason"] == "LEASE_EXPIRED"
        and len(equal) == 1
        and equal[0]["attempt_id"] == attempt_id
        and run["status"] == "PENDING"
        and run["current_attempt_id"] is None
        and attempt["status"] == "EXPIRED",
        f"hb_equal={hb_equal.get('reason')} equal={equal}",
    )
    results.check(
        "lease_until < now is expired",
        len(after) == 1
        and after[0]["run_id"] == created_after["run_id"]
        and after[0]["attempt_id"] == later["attempt"]["attempt_id"]
        and later_run["status"] == "PENDING"
        and later_run["current_attempt_id"] is None
        and later_attempt["status"] == "EXPIRED",
        f"after={after} status={later_run['status']}",
    )


def test_naive_timestamps_rejected(results, tmp_dir):
    isolate(tmp_dir, "naive-reject")
    created = enqueue_run()
    snapshot = get_run(created["run_id"])
    naive_string = "2026-08-15T12:00:00"
    naive_dt = datetime(2026, 8, 15, 12, 0, 0)
    malformed = "not-a-timestamp"

    acquire_string = _expect_value_error(
        lambda: acquire_lease("owner", lease_ttl_seconds=30, now=naive_string)
    )
    after_string = get_run(created["run_id"])
    attempts_string = list_attempts(created["run_id"])
    acquire_dt = _expect_value_error(
        lambda: acquire_lease("owner", lease_ttl_seconds=30, now=naive_dt)
    )
    after_dt = get_run(created["run_id"])
    attempts_dt = list_attempts(created["run_id"])
    acquire_bad = _expect_value_error(
        lambda: acquire_lease("owner", lease_ttl_seconds=30, now=malformed)
    )
    after_bad = get_run(created["run_id"])

    results.check(
        "naive ISO string is rejected before acquire mutation",
        acquire_string
        and after_string["status"] == snapshot["status"] == "PENDING"
        and after_string["attempt_count"] == snapshot["attempt_count"] == 0
        and after_string["current_attempt_id"] is None
        and attempts_string == [],
        f"status={after_string['status']} attempts={len(attempts_string)}",
    )
    results.check(
        "naive datetime is rejected before acquire mutation",
        acquire_dt
        and after_dt["status"] == "PENDING"
        and after_dt["attempt_count"] == 0
        and after_dt["current_attempt_id"] is None
        and attempts_dt == [],
        f"status={after_dt['status']} attempts={len(attempts_dt)}",
    )
    results.check(
        "malformed timestamp is rejected before acquire mutation",
        acquire_bad
        and after_bad["status"] == "PENDING"
        and after_bad["attempt_count"] == 0
        and list_attempts(created["run_id"]) == [],
        f"status={after_bad['status']}",
    )

    acquired = acquire_lease("owner", lease_ttl_seconds=30, now=ts(0))
    attempt_id = acquired["attempt"]["attempt_id"]
    leased = get_run(created["run_id"])
    leased_attempt = get_attempt(attempt_id)

    hb_naive = _expect_value_error(
        lambda: heartbeat(
            attempt_id, "owner", lease_ttl_seconds=30, now=naive_string
        )
    )
    complete_naive = _expect_value_error(
        lambda: complete_attempt(attempt_id, "owner", now=naive_dt)
    )
    fail_naive = _expect_value_error(
        lambda: fail_attempt(attempt_id, "owner", error="x", now=naive_string)
    )
    reclaim_naive = _expect_value_error(
        lambda: reclaim_expired_leases(now=naive_dt)
    )
    still = get_run(created["run_id"])
    still_attempt = get_attempt(attempt_id)

    results.check(
        "naive now is rejected uniformly without mutating ownership",
        acquired["ok"]
        and hb_naive
        and complete_naive
        and fail_naive
        and reclaim_naive
        and still["status"] == leased["status"] == "LEASED"
        and still["attempt_count"] == leased["attempt_count"] == 1
        and still["current_attempt_id"] == attempt_id
        and still_attempt["status"] == leased_attempt["status"] == "LEASED"
        and still_attempt["lease_until"] == leased_attempt["lease_until"]
        and still_attempt["heartbeat_at"] == leased_attempt["heartbeat_at"]
        and still_attempt["finished_at"] is None,
        f"status={still['status']} hb={hb_naive} complete={complete_naive}",
    )


def test_happy_path(results, tmp_dir):
    isolate(tmp_dir, "happy")
    created = enqueue_run(payload={"probe": True})
    acquired = acquire_lease("worker-a", lease_ttl_seconds=30, now=ts(0))
    attempt = acquired.get("attempt") or {}
    completed = complete_attempt(
        attempt.get("attempt_id"),
        "worker-a",
        now=ts(5),
    )
    run = get_run(created["run_id"])
    stored = get_attempt(attempt.get("attempt_id"))

    results.check(
        "enqueue -> acquire -> complete happy path",
        created["status"] == "PENDING"
        and created["attempt_count"] == 0
        and acquired["ok"]
        and attempt["attempt_n"] == 1
        and attempt["worker_id"] == "worker-a"
        and completed["ok"]
        and completed["reason"] == "OK"
        and run["status"] == "SUCCEEDED"
        and run["attempt_count"] == 1
        and run["current_attempt_id"] == attempt["attempt_id"]
        and stored["status"] == "SUCCEEDED"
        and stored["finished_at"] == ts(5)
        and created["payload"] == {"probe": True},
        f"run={run['status']} reason={completed.get('reason')}",
    )


def test_thread_acquire_one_winner(results, tmp_dir):
    isolate(tmp_dir, "thread-acquire")
    created = enqueue_run()
    outcomes = []

    def attempt():
        outcomes.append(acquire_lease("thread-worker", lease_ttl_seconds=30))

    threads = [threading.Thread(target=attempt) for _ in range(8)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    wins = [item for item in outcomes if item["ok"]]
    losses = [item for item in outcomes if not item["ok"]]
    run = get_run(created["run_id"])
    attempts = list_attempts(created["run_id"])

    results.check(
        "exactly one winner for competing thread acquire_lease",
        len(outcomes) == 8
        and len(wins) == 1
        and len(losses) == 7
        and all(item["reason"] == "NO_ELIGIBLE_RUN" for item in losses)
        and run["status"] == "LEASED"
        and run["attempt_count"] == 1
        and len(attempts) == 1,
        f"wins={len(wins)} losses={len(losses)}",
    )


def test_multiprocess_acquire_stress(results, tmp_dir):
    rounds = 8
    workers = 8
    failed_rounds = 0
    locked = 0

    for round_id in range(rounds):
        db_path = isolate(tmp_dir, f"acquire-race-{round_id}")
        created = enqueue_run()
        extra = [str(db_path), f"proc-{round_id}", "30"]
        processes = []
        for worker_n in range(workers):
            processes.append(
                subprocess.Popen(
                    [
                        sys.executable,
                        "-c",
                        ACQUIRE_WORKER,
                        str(BOT_DIR),
                        str(db_path),
                        f"proc-{round_id}-{worker_n}",
                        "30",
                    ],
                    cwd=str(BOT_DIR),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                )
            )

        parsed = []
        round_failures = []
        for process in processes:
            stdout, stderr = process.communicate(timeout=60)
            if process.returncode != 0:
                round_failures.append(
                    {
                        "code": process.returncode,
                        "stdout": stdout,
                        "stderr": stderr,
                    }
                )
                if (
                    "database is locked" in stderr
                    or "OperationalError" in stderr
                    or "database is locked" in stdout
                    or "OperationalError" in stdout
                ):
                    locked += 1
            else:
                parsed.append(json.loads(stdout))

        if round_failures:
            failed_rounds += 1
            results.check(
                f"multiprocess acquire round {round_id}",
                False,
                round_failures[0]["stderr"][:400]
                or round_failures[0]["stdout"][:400],
            )
            continue

        wins = [item for item in parsed if item["ok"]]
        losses = [item for item in parsed if not item["ok"]]
        run = get_run(created["run_id"])
        attempts = list_attempts(created["run_id"])
        results.check(
            f"multiprocess acquire round {round_id}",
            len(parsed) == workers
            and len(wins) == 1
            and len(losses) == workers - 1
            and all(item["reason"] == "NO_ELIGIBLE_RUN" for item in losses)
            and run["status"] == "LEASED"
            and run["attempt_count"] == 1
            and len(attempts) == 1
            and attempts[0]["attempt_n"] == 1
            and wins[0]["attempt_id"] == attempts[0]["attempt_id"],
            f"wins={len(wins)} losses={len(losses)} extra={extra[0]}",
        )
        if not (
            len(wins) == 1
            and len(losses) == workers - 1
            and run["status"] == "LEASED"
        ):
            failed_rounds += 1

    results.check(
        "multiprocess acquire stress had one winner every round",
        failed_rounds == 0 and locked == 0,
        f"failed_rounds={failed_rounds} locked={locked}",
    )


def test_duplicate_complete_and_wrong_worker(results, tmp_dir):
    isolate(tmp_dir, "complete-rules")
    created = enqueue_run()
    acquired = acquire_lease("owner", lease_ttl_seconds=30, now=ts(0))
    attempt_id = acquired["attempt"]["attempt_id"]

    first = complete_attempt(attempt_id, "owner", now=ts(1))
    duplicate = complete_attempt(attempt_id, "owner", now=ts(2))
    wrong_complete = complete_attempt(attempt_id, "intruder", now=ts(3))
    wrong_fail = fail_attempt(attempt_id, "intruder", error="nope", now=ts(3))
    wrong_heartbeat = heartbeat(
        attempt_id,
        "intruder",
        lease_ttl_seconds=30,
        now=ts(3),
    )

    leased = enqueue_run()
    other = acquire_lease("owner-2", lease_ttl_seconds=30, now=ts(10))
    other_id = other["attempt"]["attempt_id"]
    hb_wrong = heartbeat(
        other_id,
        "intruder",
        lease_ttl_seconds=60,
        now=ts(11),
    )
    complete_wrong = complete_attempt(other_id, "intruder", now=ts(11))
    fail_wrong = fail_attempt(
        other_id,
        "intruder",
        error="steal",
        now=ts(11),
    )
    still = get_run(leased["run_id"])
    still_attempt = get_attempt(other_id)

    results.check(
        "duplicate completion is idempotent",
        first["ok"]
        and first["reason"] == "OK"
        and duplicate["ok"]
        and duplicate["reason"] == "ALREADY_SUCCEEDED"
        and get_run(created["run_id"])["status"] == "SUCCEEDED",
        f"dup={duplicate.get('reason')}",
    )
    results.check(
        "wrong worker_id cannot complete succeeded current attempt",
        not wrong_complete["ok"]
        and wrong_complete["reason"] == "WRONG_WORKER",
        wrong_complete.get("reason"),
    )
    results.check(
        "wrong worker_id cannot fail succeeded current attempt",
        not wrong_fail["ok"]
        and wrong_fail["reason"] in {"WRONG_WORKER", "NOT_LEASED"},
        wrong_fail.get("reason"),
    )
    results.check(
        "wrong worker_id cannot heartbeat succeeded attempt",
        not wrong_heartbeat["ok"],
        wrong_heartbeat.get("reason"),
    )
    results.check(
        "wrong worker_id cannot heartbeat",
        not hb_wrong["ok"] and hb_wrong["reason"] == "WRONG_WORKER",
        hb_wrong.get("reason"),
    )
    results.check(
        "wrong worker_id cannot complete",
        not complete_wrong["ok"]
        and complete_wrong["reason"] == "WRONG_WORKER"
        and still["status"] == "LEASED"
        and still_attempt["status"] == "LEASED",
        complete_wrong.get("reason"),
    )
    results.check(
        "wrong worker_id cannot fail",
        not fail_wrong["ok"]
        and fail_wrong["reason"] == "WRONG_WORKER"
        and get_run(leased["run_id"])["status"] == "LEASED",
        fail_wrong.get("reason"),
    )


def test_heartbeat_extend_and_no_shorten(results, tmp_dir):
    isolate(tmp_dir, "heartbeat")
    enqueue_run()
    acquired = acquire_lease("owner", lease_ttl_seconds=3600, now=ts(0))
    attempt_id = acquired["attempt"]["attempt_id"]
    original = acquired["attempt"]["lease_until"]

    shortened = heartbeat(
        attempt_id,
        "owner",
        lease_ttl_seconds=1,
        now=ts(10),
    )
    after_short = get_attempt(attempt_id)
    extended = heartbeat(
        attempt_id,
        "owner",
        lease_ttl_seconds=4000,
        now=ts(10),
    )
    after_extend = get_attempt(attempt_id)

    results.check(
        "heartbeat cannot shorten lease",
        shortened["ok"]
        and shortened.get("extended") is False
        and after_short["lease_until"] == original
        and after_short["heartbeat_at"] == ts(10),
        f"original={original} kept={after_short['lease_until']}",
    )
    results.check(
        "heartbeat extends lease",
        extended["ok"]
        and extended.get("extended") is True
        and after_extend["lease_until"] == ts(10 + 4000)
        and after_extend["lease_until"] != original,
        f"until={after_extend['lease_until']}",
    )


def test_heartbeat_after_expiry(results, tmp_dir):
    isolate(tmp_dir, "hb-expiry")
    enqueue_run()
    acquired = acquire_lease("owner", lease_ttl_seconds=30, now=ts(0))
    attempt_id = acquired["attempt"]["attempt_id"]
    original = acquired["attempt"]["lease_until"]

    expired = heartbeat(
        attempt_id,
        "owner",
        lease_ttl_seconds=30,
        now=ts(31),
    )
    after = get_attempt(attempt_id)
    run = get_run(acquired["run"]["run_id"])

    results.check(
        "heartbeat after expiry fails",
        not expired["ok"]
        and expired["reason"] == "LEASE_EXPIRED"
        and after["status"] == "LEASED"
        and after["lease_until"] == original
        and run["status"] == "LEASED",
        expired.get("reason"),
    )


def test_crash_reclaim_and_stale_worker(results, tmp_dir):
    isolate(tmp_dir, "crash")
    created = enqueue_run()
    first = acquire_lease("worker-a", lease_ttl_seconds=30, now=ts(0))
    attempt_id = first["attempt"]["attempt_id"]

    reclaimed = reclaim_expired_leases(now=ts(31))
    run_after = get_run(created["run_id"])
    old = get_attempt(attempt_id)

    stale_complete = complete_attempt(attempt_id, "worker-a", now=ts(32))
    stale_fail = fail_attempt(
        attempt_id,
        "worker-a",
        error="late",
        now=ts(32),
    )
    stale_hb = heartbeat(
        attempt_id,
        "worker-a",
        lease_ttl_seconds=30,
        now=ts(32),
    )

    second = acquire_lease("worker-b", lease_ttl_seconds=30, now=ts(40))
    attempts = list_attempts(created["run_id"])

    results.check(
        "crash simulation reclaim then next attempt_n + 1",
        len(reclaimed) == 1
        and reclaimed[0]["run_status"] == "PENDING"
        and run_after["status"] == "PENDING"
        and run_after["current_attempt_id"] is None
        and old["status"] == "EXPIRED"
        and second["ok"]
        and second["attempt"]["attempt_n"] == 2
        and second["attempt"]["worker_id"] == "worker-b"
        and len(attempts) == 2,
        f"reclaimed={reclaimed} n={second.get('attempt', {}).get('attempt_n')}",
    )
    results.check(
        "stale worker cannot complete after reclaim",
        not stale_complete["ok"]
        and stale_complete["reason"] == "NOT_CURRENT",
        stale_complete.get("reason"),
    )
    results.check(
        "stale worker cannot fail after reclaim",
        not stale_fail["ok"]
        and stale_fail["reason"] == "NOT_CURRENT",
        stale_fail.get("reason"),
    )
    results.check(
        "stale worker cannot heartbeat after reclaim",
        not stale_hb["ok"]
        and stale_hb["reason"] == "NOT_CURRENT",
        stale_hb.get("reason"),
    )

    late_complete = complete_attempt(attempt_id, "worker-a", now=ts(41))
    results.check(
        "stale attempt complete is not silent success after new owner",
        not late_complete["ok"]
        and late_complete["reason"] == "NOT_CURRENT"
        and get_run(created["run_id"])["status"] == "LEASED",
        late_complete.get("reason"),
    )


def test_concurrent_reclaim(results, tmp_dir):
    rounds = 5
    workers = 8
    failed_rounds = 0
    locked = 0

    for round_id in range(rounds):
        db_path = isolate(tmp_dir, f"reclaim-race-{round_id}")
        created = enqueue_run()
        acquired = acquire_lease(
            "owner",
            lease_ttl_seconds=30,
            now=ts(0),
        )
        outputs, failures = _run_python_workers(
            RECLAIM_WORKER,
            [str(db_path), ts(31)],
            workers,
        )
        if failures:
            failed_rounds += 1
            locked += sum(
                1
                for item in failures
                if "database is locked" in (item.get("stderr") or "")
                or "OperationalError" in (item.get("stderr") or "")
            )
            results.check(
                f"multiprocess reclaim round {round_id}",
                False,
                failures[0]["stderr"][:400],
            )
            continue

        parsed = [json.loads(item) for item in outputs]
        winners = [item for item in parsed if item.get("count") == 1]
        losers = [item for item in parsed if item.get("count") == 0]
        run = get_run(created["run_id"])
        attempts = list_attempts(created["run_id"])
        results.check(
            f"multiprocess reclaim round {round_id}",
            len(parsed) == workers
            and len(winners) == 1
            and len(losers) == workers - 1
            and run["status"] == "PENDING"
            and run["current_attempt_id"] is None
            and len(attempts) == 1
            and attempts[0]["status"] == "EXPIRED"
            and attempts[0]["attempt_id"] == acquired["attempt"]["attempt_id"],
            f"winners={len(winners)} losers={len(losers)}",
        )
        if len(winners) != 1:
            failed_rounds += 1

    results.check(
        "concurrent reclaim has one authoritative winner",
        failed_rounds == 0 and locked == 0,
        f"failed_rounds={failed_rounds} locked={locked}",
    )


def test_explicit_fail_terminal(results, tmp_dir):
    isolate(tmp_dir, "fail-terminal")
    created = enqueue_run()
    acquired = acquire_lease("owner", lease_ttl_seconds=30, now=ts(0))
    attempt_id = acquired["attempt"]["attempt_id"]
    failed = fail_attempt(
        attempt_id,
        "owner",
        error="boom",
        now=ts(1),
    )
    again = acquire_lease("other", lease_ttl_seconds=30, now=ts(2))
    reclaimed = reclaim_expired_leases(now=ts(100))
    run = get_run(created["run_id"])
    attempt = get_attempt(attempt_id)

    results.check(
        "explicit fail is terminal",
        failed["ok"]
        and run["status"] == "FAILED"
        and attempt["status"] == "FAILED"
        and attempt["error"] == "boom"
        and not again["ok"]
        and again["reason"] == "NO_ELIGIBLE_RUN"
        and reclaimed == []
        and get_run(created["run_id"])["status"] == "FAILED",
        f"run={run['status']} acquire={again.get('reason')}",
    )


def test_retry_cap(results, tmp_dir):
    isolate(tmp_dir, "retry-cap")
    created = enqueue_run()
    attempt_ns = []

    for step in range(MAX_ATTEMPTS):
        acquired = acquire_lease(
            f"w-{step}",
            lease_ttl_seconds=30,
            now=ts(step * 100),
        )
        results.check(
            f"retry cap acquire {step + 1} of {MAX_ATTEMPTS}",
            acquired["ok"]
            and acquired["attempt"]["attempt_n"] == step + 1,
            acquired.get("reason"),
        )
        attempt_ns.append(acquired["attempt"]["attempt_n"])
        reclaimed = reclaim_expired_leases(now=ts(step * 100 + 31))
        run = get_run(created["run_id"])
        expected_status = (
            "FAILED" if step + 1 >= MAX_ATTEMPTS else "PENDING"
        )
        results.check(
            f"retry cap reclaim {step + 1}",
            len(reclaimed) == 1
            and reclaimed[0]["run_status"] == expected_status
            and run["status"] == expected_status
            and run["attempt_count"] == step + 1,
            f"status={run['status']} count={run['attempt_count']}",
        )

    overflow = acquire_lease("w-overflow", lease_ttl_seconds=30, now=ts(900))
    attempts = list_attempts(created["run_id"])
    statuses = [item["status"] for item in attempts]
    results.check(
        "retry cap exhausted run becomes FAILED and cannot be acquired",
        not overflow["ok"]
        and overflow["reason"] == "NO_ELIGIBLE_RUN"
        and get_run(created["run_id"])["status"] == "FAILED"
        and get_run(created["run_id"])["attempt_count"] == MAX_ATTEMPTS
        and attempt_ns == list(range(1, MAX_ATTEMPTS + 1))
        and len(attempts) == MAX_ATTEMPTS
        and statuses == ["EXPIRED"] * MAX_ATTEMPTS,
        f"count={get_run(created['run_id'])['attempt_count']} statuses={statuses}",
    )


def test_rollback_partial_acquire(results, tmp_dir):
    isolate(tmp_dir, "rollback")
    created = enqueue_run()
    run_store.fail_after_attempt_insert = True
    raised = False
    try:
        acquire_lease("owner", lease_ttl_seconds=30, now=ts(0))
    except RuntimeError as exc:
        raised = str(exc) == "fail_after_attempt_insert"
    finally:
        reset_hooks()

    run = get_run(created["run_id"])
    attempts = list_attempts(created["run_id"])
    recovered = acquire_lease("owner", lease_ttl_seconds=30, now=ts(1))

    results.check(
        "transaction rollback leaves no half-created attempt/run state",
        raised
        and run["status"] == "PENDING"
        and run["attempt_count"] == 0
        and run["current_attempt_id"] is None
        and attempts == []
        and recovered["ok"]
        and recovered["attempt"]["attempt_n"] == 1
        and get_run(created["run_id"])["attempt_count"] == 1,
        f"status={run['status']} attempts={len(attempts)}",
    )


def test_fd_lifecycle_clean(results, tmp_dir):
    db_path = isolate(tmp_dir, "fds-clean")
    created = enqueue_run()
    acquired = acquire_lease("warmup", lease_ttl_seconds=30)
    complete_attempt(acquired["attempt"]["attempt_id"], "warmup")
    get_run(created["run_id"])

    gc.disable()
    try:
        before = count_open_fds()
        db_before = count_fds_for(db_path)
        for index in range(ITERATIONS):
            item = enqueue_run()
            leased = acquire_lease(f"fd-{index}", lease_ttl_seconds=30)
            complete_attempt(
                leased["attempt"]["attempt_id"],
                f"fd-{index}",
            )
            get_run(item["run_id"])
            list_attempts(item["run_id"])
        after = count_open_fds()
        db_after = count_fds_for(db_path)
    finally:
        gc.enable()
        gc.collect()

    results.check(
        "SQLite connections close deterministically with GC disabled",
        after <= before + 4 and db_after <= max(db_before, 0) + 2,
        f"process_fds {before}->{after}; db_fds {db_before}->{db_after}",
    )


def test_compile_and_live_untouched(results, tmp_dir):
    isolate(tmp_dir, "compile")
    import compileall

    compiled = compileall.compile_file(str(BOT_DIR / "run_store.py"), quiet=1)
    results.check("run_store.py compiles", compiled)
    results.check(
        "callable ownership API",
        callable(enqueue_run)
        and callable(acquire_lease)
        and callable(heartbeat)
        and callable(complete_attempt)
        and callable(fail_attempt)
        and callable(reclaim_expired_leases),
    )
    results.check(
        "live data/runs.db was not created",
        not (LIVE_DATA / "runs.db").exists(),
    )


def main():
    results = Results()
    reset_hooks()

    if (LIVE_DATA / "runs.db").exists():
        print("REFUSING TO RUN: live data/runs.db already exists")
        return 1

    with tempfile.TemporaryDirectory(prefix="atlas-r4-") as tmp_dir:
        assert_not_live(tmp_dir)
        print(f"Using temp dir: {tmp_dir}")
        print(f"Live data dir (untouched): {LIVE_DATA}")
        print()

        tests = [
            test_fresh_schema,
            test_concurrent_initialize,
            test_canonical_offset_equivalence,
            test_premature_reclaim_offset,
            test_late_reclaim_offset,
            test_utc_expiry_boundary,
            test_naive_timestamps_rejected,
            test_happy_path,
            test_thread_acquire_one_winner,
            test_multiprocess_acquire_stress,
            test_duplicate_complete_and_wrong_worker,
            test_heartbeat_extend_and_no_shorten,
            test_heartbeat_after_expiry,
            test_crash_reclaim_and_stale_worker,
            test_concurrent_reclaim,
            test_explicit_fail_terminal,
            test_rollback_partial_acquire,
            test_retry_cap,
            test_fd_lifecycle_clean,
            test_compile_and_live_untouched,
        ]

        for test in tests:
            reset_hooks()
            try:
                test(results, tmp_dir)
            except Exception:
                results.failed.append(test.__name__)
                print(f"FAIL  {test.__name__}  crashed")
                traceback.print_exc()
            finally:
                reset_hooks()

    print()
    print(f"Passed: {len(results.passed)}")
    print(f"Failed: {len(results.failed)}")
    if results.failed:
        print("Failed tests: " + ", ".join(results.failed))
        return 1

    print("All isolated R4 run-durability tests passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
