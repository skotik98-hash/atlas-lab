import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from activity_store import log_event
from sqlite_lifecycle import managed_connection
from task_store import apply_task_approval_decision, get_task


DB_PATH = Path(__file__).with_name("data") / "approvals.db"

PROP_NONE = "NONE"
PROP_PENDING = "PENDING"
PROP_APPLIED = "APPLIED"
PROP_INCOMPATIBLE = "INCOMPATIBLE"

PROPAGATION_STATUSES = {
    PROP_NONE,
    PROP_PENDING,
    PROP_APPLIED,
    PROP_INCOMPATIBLE,
}

# Test-only hooks. Production code never sets these.
fail_after_decision = False
fail_after_task_before_mark = False


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def connect():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DB_PATH, timeout=5)
    connection.row_factory = sqlite3.Row

    return managed_connection(connection)


def _column_names(db):
    rows = db.execute("PRAGMA table_info(approvals)").fetchall()
    return {row[1] for row in rows}


def _add_column_if_missing(db, name, ddl):
    if name in _column_names(db):
        return

    db.execute(ddl)


def _ensure_schema(db):
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS approvals (
            approval_id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            action_type TEXT NOT NULL,
            details TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'PENDING',
            created_at TEXT NOT NULL,
            decided_at TEXT,
            decided_by INTEGER,
            decision TEXT,
            task_id TEXT,
            propagation_status TEXT NOT NULL DEFAULT 'NONE',
            propagation_error TEXT
        )
        """
    )

    _add_column_if_missing(
        db,
        "task_id",
        "ALTER TABLE approvals ADD COLUMN task_id TEXT",
    )
    _add_column_if_missing(
        db,
        "propagation_status",
        """
        ALTER TABLE approvals
        ADD COLUMN propagation_status TEXT NOT NULL DEFAULT 'NONE'
        """,
    )
    _add_column_if_missing(
        db,
        "propagation_error",
        "ALTER TABLE approvals ADD COLUMN propagation_error TEXT",
    )

    db.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_approvals_task_id
        ON approvals(task_id)
        """
    )

    db.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_approvals_propagation
        ON approvals(propagation_status)
        """
    )


def initialize():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DB_PATH, timeout=30)
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


def _normalize_task_id(task_id):
    if task_id is None:
        return None

    task_id = str(task_id).strip()
    return task_id or None


def _linked_task_id(approval):
    if not approval:
        return None

    return _normalize_task_id(approval.get("task_id"))


def _decode(row):
    if row is None:
        return None

    item = dict(row)
    item["task_id"] = _normalize_task_id(item.get("task_id"))
    item["propagation_status"] = (
        item.get("propagation_status") or PROP_NONE
    )
    return item


def create_approval(
    approval_id,
    title,
    action_type,
    details,
    task_id=None,
):
    initialize()

    task_id = _normalize_task_id(task_id)

    try:
        with connect() as db:
            db.execute(
                """
                INSERT INTO approvals (
                    approval_id,
                    title,
                    action_type,
                    details,
                    status,
                    created_at,
                    task_id,
                    propagation_status
                )
                VALUES (?, ?, ?, ?, 'PENDING', ?, ?, 'NONE')
                """,
                (
                    approval_id,
                    title,
                    action_type,
                    details,
                    utc_now(),
                    task_id,
                ),
            )

            db.commit()

        log_event(
            event_type="APPROVAL_CREATED",
            source="Approval Engine",
            title=title,
            details=details,
            metadata={
                "approval_id": approval_id,
                "action_type": action_type,
                "status": "PENDING",
                "task_id": task_id,
            },
        )

        return True

    except sqlite3.IntegrityError:
        return False


def get_approval(approval_id):
    initialize()

    with connect() as db:
        row = db.execute(
            """
            SELECT *
            FROM approvals
            WHERE approval_id = ?
            """,
            (approval_id,),
        ).fetchone()

    return _decode(row)


def _expected_task_status(decision):
    if decision == "APPROVED":
        return "IN_PROGRESS"
    if decision == "REJECTED":
        return "BLOCKED"
    raise ValueError("Некорректное решение")


def _set_propagation(approval_id, status, error=None):
    if status not in PROPAGATION_STATUSES:
        raise ValueError("Некорректный статус распространения")

    with connect() as db:
        cursor = db.execute(
            """
            UPDATE approvals
            SET
                propagation_status = ?,
                propagation_error = ?
            WHERE approval_id = ?
              AND propagation_status = 'PENDING'
            """,
            (
                status,
                error,
                approval_id,
            ),
        )
        db.commit()
        return cursor.rowcount == 1


def _outcome(
    reason,
    approval,
    task=None,
    recovered=False,
):
    approval = _decode(approval) if approval is not None and not isinstance(approval, dict) else approval
    decision = None
    propagation = PROP_NONE

    if approval:
        decision = approval.get("decision")
        propagation = approval.get("propagation_status") or PROP_NONE

    ok = reason in {"APPROVED", "REJECTED"}
    if reason == "ALREADY_DECIDED" and propagation in {
        PROP_NONE,
        PROP_APPLIED,
        PROP_INCOMPATIBLE,
    }:
        ok = False

    if reason in {"APPROVED", "REJECTED"} and propagation == PROP_PENDING:
        ok = False

    return {
        "ok": ok,
        "reason": reason,
        "decision": decision if reason == "ALREADY_DECIDED" else (
            reason if reason in {"APPROVED", "REJECTED"} else decision
        ),
        "propagation": propagation,
        "approval": approval,
        "task": task,
        "recovered": recovered,
    }


def _propagate(approval):
    approval_id = approval["approval_id"]
    task_id = _linked_task_id(approval)
    decision = approval.get("decision")

    if not task_id or decision not in {"APPROVED", "REJECTED"}:
        current = get_approval(approval_id)
        return _outcome(
            current["decision"] if current and current["status"] != "PENDING" else "NOT_FOUND",
            current,
        )

    dest = _expected_task_status(decision)
    task_result = apply_task_approval_decision(
        task_id,
        decision,
        approval_id=approval_id,
    )
    task = task_result.get("task")

    if fail_after_task_before_mark:
        raise RuntimeError(
            "R3 injected failure after task write"
        )

    applied = False
    incompatible_error = None

    if task_result.get("ok"):
        applied = True
    elif task is not None and task.get("status") == dest:
        applied = True
    elif task is None:
        incompatible_error = "TASK_NOT_FOUND"
    else:
        incompatible_error = task_result.get("reason") or "INVALID_TRANSITION"

    if applied:
        _set_propagation(approval_id, PROP_APPLIED, None)
        log_event(
            event_type="APPROVAL_TASK_APPLIED",
            source="Approval Engine",
            title="Approval propagated to task",
            details=(
                f"{approval_id} → {task_id} "
                f"{decision} / {dest}"
            ),
            metadata={
                "approval_id": approval_id,
                "task_id": task_id,
                "decision": decision,
                "task_status": dest,
            },
        )
        current = get_approval(approval_id)
        return _outcome(
            current["decision"],
            current,
            task=get_task(task_id),
        )

    _set_propagation(
        approval_id,
        PROP_INCOMPATIBLE,
        incompatible_error,
    )
    log_event(
        event_type="APPROVAL_TASK_INCOMPATIBLE",
        source="Approval Engine",
        title="Approval could not change task",
        details=(
            f"{approval_id} → {task_id} "
            f"{decision}: {incompatible_error}"
        ),
        metadata={
            "approval_id": approval_id,
            "task_id": task_id,
            "decision": decision,
            "error": incompatible_error,
            "task_status": None if task is None else task.get("status"),
        },
    )
    current = get_approval(approval_id)
    return _outcome(
        current["decision"],
        current,
        task=get_task(task_id) if task_id else None,
    )


def _finish_existing(approval):
    if (
        _linked_task_id(approval)
        and approval.get("propagation_status") == PROP_PENDING
        and approval.get("decision") in {"APPROVED", "REJECTED"}
    ):
        propagated = _propagate(approval)
        propagated["reason"] = "ALREADY_DECIDED"
        propagated["ok"] = False
        propagated["recovered"] = (
            propagated.get("propagation") != PROP_PENDING
        )
        propagated["decision"] = approval.get("decision")
        return propagated

    current = get_approval(approval["approval_id"])
    task = None
    task_id = _linked_task_id(current)
    if task_id:
        task = get_task(task_id)

    return _outcome(
        "ALREADY_DECIDED",
        current,
        task=task,
    )


def apply_approval_decision(
    approval_id,
    decision,
    decided_by,
):
    """CAS-decide an approval and propagate to a linked task.

    Unlinked approvals complete when the decision row commits.
    Linked approvals are not treated as fully successful until
    propagation is APPLIED or INCOMPATIBLE (detectable, no
    resurrection). Duplicate callbacks retry PENDING propagation.
    """
    initialize()

    if decision not in {"APPROVED", "REJECTED"}:
        raise ValueError("Некорректное решение")

    approval = get_approval(approval_id)

    if not approval:
        return _outcome("NOT_FOUND", None)

    if approval["status"] != "PENDING":
        return _finish_existing(approval)

    linked = _linked_task_id(approval) is not None
    propagation = PROP_PENDING if linked else PROP_NONE
    now = utc_now()

    with connect() as db:
        cursor = db.execute(
            """
            UPDATE approvals
            SET
                status = ?,
                decision = ?,
                decided_at = ?,
                decided_by = ?,
                propagation_status = ?,
                propagation_error = NULL
            WHERE approval_id = ?
              AND status = 'PENDING'
            """,
            (
                decision,
                decision,
                now,
                decided_by,
                propagation,
                approval_id,
            ),
        )
        changed = cursor.rowcount == 1
        db.commit()

    if not changed:
        current = get_approval(approval_id)
        if not current:
            return _outcome("NOT_FOUND", None)
        return _finish_existing(current)

    log_event(
        event_type="APPROVAL_DECIDED",
        source="Approval Engine",
        title=f"Approval {decision}",
        details=f"Решение владельца по {approval_id}: {decision}",
        metadata={
            "approval_id": approval_id,
            "decision": decision,
            "decided_by": decided_by,
            "task_id": _linked_task_id(approval),
            "propagation_status": propagation,
        },
    )

    if fail_after_decision:
        raise RuntimeError(
            "R3 injected failure after approval decision"
        )

    current = get_approval(approval_id)

    if not linked:
        return _outcome(decision, current)

    propagated = _propagate(current)
    if propagated["reason"] in {"APPROVED", "REJECTED"}:
        return propagated

    # _propagate returns the stored decision after reload.
    propagated["reason"] = decision
    return propagated


def decide_approval(
    approval_id,
    decision,
    decided_by,
):
    outcome = apply_approval_decision(
        approval_id,
        decision,
        decided_by,
    )

    if outcome["reason"] in {"NOT_FOUND", "ALREADY_DECIDED"}:
        return outcome["reason"]

    return outcome["decision"]


def recover_pending_propagations(limit=50):
    """Retry decided approvals whose task write never finished."""
    initialize()

    limit = max(1, min(int(limit), 100))

    with connect() as db:
        rows = db.execute(
            """
            SELECT *
            FROM approvals
            WHERE status IN ('APPROVED', 'REJECTED')
              AND propagation_status = 'PENDING'
              AND task_id IS NOT NULL
              AND TRIM(task_id) != ''
            ORDER BY decided_at ASC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()

    results = []
    for row in rows:
        approval = _decode(row)
        outcome = _propagate(approval)
        outcome["recovered"] = True
        results.append(outcome)

    return results


if __name__ == "__main__":
    initialize()

    print("✅ Approval Store инициализирован")
    print(f"📁 Database: {DB_PATH}")
    print("🔒 Runtime database предназначена только для локального хранения")


def list_approvals(limit=10):
    initialize()

    with connect() as db:
        rows = db.execute(
            """
            SELECT *
            FROM approvals
            ORDER BY created_at DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()

    return [_decode(row) for row in rows]


def count_approvals():
    initialize()

    counts = {
        "PENDING": 0,
        "APPROVED": 0,
        "REJECTED": 0,
    }

    with connect() as db:
        rows = db.execute(
            """
            SELECT status, COUNT(*) AS total
            FROM approvals
            GROUP BY status
            """
        ).fetchall()

    for row in rows:
        counts[row["status"]] = row["total"]

    return counts


def list_pending(limit=10):
    initialize()

    with connect() as db:
        rows = db.execute(
            """
            SELECT *
            FROM approvals
            WHERE status = 'PENDING'
            ORDER BY created_at ASC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()

    return [_decode(row) for row in rows]
