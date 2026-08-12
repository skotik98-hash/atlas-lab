import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path


DB_PATH = Path(__file__).with_name("data") / "activity.db"


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def connect():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    db = sqlite3.connect(
        DB_PATH,
        timeout=5,
    )

    db.row_factory = sqlite3.Row

    db.execute("PRAGMA journal_mode=WAL")
    db.execute("PRAGMA busy_timeout=5000")

    return db


def initialize():
    with connect() as db:
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS activity (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_type TEXT NOT NULL,
                source TEXT NOT NULL,
                title TEXT NOT NULL,
                details TEXT,
                metadata_json TEXT,
                created_at TEXT NOT NULL
            )
            """
        )

        db.execute(
            """
            CREATE INDEX IF NOT EXISTS
            idx_activity_created_at
            ON activity(created_at DESC)
            """
        )

        db.commit()


def log_event(
    event_type,
    source,
    title,
    details="",
    metadata=None,
):
    initialize()

    metadata_json = json.dumps(
        metadata or {},
        ensure_ascii=False,
    )

    with connect() as db:
        cursor = db.execute(
            """
            INSERT INTO activity (
                event_type,
                source,
                title,
                details,
                metadata_json,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                event_type,
                source,
                title,
                details,
                metadata_json,
                utc_now(),
            ),
        )

        db.commit()

        return cursor.lastrowid


def list_events(limit=10):
    initialize()

    with connect() as db:
        rows = db.execute(
            """
            SELECT *
            FROM activity
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()

    result = []

    for row in rows:
        item = dict(row)

        try:
            item["metadata"] = json.loads(
                item.pop("metadata_json") or "{}"
            )
        except Exception:
            item["metadata"] = {}

        result.append(item)

    return result


if __name__ == "__main__":
    initialize()

    print("✅ Atlas Activity Store инициализирован")
    print(f"📁 Database: {DB_PATH}")
    print("🔒 Activity database хранится локально")
