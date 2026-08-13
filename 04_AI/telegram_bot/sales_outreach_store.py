import json
import os
import sqlite3
from datetime import datetime, timezone

from sqlite_lifecycle import managed_connection


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(DATA_DIR, "sales_outreach.db")

VALID_STAGES = {
    "READY_TO_SEND",
    "SENT",
    "WAITING_REPLY",
    "REPLIED",
    "MEETING",
    "PROPOSAL",
    "WON",
    "LOST",
}

# dest -> allowed current stages. Store is authoritative.
STAGE_TRANSITIONS = {
    "SENT": frozenset({"READY_TO_SEND"}),
    "WAITING_REPLY": frozenset({"SENT"}),
    "REPLIED": frozenset({"WAITING_REPLY", "SENT"}),
    "MEETING": frozenset({"REPLIED"}),
    "PROPOSAL": frozenset({"MEETING"}),
    "WON": frozenset({"PROPOSAL"}),
    "LOST": frozenset({"MEETING", "PROPOSAL"}),
}


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def connect():
    os.makedirs(DATA_DIR, exist_ok=True)

    db = sqlite3.connect(DB_PATH, timeout=5)
    db.row_factory = sqlite3.Row
    return managed_connection(db)


def initialize():
    with connect() as db:
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS sales_outreach (
                outreach_id TEXT PRIMARY KEY,
                task_id TEXT NOT NULL,
                company TEXT NOT NULL,
                contact_name TEXT,
                contact_role TEXT,
                channel TEXT NOT NULL,
                stage TEXT NOT NULL,
                solution TEXT,
                message TEXT,
                approval_id TEXT,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                sent_at TEXT,
                replied_at TEXT,
                metadata_json TEXT
            )
            """
        )

        db.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_sales_outreach_task
            ON sales_outreach(task_id)
            """
        )

        db.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_sales_outreach_stage
            ON sales_outreach(stage)
            """
        )

        db.commit()


def create_outreach(
    outreach_id,
    task_id,
    company,
    contact_name,
    contact_role,
    channel,
    stage,
    solution,
    message,
    approval_id=None,
    metadata=None,
):
    initialize()

    if stage not in VALID_STAGES:
        raise ValueError(f"Invalid stage: {stage}")

    now = utc_now()

    with connect() as db:
        try:
            db.execute(
                """
                INSERT INTO sales_outreach (
                    outreach_id,
                    task_id,
                    company,
                    contact_name,
                    contact_role,
                    channel,
                    stage,
                    solution,
                    message,
                    approval_id,
                    created_at,
                    updated_at,
                    metadata_json
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    outreach_id,
                    task_id,
                    company,
                    contact_name,
                    contact_role,
                    channel,
                    stage,
                    solution,
                    message,
                    approval_id,
                    now,
                    now,
                    json.dumps(
                        metadata or {},
                        ensure_ascii=False,
                    ),
                ),
            )

            db.commit()
            return True

        except sqlite3.IntegrityError:
            return False


def get_outreach(outreach_id):
    initialize()

    with connect() as db:
        row = db.execute(
            """
            SELECT *
            FROM sales_outreach
            WHERE outreach_id = ?
            """,
            (outreach_id,),
        ).fetchone()

    if not row:
        return None

    item = dict(row)

    try:
        item["metadata"] = json.loads(
            item.pop("metadata_json") or "{}"
        )
    except Exception:
        item["metadata"] = {}

    return item


def list_outreach(limit=50):
    initialize()

    with connect() as db:
        rows = db.execute(
            """
            SELECT *
            FROM sales_outreach
            ORDER BY created_at DESC
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


def count_stages():
    initialize()

    counts = {
        stage: 0
        for stage in VALID_STAGES
    }

    with connect() as db:
        rows = db.execute(
            """
            SELECT stage, COUNT(*) AS total
            FROM sales_outreach
            GROUP BY stage
            """
        ).fetchall()

    for row in rows:
        counts[row["stage"]] = row["total"]

    return counts


def transition_stage(outreach_id, stage, expected_stage=None):
    """Atomically move outreach to stage from an allowed source stage.

    Returns {"ok", "reason"}.
    """
    initialize()

    if stage not in VALID_STAGES:
        raise ValueError(f"Invalid stage: {stage}")

    allowed = STAGE_TRANSITIONS.get(stage)

    if not allowed:
        return {
            "ok": False,
            "reason": "INVALID_TRANSITION",
        }

    if expected_stage is not None:
        if expected_stage not in allowed:
            return {
                "ok": False,
                "reason": "INVALID_TRANSITION",
            }

        sources = (expected_stage,)
    else:
        sources = tuple(sorted(allowed))

    now = utc_now()
    placeholders = ",".join(["?"] * len(sources))
    extra_sql = ""
    params = [stage, now]

    if stage == "SENT":
        extra_sql += ", sent_at = COALESCE(sent_at, ?)"
        params.append(now)

    if stage == "REPLIED":
        extra_sql += ", replied_at = COALESCE(replied_at, ?)"
        params.append(now)

    params.append(outreach_id)
    params.extend(sources)

    with connect() as db:
        result = db.execute(
            f"""
            UPDATE sales_outreach
            SET stage = ?,
                updated_at = ?
                {extra_sql}
            WHERE outreach_id = ?
              AND stage IN ({placeholders})
            """,
            params,
        )

        db.commit()
        changed = result.rowcount == 1

    if changed:
        return {
            "ok": True,
            "reason": "OK",
        }

    item = get_outreach(outreach_id)

    return {
        "ok": False,
        "reason": (
            "NOT_FOUND"
            if item is None
            else "INVALID_TRANSITION"
        ),
    }


def update_stage(outreach_id, stage, expected_stage=None):
    return transition_stage(
        outreach_id,
        stage,
        expected_stage=expected_stage,
    )["ok"]


def record_inbound_reply(outreach_id, reply_text):
    """
    Save a real inbound company reply and move the outreach
    to REPLIED.

    The full reply is stored locally inside metadata_json.
    """

    initialize()

    reply_text = str(reply_text or "").strip()

    if not reply_text:
        return False

    item = get_outreach(outreach_id)

    if not item:
        return False

    now = utc_now()

    metadata = item.get("metadata") or {}

    if not isinstance(metadata, dict):
        metadata = {}

    history = metadata.get("reply_history") or []

    if not isinstance(history, list):
        history = []

    history.append(
        {
            "received_at": now,
            "text": reply_text,
        }
    )

    # Keep a reasonable local history.
    metadata["reply_history"] = history[-20:]
    metadata["last_reply_text"] = reply_text
    metadata["last_reply_at"] = now

    sources = tuple(sorted(STAGE_TRANSITIONS["REPLIED"]))
    placeholders = ",".join(["?"] * len(sources))

    with connect() as db:
        result = db.execute(
            f"""
            UPDATE sales_outreach
            SET
                stage = ?,
                updated_at = ?,
                replied_at = COALESCE(replied_at, ?),
                metadata_json = ?
            WHERE outreach_id = ?
              AND stage IN ({placeholders})
            """,
            (
                "REPLIED",
                now,
                now,
                json.dumps(
                    metadata,
                    ensure_ascii=False,
                ),
                outreach_id,
                *sources,
            ),
        )

        db.commit()

        return result.rowcount == 1


if __name__ == "__main__":
    initialize()
    print("✅ Atlas Sales Outreach Store инициализирован")
    print(f"🗄 Database: {DB_PATH}")
    print("🔐 Runtime database хранится локально")
