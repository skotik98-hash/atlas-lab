import json
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from pathlib import Path

from sqlite_lifecycle import managed_connection


DB_PATH = Path(__file__).with_name("data") / "runs.db"

MAX_ATTEMPTS = 5
DEFAULT_LEASE_TTL_SECONDS = 30

WORK_TYPE_NOOP = "NOOP_PROBE"
ALLOWED_WORK_TYPES = frozenset({WORK_TYPE_NOOP})

RUN_PENDING = "PENDING"
RUN_LEASED = "LEASED"
RUN_SUCCEEDED = "SUCCEEDED"
RUN_FAILED = "FAILED"
RUN_CANCELLED = "CANCELLED"

RUN_STATUSES = {
    RUN_PENDING,
    RUN_LEASED,
    RUN_SUCCEEDED,
    RUN_FAILED,
    RUN_CANCELLED,
}

ATTEMPT_LEASED = "LEASED"
ATTEMPT_SUCCEEDED = "SUCCEEDED"
ATTEMPT_FAILED = "FAILED"
ATTEMPT_EXPIRED = "EXPIRED"

ATTEMPT_STATUSES = {
    ATTEMPT_LEASED,
    ATTEMPT_SUCCEEDED,
    ATTEMPT_FAILED,
    ATTEMPT_EXPIRED,
}

# Test-only hook. Production code never sets this.
fail_after_attempt_insert = False


def utc_now():
    return _as_iso(datetime.now(timezone.utc))


def _as_dt(value):
    if isinstance(value, datetime):
        parsed = value
    else:
        try:
            parsed = datetime.fromisoformat(str(value))
        except ValueError as exc:
            raise ValueError(f"invalid timestamp: {value!r}") from exc
    if parsed.tzinfo is None:
        raise ValueError(
            "timestamp must include a UTC offset; naive values are rejected"
        )
    return parsed.astimezone(timezone.utc)


def _as_iso(value):
    return _as_dt(value).isoformat()


def _shift(now, seconds):
    return _as_iso(_as_dt(now) + timedelta(seconds=int(seconds)))


def _normalize_worker_id(worker_id):
    worker_id = str(worker_id or "").strip()
    if not worker_id:
        raise ValueError("worker_id must be a non-empty logical identity")
    return worker_id


def _normalize_ttl(lease_ttl_seconds):
    ttl = int(lease_ttl_seconds)
    if ttl <= 0:
        raise ValueError("lease_ttl_seconds must be a positive integer")
    return ttl


def _normalize_work_type(work_type):
    work_type = str(work_type or "").strip() or WORK_TYPE_NOOP
    if work_type not in ALLOWED_WORK_TYPES:
        raise ValueError(f"Unsupported work_type: {work_type}")
    return work_type


def _result(ok, reason, **extra):
    payload = {"ok": bool(ok), "reason": reason}
    payload.update(extra)
    return payload


def _decode_run(row):
    if row is None:
        return None

    item = dict(row)
    raw = item.get("payload_json") or "{}"
    try:
        item["payload"] = json.loads(raw)
    except json.JSONDecodeError:
        item["payload"] = {}
    return item


def _decode_attempt(row):
    if row is None:
        return None
    return dict(row)


def initialize():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(str(DB_PATH), timeout=30)
    connection.row_factory = sqlite3.Row
    connection.isolation_level = None

    try:
        connection.execute("PRAGMA busy_timeout=30000")
        connection.execute("BEGIN IMMEDIATE")
        try:
            _ensure_schema(connection)
            connection.execute("COMMIT")
        except Exception:
            connection.execute("ROLLBACK")
            raise
    finally:
        connection.close()


def _ensure_schema(db):
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_id TEXT UNIQUE,
            work_type TEXT NOT NULL,
            payload_json TEXT NOT NULL DEFAULT '{}',
            status TEXT NOT NULL,
            attempt_count INTEGER NOT NULL DEFAULT 0,
            current_attempt_id TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
        """
    )
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS attempts (
            attempt_id TEXT PRIMARY KEY,
            run_id TEXT NOT NULL,
            attempt_n INTEGER NOT NULL,
            status TEXT NOT NULL,
            worker_id TEXT NOT NULL,
            lease_until TEXT NOT NULL,
            heartbeat_at TEXT NOT NULL,
            started_at TEXT NOT NULL,
            finished_at TEXT,
            error TEXT,
            UNIQUE (run_id, attempt_n)
        )
        """
    )
    db.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_runs_status_created
        ON runs(status, created_at, run_id)
        """
    )
    db.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_attempts_run_id
        ON attempts(run_id)
        """
    )
    db.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_attempts_lease
        ON attempts(status, lease_until)
        """
    )


def connect():
    initialize()

    connection = sqlite3.connect(str(DB_PATH), timeout=30)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA busy_timeout=30000")
    return managed_connection(connection)


@contextmanager
def exclusive_connection():
    """Single-writer transaction: BEGIN IMMEDIATE, R1 close, rollback on failure."""
    initialize()

    connection = sqlite3.connect(str(DB_PATH), timeout=30)
    connection.row_factory = sqlite3.Row
    connection.isolation_level = None
    connection.execute("PRAGMA busy_timeout=30000")

    with managed_connection(connection) as db:
        db.execute("BEGIN IMMEDIATE")
        yield db


def enqueue_run(work_type=WORK_TYPE_NOOP, payload=None):
    work_type = _normalize_work_type(work_type)
    now = utc_now()
    payload_json = json.dumps(payload or {}, ensure_ascii=False)

    with exclusive_connection() as db:
        cursor = db.execute(
            """
            INSERT INTO runs (
                work_type,
                payload_json,
                status,
                attempt_count,
                current_attempt_id,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?, 0, NULL, ?, ?)
            """,
            (work_type, payload_json, RUN_PENDING, now, now),
        )
        rowid = cursor.lastrowid
        run_id = f"RUN-{rowid:04d}"
        db.execute(
            """
            UPDATE runs
            SET run_id = ?
            WHERE id = ?
            """,
            (run_id, rowid),
        )

    return get_run(run_id)


def get_run(run_id):
    initialize()

    with connect() as db:
        row = db.execute(
            """
            SELECT *
            FROM runs
            WHERE run_id = ?
            """,
            (run_id,),
        ).fetchone()

    return _decode_run(row)


def get_attempt(attempt_id):
    initialize()

    with connect() as db:
        row = db.execute(
            """
            SELECT *
            FROM attempts
            WHERE attempt_id = ?
            """,
            (attempt_id,),
        ).fetchone()

    return _decode_attempt(row)


def list_attempts(run_id):
    initialize()

    with connect() as db:
        rows = db.execute(
            """
            SELECT *
            FROM attempts
            WHERE run_id = ?
            ORDER BY attempt_n ASC
            """,
            (run_id,),
        ).fetchall()

    return [_decode_attempt(row) for row in rows]


def _load_run(db, run_id):
    return _decode_run(
        db.execute(
            """
            SELECT *
            FROM runs
            WHERE run_id = ?
            """,
            (run_id,),
        ).fetchone()
    )


def _load_attempt(db, attempt_id):
    return _decode_attempt(
        db.execute(
            """
            SELECT *
            FROM attempts
            WHERE attempt_id = ?
            """,
            (attempt_id,),
        ).fetchone()
    )


def _ownership_snapshot(db, attempt_id):
    attempt = _load_attempt(db, attempt_id)
    if attempt is None:
        return None, None
    return attempt, _load_run(db, attempt["run_id"])


def _lease_valid(attempt, now):
    return _as_dt(attempt["lease_until"]) > _as_dt(now)


def _is_current_owner(run, attempt, worker_id, now):
    if run is None or attempt is None:
        return False, "NOT_FOUND"
    if attempt["worker_id"] != worker_id:
        return False, "WRONG_WORKER"
    if run["current_attempt_id"] != attempt["attempt_id"]:
        return False, "NOT_CURRENT"
    if run["status"] != RUN_LEASED:
        return False, "NOT_LEASED"
    if attempt["status"] != ATTEMPT_LEASED:
        return False, "NOT_LEASED"
    if not _lease_valid(attempt, now):
        return False, "LEASE_EXPIRED"
    return True, "OK"


def acquire_lease(
    worker_id,
    lease_ttl_seconds=DEFAULT_LEASE_TTL_SECONDS,
    work_types=None,
    now=None,
):
    worker_id = _normalize_worker_id(worker_id)
    ttl = _normalize_ttl(lease_ttl_seconds)
    now = _as_iso(now or utc_now())
    lease_until = _shift(now, ttl)

    if work_types is None:
        allowed = tuple(sorted(ALLOWED_WORK_TYPES))
    else:
        allowed = tuple(
            _normalize_work_type(item) for item in work_types
        )
        if not allowed:
            return _result(False, "NO_ELIGIBLE_RUN")

    placeholders = ",".join(["?"] * len(allowed))

    with exclusive_connection() as db:
        row = db.execute(
            f"""
            SELECT *
            FROM runs
            WHERE status = ?
              AND attempt_count < ?
              AND work_type IN ({placeholders})
            ORDER BY created_at ASC, run_id ASC
            LIMIT 1
            """,
            (RUN_PENDING, MAX_ATTEMPTS, *allowed),
        ).fetchone()

        if row is None:
            return _result(False, "NO_ELIGIBLE_RUN")

        run = _decode_run(row)
        next_n = int(run["attempt_count"]) + 1
        attempt_id = f"ATT-{run['run_id']}-{next_n:02d}"

        db.execute(
            """
            INSERT INTO attempts (
                attempt_id,
                run_id,
                attempt_n,
                status,
                worker_id,
                lease_until,
                heartbeat_at,
                started_at,
                finished_at,
                error
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, NULL, NULL)
            """,
            (
                attempt_id,
                run["run_id"],
                next_n,
                ATTEMPT_LEASED,
                worker_id,
                lease_until,
                now,
                now,
            ),
        )

        if fail_after_attempt_insert:
            raise RuntimeError("fail_after_attempt_insert")

        updated = db.execute(
            """
            UPDATE runs
            SET status = ?,
                attempt_count = attempt_count + 1,
                current_attempt_id = ?,
                updated_at = ?
            WHERE run_id = ?
              AND status = ?
              AND attempt_count = ?
              AND attempt_count < ?
            """,
            (
                RUN_LEASED,
                attempt_id,
                now,
                run["run_id"],
                RUN_PENDING,
                run["attempt_count"],
                MAX_ATTEMPTS,
            ),
        )

        if updated.rowcount != 1:
            raise RuntimeError(
                "acquire_lease lost CAS while holding IMMEDIATE lock"
            )

        attempt = _load_attempt(db, attempt_id)
        owned = _load_run(db, run["run_id"])

    return _result(
        True,
        "OK",
        attempt=attempt,
        run=owned,
    )


def heartbeat(
    attempt_id,
    worker_id,
    lease_ttl_seconds=DEFAULT_LEASE_TTL_SECONDS,
    now=None,
):
    worker_id = _normalize_worker_id(worker_id)
    ttl = _normalize_ttl(lease_ttl_seconds)
    now = _as_iso(now or utc_now())
    candidate_until = _shift(now, ttl)

    with exclusive_connection() as db:
        attempt, run = _ownership_snapshot(db, attempt_id)
        ok, reason = _is_current_owner(run, attempt, worker_id, now)
        if not ok:
            return _result(False, reason, attempt=attempt, run=run)

        current_until = attempt["lease_until"]
        if _as_dt(candidate_until) > _as_dt(current_until):
            new_until = candidate_until
            extended = True
        else:
            new_until = current_until
            extended = False

        attempt_rows = db.execute(
            """
            UPDATE attempts
            SET heartbeat_at = ?,
                lease_until = ?
            WHERE attempt_id = ?
              AND worker_id = ?
              AND status = ?
            """,
            (
                now,
                new_until,
                attempt_id,
                worker_id,
                ATTEMPT_LEASED,
            ),
        )
        run_rows = db.execute(
            """
            UPDATE runs
            SET updated_at = ?
            WHERE run_id = ?
              AND status = ?
              AND current_attempt_id = ?
            """,
            (
                now,
                run["run_id"],
                RUN_LEASED,
                attempt_id,
            ),
        )

        if attempt_rows.rowcount != 1 or run_rows.rowcount != 1:
            return _result(False, "NOT_CURRENT")

        attempt = _load_attempt(db, attempt_id)
        run = _load_run(db, run["run_id"])

    return _result(
        True,
        "OK",
        extended=extended,
        lease_until=attempt["lease_until"],
        attempt=attempt,
        run=run,
    )


def complete_attempt(attempt_id, worker_id, now=None):
    worker_id = _normalize_worker_id(worker_id)
    now = _as_iso(now or utc_now())

    with exclusive_connection() as db:
        attempt, run = _ownership_snapshot(db, attempt_id)
        if attempt is None or run is None:
            return _result(False, "NOT_FOUND")

        if (
            attempt["status"] == ATTEMPT_SUCCEEDED
            and run["status"] == RUN_SUCCEEDED
            and run["current_attempt_id"] == attempt_id
            and attempt["worker_id"] == worker_id
        ):
            return _result(
                True,
                "ALREADY_SUCCEEDED",
                attempt=attempt,
                run=run,
            )

        if run["current_attempt_id"] != attempt_id:
            return _result(False, "NOT_CURRENT", attempt=attempt, run=run)
        if attempt["worker_id"] != worker_id:
            return _result(False, "WRONG_WORKER", attempt=attempt, run=run)

        ok, reason = _is_current_owner(run, attempt, worker_id, now)
        if not ok:
            return _result(False, reason, attempt=attempt, run=run)

        attempt_rows = db.execute(
            """
            UPDATE attempts
            SET status = ?,
                finished_at = ?,
                error = NULL
            WHERE attempt_id = ?
              AND worker_id = ?
              AND status = ?
            """,
            (
                ATTEMPT_SUCCEEDED,
                now,
                attempt_id,
                worker_id,
                ATTEMPT_LEASED,
            ),
        )
        run_rows = db.execute(
            """
            UPDATE runs
            SET status = ?,
                updated_at = ?
            WHERE run_id = ?
              AND status = ?
              AND current_attempt_id = ?
            """,
            (
                RUN_SUCCEEDED,
                now,
                run["run_id"],
                RUN_LEASED,
                attempt_id,
            ),
        )

        if attempt_rows.rowcount != 1 or run_rows.rowcount != 1:
            return _result(False, "NOT_CURRENT")

        attempt = _load_attempt(db, attempt_id)
        run = _load_run(db, run["run_id"])

    return _result(True, "OK", attempt=attempt, run=run)


def fail_attempt(attempt_id, worker_id, error=None, now=None):
    worker_id = _normalize_worker_id(worker_id)
    now = _as_iso(now or utc_now())
    error_text = None if error is None else str(error)

    with exclusive_connection() as db:
        attempt, run = _ownership_snapshot(db, attempt_id)
        if attempt is None or run is None:
            return _result(False, "NOT_FOUND")

        if run["current_attempt_id"] != attempt_id:
            return _result(False, "NOT_CURRENT", attempt=attempt, run=run)
        if attempt["worker_id"] != worker_id:
            return _result(False, "WRONG_WORKER", attempt=attempt, run=run)

        ok, reason = _is_current_owner(run, attempt, worker_id, now)
        if not ok:
            return _result(False, reason, attempt=attempt, run=run)

        attempt_rows = db.execute(
            """
            UPDATE attempts
            SET status = ?,
                finished_at = ?,
                error = ?
            WHERE attempt_id = ?
              AND worker_id = ?
              AND status = ?
            """,
            (
                ATTEMPT_FAILED,
                now,
                error_text,
                attempt_id,
                worker_id,
                ATTEMPT_LEASED,
            ),
        )
        run_rows = db.execute(
            """
            UPDATE runs
            SET status = ?,
                updated_at = ?
            WHERE run_id = ?
              AND status = ?
              AND current_attempt_id = ?
            """,
            (
                RUN_FAILED,
                now,
                run["run_id"],
                RUN_LEASED,
                attempt_id,
            ),
        )

        if attempt_rows.rowcount != 1 or run_rows.rowcount != 1:
            return _result(False, "NOT_CURRENT")

        attempt = _load_attempt(db, attempt_id)
        run = _load_run(db, run["run_id"])

    return _result(True, "OK", attempt=attempt, run=run)


def reclaim_expired_leases(now=None):
    now = _as_iso(now or utc_now())
    reclaimed = []

    with exclusive_connection() as db:
        rows = db.execute(
            """
            SELECT
                attempts.attempt_id AS attempt_id,
                attempts.run_id AS run_id,
                runs.attempt_count AS attempt_count
            FROM attempts
            JOIN runs ON runs.run_id = attempts.run_id
            WHERE attempts.status = ?
              AND runs.status = ?
              AND runs.current_attempt_id = attempts.attempt_id
              AND attempts.lease_until <= ?
            ORDER BY attempts.lease_until ASC, attempts.attempt_id ASC
            """,
            (ATTEMPT_LEASED, RUN_LEASED, now),
        ).fetchall()

        for row in rows:
            attempt_id = row["attempt_id"]
            run_id = row["run_id"]
            attempt_count = int(row["attempt_count"])
            exhausted = attempt_count >= MAX_ATTEMPTS
            run_status = RUN_FAILED if exhausted else RUN_PENDING

            attempt_rows = db.execute(
                """
                UPDATE attempts
                SET status = ?,
                    finished_at = ?
                WHERE attempt_id = ?
                  AND status = ?
                """,
                (
                    ATTEMPT_EXPIRED,
                    now,
                    attempt_id,
                    ATTEMPT_LEASED,
                ),
            )
            run_rows = db.execute(
                """
                UPDATE runs
                SET status = ?,
                    current_attempt_id = NULL,
                    updated_at = ?
                WHERE run_id = ?
                  AND status = ?
                  AND current_attempt_id = ?
                """,
                (
                    run_status,
                    now,
                    run_id,
                    RUN_LEASED,
                    attempt_id,
                ),
            )

            if attempt_rows.rowcount != 1 or run_rows.rowcount != 1:
                raise RuntimeError(
                    "reclaim_expired_leases lost CAS while holding IMMEDIATE lock"
                )

            reclaimed.append(
                {
                    "run_id": run_id,
                    "attempt_id": attempt_id,
                    "run_status": run_status,
                    "exhausted": exhausted,
                }
            )

    return reclaimed
