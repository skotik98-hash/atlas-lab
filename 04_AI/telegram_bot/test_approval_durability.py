#!/usr/bin/env python3
"""Isolated approval-to-task durability tests. Uses temporary databases only."""

import sqlite3
import subprocess
import sys
import tempfile
import threading
import traceback
from pathlib import Path

import activity_store
import approval_store
import task_store
from approval_store import (
    PROP_APPLIED,
    PROP_INCOMPATIBLE,
    PROP_NONE,
    PROP_PENDING,
    apply_approval_decision,
    recover_pending_propagations,
)


LIVE_DATA = Path(__file__).resolve().parent / "data"
BOT_DIR = Path(__file__).resolve().parent

REQUIRED_APPROVAL_COLUMNS = {
    "approval_id",
    "title",
    "action_type",
    "details",
    "status",
    "created_at",
    "decided_at",
    "decided_by",
    "decision",
    "task_id",
    "propagation_status",
    "propagation_error",
}

REQUIRED_APPROVAL_INDEXES = {
    "idx_approvals_task_id",
    "idx_approvals_propagation",
}

MIGRATION_WORKER = r"""
import sys
from pathlib import Path

sys.path.insert(0, sys.argv[1])

import approval_store

approval_store.DB_PATH = Path(sys.argv[2])
approval_store.initialize()
"""


def assert_not_live(path):
    resolved = Path(path).resolve()
    live = LIVE_DATA.resolve()
    if resolved == live or live in resolved.parents:
        raise AssertionError(f"Refusing to use live database path: {resolved}")


def point_store_at_temp(module, tmp_dir, filename):
    db_path = Path(tmp_dir) / filename
    assert_not_live(db_path)

    if hasattr(module, "DB_PATH"):
        if isinstance(getattr(module, "DB_PATH"), str):
            module.DB_PATH = str(db_path)
        else:
            module.DB_PATH = db_path

    return db_path


def isolate_stores(tmp_dir):
    return {
        "activity": point_store_at_temp(
            activity_store, tmp_dir, "activity.db"
        ),
        "approvals": point_store_at_temp(
            approval_store, tmp_dir, "approvals.db"
        ),
        "tasks": point_store_at_temp(
            task_store, tmp_dir, "tasks.db"
        ),
    }


def reset_hooks():
    approval_store.fail_after_decision = False
    approval_store.fail_after_task_before_mark = False


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


def make_linked(title="linked task"):
    task = task_store.create_task(title)
    approval_id = f"APR-{task['task_id']}-R3"
    created = approval_store.create_approval(
        approval_id,
        title,
        "TASK",
        "R3 linked approval",
        task_id=task["task_id"],
    )
    return task, approval_id, created


def test_happy_path_approve_and_reject(results, tmp_dir):
    isolate_stores(tmp_dir)

    task, approval_id, created = make_linked("approve me")
    outcome = apply_approval_decision(approval_id, "APPROVED", 1)
    approval = approval_store.get_approval(approval_id)
    after = task_store.get_task(task["task_id"])
    results.check(
        "linked APPROVED commits decision and task together",
        created is True
        and outcome["reason"] == "APPROVED"
        and outcome["ok"] is True
        and outcome["propagation"] == PROP_APPLIED
        and approval["status"] == "APPROVED"
        and approval["task_id"] == task["task_id"]
        and after["status"] == "IN_PROGRESS"
        and after["approval_id"] == approval_id,
    )

    rejected_task, rejected_id, _ = make_linked("reject me")
    rejected = apply_approval_decision(rejected_id, "REJECTED", 1)
    results.check(
        "linked REJECTED moves task to BLOCKED",
        rejected["reason"] == "REJECTED"
        and rejected["propagation"] == PROP_APPLIED
        and task_store.get_task(rejected_task["task_id"])["status"]
        == "BLOCKED",
    )


def test_unlinked_and_string_api(results, tmp_dir):
    isolate_stores(tmp_dir)
    task = task_store.create_task("must stay new")

    created = approval_store.create_approval(
        "APR-UNLINKED-001",
        "unlinked",
        "TEST",
        "no task",
    )
    decided = approval_store.decide_approval(
        "APR-UNLINKED-001",
        "APPROVED",
        1,
    )
    approval = approval_store.get_approval("APR-UNLINKED-001")
    results.check(
        "unlinked decide_approval string API unchanged",
        created is True
        and decided == "APPROVED"
        and approval["status"] == "APPROVED"
        and approval["task_id"] is None
        and approval["propagation_status"] == PROP_NONE
        and task_store.get_task(task["task_id"])["status"] == "NEW",
    )

    already = approval_store.decide_approval(
        "APR-UNLINKED-001",
        "REJECTED",
        1,
    )
    missing = approval_store.decide_approval(
        "APR-MISSING",
        "APPROVED",
        1,
    )
    results.check(
        "unlinked duplicate and missing results preserved",
        already == "ALREADY_DECIDED"
        and missing == "NOT_FOUND"
        and approval_store.get_approval("APR-UNLINKED-001")["decision"]
        == "APPROVED",
    )


def test_no_parse_of_task_id_convention(results, tmp_dir):
    isolate_stores(tmp_dir)
    task = task_store.create_task("do not infer")
    fake_id = f"{task['task_id']}-20260813-000000"
    approval_store.create_approval(
        fake_id,
        "looks linked",
        "TASK",
        "id only, no column",
    )
    outcome = apply_approval_decision(fake_id, "APPROVED", 1)
    after = task_store.get_task(task["task_id"])
    approval = approval_store.get_approval(fake_id)
    results.check(
        "TASK-* approval_id without task_id does not mutate task",
        outcome["reason"] == "APPROVED"
        and outcome["propagation"] == PROP_NONE
        and approval["task_id"] is None
        and after["status"] == "NEW",
    )


def test_duplicate_callback(results, tmp_dir):
    isolate_stores(tmp_dir)
    task, approval_id, _ = make_linked("dup")
    first = apply_approval_decision(approval_id, "APPROVED", 1)
    second = apply_approval_decision(approval_id, "APPROVED", 1)
    third = apply_approval_decision(approval_id, "REJECTED", 2)
    after = task_store.get_task(task["task_id"])
    results.check(
        "duplicate approval callbacks remain safe",
        first["reason"] == "APPROVED"
        and second["reason"] == "ALREADY_DECIDED"
        and third["reason"] == "ALREADY_DECIDED"
        and second["propagation"] == PROP_APPLIED
        and third["decision"] == "APPROVED"
        and after["status"] == "IN_PROGRESS",
    )


def test_concurrent_same_decision(results, tmp_dir):
    isolate_stores(tmp_dir)
    task, approval_id, _ = make_linked("concurrent same")
    outcomes = []
    barrier = threading.Barrier(2)

    def attempt():
        barrier.wait()
        outcomes.append(
            apply_approval_decision(approval_id, "APPROVED", 1)
        )

    threads = [
        threading.Thread(target=attempt),
        threading.Thread(target=attempt),
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    wins = sum(1 for item in outcomes if item["reason"] == "APPROVED")
    already = sum(
        1 for item in outcomes if item["reason"] == "ALREADY_DECIDED"
    )
    approval = approval_store.get_approval(approval_id)
    after = task_store.get_task(task["task_id"])
    results.check(
        "concurrent duplicate approve has one CAS winner",
        wins == 1
        and already == 1
        and approval["status"] == "APPROVED"
        and approval["propagation_status"] == PROP_APPLIED
        and after["status"] == "IN_PROGRESS"
        and len(outcomes) == 2,
        f"wins={wins} already={already}",
    )


def test_concurrent_contradictory_decisions(results, tmp_dir):
    isolate_stores(tmp_dir)
    task, approval_id, _ = make_linked("concurrent conflict")
    outcomes = []
    barrier = threading.Barrier(2)

    def attempt(decision):
        barrier.wait()
        outcomes.append(
            apply_approval_decision(approval_id, decision, 1)
        )

    threads = [
        threading.Thread(target=attempt, args=("APPROVED",)),
        threading.Thread(target=attempt, args=("REJECTED",)),
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    stored = approval_store.get_approval(approval_id)
    after = task_store.get_task(task["task_id"])
    winner_reasons = [
        item["reason"]
        for item in outcomes
        if item["reason"] in {"APPROVED", "REJECTED"}
    ]
    expected_task = (
        "IN_PROGRESS" if stored["decision"] == "APPROVED" else "BLOCKED"
    )
    results.check(
        "concurrent approve/reject cannot both commit",
        len(winner_reasons) == 1
        and stored["status"] == stored["decision"]
        and stored["propagation_status"] == PROP_APPLIED
        and after["status"] == expected_task
        and {item["reason"] for item in outcomes}
        == {stored["decision"], "ALREADY_DECIDED"},
        f"stored={stored['decision']} task={after['status']}",
    )


def test_terminal_task(results, tmp_dir):
    isolate_stores(tmp_dir)
    task = task_store.create_task("already done")
    task_store.update_task_status(task["task_id"], "IN_PROGRESS")
    task_store.update_task_status(task["task_id"], "DONE")
    completed_at = task_store.get_task(task["task_id"])["completed_at"]

    approval_id = "APR-TERMINAL-001"
    approval_store.create_approval(
        approval_id,
        "too late",
        "TASK",
        "terminal",
        task_id=task["task_id"],
    )
    outcome = apply_approval_decision(approval_id, "APPROVED", 1)
    after = task_store.get_task(task["task_id"])
    approval = approval_store.get_approval(approval_id)
    results.check(
        "approval against terminal task does not resurrect",
        outcome["reason"] == "APPROVED"
        and outcome["propagation"] == PROP_INCOMPATIBLE
        and approval["status"] == "APPROVED"
        and approval["propagation_error"] == "INVALID_TRANSITION"
        and after["status"] == "DONE"
        and after["completed_at"] == completed_at,
    )

    retry = apply_approval_decision(approval_id, "REJECTED", 1)
    still = task_store.get_task(task["task_id"])
    results.check(
        "retry of incompatible terminal approval stays safe",
        retry["reason"] == "ALREADY_DECIDED"
        and retry["propagation"] == PROP_INCOMPATIBLE
        and still["status"] == "DONE"
        and still["completed_at"] == completed_at,
    )


def test_missing_linked_task(results, tmp_dir):
    isolate_stores(tmp_dir)
    approval_store.create_approval(
        "APR-MISSING-TASK",
        "ghost",
        "TASK",
        "no such task",
        task_id="TASK-9999",
    )
    outcome = apply_approval_decision("APR-MISSING-TASK", "APPROVED", 1)
    approval = approval_store.get_approval("APR-MISSING-TASK")
    results.check(
        "missing linked task is detectable, not silent",
        outcome["reason"] == "APPROVED"
        and outcome["propagation"] == PROP_INCOMPATIBLE
        and approval["propagation_error"] == "TASK_NOT_FOUND"
        and approval["status"] == "APPROVED",
    )


def test_failure_between_decision_and_task(results, tmp_dir):
    isolate_stores(tmp_dir)
    task, approval_id, _ = make_linked("crash window")
    approval_store.fail_after_decision = True
    raised = False
    try:
        apply_approval_decision(approval_id, "APPROVED", 1)
    except RuntimeError:
        raised = True
    finally:
        reset_hooks()

    approval = approval_store.get_approval(approval_id)
    after = task_store.get_task(task["task_id"])
    results.check(
        "failure after decision leaves PENDING propagation",
        raised is True
        and approval["status"] == "APPROVED"
        and approval["propagation_status"] == PROP_PENDING
        and after["status"] == "NEW",
    )

    recovered = apply_approval_decision(approval_id, "APPROVED", 1)
    approval = approval_store.get_approval(approval_id)
    after = task_store.get_task(task["task_id"])
    results.check(
        "duplicate callback recovers pending task propagation",
        recovered["reason"] == "ALREADY_DECIDED"
        and recovered["recovered"] is True
        and recovered["propagation"] == PROP_APPLIED
        and approval["propagation_status"] == PROP_APPLIED
        and after["status"] == "IN_PROGRESS",
    )


def test_restart_recovery_and_idempotent_mark(results, tmp_dir):
    isolate_stores(tmp_dir)
    task, approval_id, _ = make_linked("restart")
    approval_store.fail_after_decision = True
    try:
        apply_approval_decision(approval_id, "APPROVED", 1)
    except RuntimeError:
        pass
    finally:
        reset_hooks()

    recovered = recover_pending_propagations()
    approval = approval_store.get_approval(approval_id)
    after = task_store.get_task(task["task_id"])
    results.check(
        "restart recover_pending_propagations applies task",
        len(recovered) == 1
        and recovered[0]["propagation"] == PROP_APPLIED
        and approval["propagation_status"] == PROP_APPLIED
        and after["status"] == "IN_PROGRESS",
    )

    empty = recover_pending_propagations()
    results.check(
        "second recovery pass is a no-op",
        empty == [],
    )

    task2, approval_id2, _ = make_linked("mark crash")
    approval_store.fail_after_task_before_mark = True
    try:
        apply_approval_decision(approval_id2, "APPROVED", 1)
    except RuntimeError:
        pass
    finally:
        reset_hooks()

    mid = approval_store.get_approval(approval_id2)
    mid_task = task_store.get_task(task2["task_id"])
    retry = recover_pending_propagations()
    final = approval_store.get_approval(approval_id2)
    results.check(
        "task write without mark is recovered idempotently",
        mid["propagation_status"] == PROP_PENDING
        and mid_task["status"] == "IN_PROGRESS"
        and len(retry) == 1
        and retry[0]["propagation"] == PROP_APPLIED
        and final["propagation_status"] == PROP_APPLIED
        and task_store.get_task(task2["task_id"])["status"]
        == "IN_PROGRESS",
    )


def test_audit_matches_commit(results, tmp_dir):
    isolate_stores(tmp_dir)
    _, approval_id, _ = make_linked("audit")
    apply_approval_decision(approval_id, "APPROVED", 7)
    apply_approval_decision(approval_id, "REJECTED", 8)

    events = activity_store.list_events(limit=50)
    decided = [
        event
        for event in events
        if event["event_type"] == "APPROVAL_DECIDED"
        and (event.get("metadata") or {}).get("approval_id") == approval_id
    ]
    applied = [
        event
        for event in events
        if event["event_type"] == "APPROVAL_TASK_APPLIED"
        and (event.get("metadata") or {}).get("approval_id") == approval_id
    ]
    results.check(
        "audit logs one decision and one successful propagation",
        len(decided) == 1
        and decided[0]["metadata"]["decision"] == "APPROVED"
        and decided[0]["metadata"]["decided_by"] == 7
        and len(applied) == 1,
        f"decided={len(decided)} applied={len(applied)}",
    )


def test_legacy_schema_migration(results, tmp_dir):
    legacy_dir = Path(tmp_dir) / "legacy"
    legacy_dir.mkdir()
    isolate_stores(legacy_dir)
    db_path = Path(legacy_dir) / "approvals.db"
    assert_not_live(db_path)

    raw = sqlite3.connect(db_path)
    try:
        raw.execute(
            """
            CREATE TABLE approvals (
                approval_id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                action_type TEXT NOT NULL,
                details TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'PENDING',
                created_at TEXT NOT NULL,
                decided_at TEXT,
                decided_by INTEGER,
                decision TEXT
            )
            """
        )
        raw.execute(
            """
            INSERT INTO approvals (
                approval_id, title, action_type, details, status, created_at
            )
            VALUES (
                'APR-LEGACY', 'legacy', 'TEST', 'old row',
                'PENDING', '2026-08-13T00:00:00+00:00'
            )
            """
        )
        raw.commit()
    finally:
        raw.close()

    fetched = approval_store.get_approval("APR-LEGACY")
    decided = apply_approval_decision("APR-LEGACY", "APPROVED", 1)
    after = approval_store.get_approval("APR-LEGACY")
    results.check(
        "legacy approvals table gains link columns and remains decidable",
        fetched["task_id"] is None
        and fetched["propagation_status"] == PROP_NONE
        and decided["reason"] == "APPROVED"
        and after["propagation_status"] == PROP_NONE
        and after["status"] == "APPROVED",
    )

    task = task_store.create_task("legacy link")
    created = approval_store.create_approval(
        "APR-LEGACY-LINK",
        "new on old schema",
        "TASK",
        "after alter",
        task_id=task["task_id"],
    )
    linked = apply_approval_decision("APR-LEGACY-LINK", "APPROVED", 1)
    results.check(
        "new linked approval works after ALTER TABLE",
        created is True
        and linked["propagation"] == PROP_APPLIED
        and task_store.get_task(task["task_id"])["status"] == "IN_PROGRESS",
    )


def _write_legacy_approvals_db(db_path):
    assert_not_live(db_path)
    raw = sqlite3.connect(db_path)
    try:
        raw.execute(
            """
            CREATE TABLE approvals (
                approval_id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                action_type TEXT NOT NULL,
                details TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'PENDING',
                created_at TEXT NOT NULL,
                decided_at TEXT,
                decided_by INTEGER,
                decision TEXT
            )
            """
        )
        raw.execute(
            """
            INSERT INTO approvals (
                approval_id, title, action_type, details, status, created_at
            )
            VALUES (
                'APR-LEGACY-RACE', 'keep me', 'TEST', 'concurrent migrate',
                'PENDING', '2026-08-13T00:00:00+00:00'
            )
            """
        )
        raw.commit()
    finally:
        raw.close()


def _read_schema(db_path):
    raw = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    try:
        columns = {
            row[1] for row in raw.execute("PRAGMA table_info(approvals)")
        }
        indexes = {
            row[0]
            for row in raw.execute(
                """
                SELECT name
                FROM sqlite_master
                WHERE type = 'index'
                  AND tbl_name = 'approvals'
                  AND name IS NOT NULL
                """
            )
        }
        row = raw.execute(
            """
            SELECT approval_id, title, action_type, details, status
            FROM approvals
            WHERE approval_id = 'APR-LEGACY-RACE'
            """
        ).fetchone()
        count = raw.execute(
            "SELECT COUNT(*) FROM approvals"
        ).fetchone()[0]
        return columns, indexes, row, count
    finally:
        raw.close()


def _run_initializers(db_path, workers):
    processes = [
        subprocess.Popen(
            [
                sys.executable,
                "-c",
                MIGRATION_WORKER,
                str(BOT_DIR),
                str(db_path),
            ],
            cwd=str(BOT_DIR),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        for _ in range(workers)
    ]
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
    return failures


def _assert_migrated_schema(results, name, db_path):
    columns, indexes, row, count = _read_schema(db_path)
    results.check(
        name,
        REQUIRED_APPROVAL_COLUMNS <= columns
        and REQUIRED_APPROVAL_INDEXES <= indexes
        and count == 1
        and row is not None
        and row[0] == "APR-LEGACY-RACE"
        and row[1] == "keep me"
        and row[2] == "TEST"
        and row[3] == "concurrent migrate"
        and row[4] == "PENDING",
        f"columns={sorted(columns)} indexes={sorted(indexes)} count={count}",
    )


def test_concurrent_legacy_schema_migration(results, tmp_dir):
    two_process_rounds = 8
    multi_workers = 8
    multi_rounds = 5
    failed_rounds = 0

    for round_id in range(two_process_rounds):
        race_dir = Path(tmp_dir) / f"race-2p-{round_id}"
        race_dir.mkdir()
        db_path = race_dir / "approvals.db"
        _write_legacy_approvals_db(db_path)
        failures = _run_initializers(db_path, workers=2)
        if failures:
            failed_rounds += 1
            results.check(
                f"two-process bot/watcher-equivalent race round {round_id}",
                False,
                failures[0]["stderr"][:400],
            )
        else:
            _assert_migrated_schema(
                results,
                f"two-process bot/watcher-equivalent race round {round_id}",
                db_path,
            )

    for round_id in range(multi_rounds):
        race_dir = Path(tmp_dir) / f"race-np-{round_id}"
        race_dir.mkdir()
        db_path = race_dir / "approvals.db"
        _write_legacy_approvals_db(db_path)
        failures = _run_initializers(db_path, workers=multi_workers)
        if failures:
            failed_rounds += 1
            results.check(
                f"multi-process migration race round {round_id}",
                False,
                failures[0]["stderr"][:400],
            )
        else:
            _assert_migrated_schema(
                results,
                f"multi-process migration race round {round_id}",
                db_path,
            )

    results.check(
        "concurrent legacy migration had zero initializer failures",
        failed_rounds == 0,
        f"failed_rounds={failed_rounds}",
    )


def test_bot_no_longer_parses_task_ids(results, tmp_dir):
    isolate_stores(tmp_dir)
    bot_path = Path(__file__).resolve().parent / "bot.py"
    text = bot_path.read_text(encoding="utf-8")
    results.check(
        "bot.py no longer parses TASK-* approval IDs",
        "approval_id.startswith(\"TASK-\")" not in text
        and "apply_task_approval_decision" not in text
        and "apply_approval_decision" in text
        and "recover_pending_propagations" in text,
    )


def test_import_and_compile(results, tmp_dir):
    isolate_stores(tmp_dir)
    import compileall

    root = Path(__file__).resolve().parent
    targets = [
        root / "approval_store.py",
        root / "task_store.py",
        root / "bot.py",
        root / "sqlite_lifecycle.py",
    ]
    compiled = all(
        compileall.compile_file(str(path), quiet=1)
        for path in targets
    )
    results.check("R3 modules compile", compiled)

    import importlib
    importlib.reload(approval_store)
    isolate_stores(tmp_dir)
    results.check(
        "apply_approval_decision importable",
        callable(approval_store.apply_approval_decision)
        and callable(approval_store.recover_pending_propagations),
    )


def main():
    results = Results()
    reset_hooks()

    with tempfile.TemporaryDirectory(prefix="atlas-r3-") as tmp_dir:
        assert_not_live(tmp_dir)
        print(f"Using temp dir: {tmp_dir}")
        print(f"Live data dir (untouched): {LIVE_DATA}")
        print()

        tests = [
            test_happy_path_approve_and_reject,
            test_unlinked_and_string_api,
            test_no_parse_of_task_id_convention,
            test_duplicate_callback,
            test_concurrent_same_decision,
            test_concurrent_contradictory_decisions,
            test_terminal_task,
            test_missing_linked_task,
            test_failure_between_decision_and_task,
            test_restart_recovery_and_idempotent_mark,
            test_audit_matches_commit,
            test_legacy_schema_migration,
            test_concurrent_legacy_schema_migration,
            test_bot_no_longer_parses_task_ids,
            test_import_and_compile,
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

    print("All isolated R3 approval-durability tests passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
