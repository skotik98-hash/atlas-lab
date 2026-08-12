import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "data" / "tasks.db"

STATUSES = {
    "NEW",
    "IN_PROGRESS",
    "WAITING_APPROVAL",
    "BLOCKED",
    "DONE",
    "CANCELLED",
}

PRIORITIES = {
    "LOW",
    "NORMAL",
    "HIGH",
    "CRITICAL",
}


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def connect():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row

    return db


def initialize():
    with connect() as db:
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_id TEXT UNIQUE,
                title TEXT NOT NULL,
                description TEXT NOT NULL DEFAULT '',
                status TEXT NOT NULL DEFAULT 'NEW',
                priority TEXT NOT NULL DEFAULT 'NORMAL',
                source TEXT NOT NULL DEFAULT 'OWNER',
                result TEXT,
                approval_id TEXT,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                completed_at TEXT,
                metadata_json TEXT NOT NULL DEFAULT '{}'
            )
            """
        )

        db.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_tasks_status
            ON tasks(status)
            """
        )

        db.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_tasks_created_at
            ON tasks(created_at DESC)
            """
        )

        db.commit()


def _decode(row):
    if row is None:
        return None

    item = dict(row)

    try:
        item["metadata"] = json.loads(
            item.pop("metadata_json") or "{}"
        )
    except Exception:
        item["metadata"] = {}

    return item


def create_task(
    title,
    description="",
    priority="NORMAL",
    source="OWNER",
    metadata=None,
):
    initialize()

    title = str(title).strip()
    description = str(description).strip()
    priority = str(priority).upper().strip()
    source = str(source).upper().strip()

    if not title:
        raise ValueError("Название задачи не может быть пустым")

    if priority not in PRIORITIES:
        raise ValueError(
            f"Некорректный приоритет: {priority}"
        )

    now = utc_now()

    with connect() as db:
        cursor = db.execute(
            """
            INSERT INTO tasks (
                title,
                description,
                status,
                priority,
                source,
                created_at,
                updated_at,
                metadata_json
            )
            VALUES (?, ?, 'NEW', ?, ?, ?, ?, ?)
            """,
            (
                title,
                description,
                priority,
                source,
                now,
                now,
                json.dumps(
                    metadata or {},
                    ensure_ascii=False,
                ),
            ),
        )

        task_id = f"TASK-{cursor.lastrowid:04d}"

        db.execute(
            """
            UPDATE tasks
            SET task_id = ?
            WHERE id = ?
            """,
            (
                task_id,
                cursor.lastrowid,
            ),
        )

        db.commit()

    return get_task(task_id)


def get_task(task_id):
    initialize()

    with connect() as db:
        row = db.execute(
            """
            SELECT *
            FROM tasks
            WHERE task_id = ?
            """,
            (task_id,),
        ).fetchone()

    return _decode(row)


def list_tasks(limit=20, status=None):
    initialize()

    limit = max(1, min(int(limit), 100))

    with connect() as db:
        if status:
            status = status.upper().strip()

            if status not in STATUSES:
                raise ValueError(
                    f"Некорректный статус: {status}"
                )

            rows = db.execute(
                """
                SELECT *
                FROM tasks
                WHERE status = ?
                ORDER BY id DESC
                LIMIT ?
                """,
                (
                    status,
                    limit,
                ),
            ).fetchall()

        else:
            rows = db.execute(
                """
                SELECT *
                FROM tasks
                ORDER BY id DESC
                LIMIT ?
                """,
                (limit,),
            ).fetchall()

    return [_decode(row) for row in rows]


def update_task_status(
    task_id,
    status,
    result=None,
    approval_id=None,
):
    initialize()

    status = str(status).upper().strip()

    if status not in STATUSES:
        raise ValueError(
            f"Некорректный статус: {status}"
        )

    now = utc_now()

    completed_at = (
        now
        if status in {"DONE", "CANCELLED"}
        else None
    )

    with connect() as db:
        cursor = db.execute(
            """
            UPDATE tasks
            SET
                status = ?,
                result = COALESCE(?, result),
                approval_id = COALESCE(?, approval_id),
                updated_at = ?,
                completed_at = ?
            WHERE task_id = ?
            """,
            (
                status,
                result,
                approval_id,
                now,
                completed_at,
                task_id,
            ),
        )

        db.commit()

        if cursor.rowcount == 0:
            return None

    return get_task(task_id)


def count_tasks():
    initialize()

    counts = {
        status: 0
        for status in STATUSES
    }

    with connect() as db:
        rows = db.execute(
            """
            SELECT status, COUNT(*) AS total
            FROM tasks
            GROUP BY status
            """
        ).fetchall()

    for row in rows:
        counts[row["status"]] = row["total"]

    return counts


if __name__ == "__main__":
    initialize()

    print("✅ Atlas Task Store инициализирован")
    print(f"🗄 Database: {DB_PATH}")
    print("🔐 Runtime database хранится локально")
