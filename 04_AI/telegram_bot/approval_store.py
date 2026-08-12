import sqlite3
from datetime import datetime, timezone
from pathlib import Path


DB_PATH = Path(__file__).with_name("data") / "approvals.db"


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def connect():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row

    return connection


def initialize():
    with connect() as db:
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
                decision TEXT
            )
            """
        )

        db.commit()


def create_approval(
    approval_id,
    title,
    action_type,
    details,
):
    initialize()

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
                    created_at
                )
                VALUES (?, ?, ?, ?, 'PENDING', ?)
                """,
                (
                    approval_id,
                    title,
                    action_type,
                    details,
                    utc_now(),
                ),
            )

            db.commit()

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

    return dict(row) if row else None


def decide_approval(
    approval_id,
    decision,
    decided_by,
):
    initialize()

    if decision not in {"APPROVED", "REJECTED"}:
        raise ValueError("Некорректное решение")

    with connect() as db:
        row = db.execute(
            """
            SELECT status
            FROM approvals
            WHERE approval_id = ?
            """,
            (approval_id,),
        ).fetchone()

        if not row:
            return "NOT_FOUND"

        if row["status"] != "PENDING":
            return "ALREADY_DECIDED"

        db.execute(
            """
            UPDATE approvals
            SET
                status = ?,
                decision = ?,
                decided_at = ?,
                decided_by = ?
            WHERE approval_id = ?
              AND status = 'PENDING'
            """,
            (
                decision,
                decision,
                utc_now(),
                decided_by,
                approval_id,
            ),
        )

        db.commit()

    return decision


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

    return [dict(row) for row in rows]


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

    return [dict(row) for row in rows]
