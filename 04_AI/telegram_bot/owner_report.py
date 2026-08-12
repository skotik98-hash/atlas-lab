from datetime import datetime
import html

from activity_store import list_events
from atlas_status import get_atlas_status


def local_datetime(value):
    try:
        return datetime.fromisoformat(value).astimezone()
    except Exception:
        return None


def build_owner_report():
    status = get_atlas_status()

    events = list_events(100)

    now = datetime.now().astimezone()
    today = now.date()

    today_events = []

    for event in events:
        dt = local_datetime(event["created_at"])

        if dt and dt.date() == today:
            today_events.append(event)

    commits = [
        event
        for event in today_events
        if event["event_type"] == "GIT_COMMIT"
    ]

    approvals = [
        event
        for event in today_events
        if event["event_type"] == "APPROVAL_DECIDED"
    ]

    approved_today = sum(
        1
        for event in approvals
        if (event.get("metadata") or {}).get("decision")
        == "APPROVED"
    )

    rejected_today = sum(
        1
        for event in approvals
        if (event.get("metadata") or {}).get("decision")
        == "REJECTED"
    )

    latest_commit_event = commits[0] if commits else None

    if latest_commit_event:
        metadata = latest_commit_event.get("metadata") or {}

        latest_hash = metadata.get(
            "commit_hash",
            status["commit_hash"],
        )

        latest_message = metadata.get(
            "commit_message",
            status["commit_message"],
        )

        commit_files = metadata.get("files") or []
    else:
        latest_hash = status["commit_hash"]
        latest_message = status["commit_message"]
        commit_files = status.get("commit_files", [])

    meaningful_types = {
        "GIT_COMMIT",
        "APPROVAL_CREATED",
        "APPROVAL_DECIDED",
        "SYSTEM",
    }

    meaningful = [
        event
        for event in today_events
        if event["event_type"] in meaningful_types
    ][:5]

    return {
        "generated_at": now,
        "status": status,
        "today_events": len(today_events),
        "today_commits": len(commits),
        "approved_today": approved_today,
        "rejected_today": rejected_today,
        "latest_hash": latest_hash,
        "latest_message": latest_message,
        "commit_files": commit_files,
        "meaningful": meaningful,
    }


def render_owner_report_html():
    data = build_owner_report()
    status = data["status"]

    tree = (
        "🟢 ЧИСТО"
        if status["working_tree_clean"]
        else "🟡 ЕСТЬ ИЗМЕНЕНИЯ"
    )

    sync = (
        "🟢 СИНХРОНИЗИРОВАН"
        if status["ahead"] == 0
        and status["behind"] == 0
        else "🟡 ТРЕБУЕТ СИНХРОНИЗАЦИИ"
    )

    parts = [
        "📊 <b>ATLAS · ОТЧЁТ ВЛАДЕЛЬЦУ</b>",
        "",
        "━━━━━━━━━━━━━━━━━━",
        "",
        "🧠 <b>Сегодня</b>",
        f"Событий Atlas: <b>{data['today_events']}</b>",
        f"Новых commit: <b>{data['today_commits']}</b>",
        (
            "Решения владельца: "
            f"✅ {data['approved_today']} · "
            f"❌ {data['rejected_today']}"
        ),
        "",
        "📦 <b>Последний результат</b>",
        f"<code>{html.escape(str(data['latest_hash']))}</code>",
        html.escape(str(data["latest_message"])),
        "",
    ]

    if data["commit_files"]:
        parts.append("📁 <b>Изменено в последнем commit:</b>")

        shown = data["commit_files"][:8]

        for file_name in shown:
            parts.append(
                "• <code>"
                + html.escape(str(file_name))
                + "</code>"
            )

        remaining = len(data["commit_files"]) - len(shown)

        if remaining > 0:
            parts.append(f"• … ещё {remaining}")

        parts.append("")

    parts.extend([
        "⚠️ <b>Требуют решения</b>",
        f"Ожидают Approval: <b>{status['pending']}</b>",
        "",
        "💻 <b>Состояние Atlas</b>",
        f"Рабочее дерево: {tree}",
        f"Git: {sync}",
        (
            f"Ahead: <b>{status['ahead']}</b> · "
            f"Behind: <b>{status['behind']}</b>"
        ),
        "",
    ])

    if data["meaningful"]:
        parts.extend([
            "🗂 <b>Последние важные события</b>",
            "",
        ])

        for event in data["meaningful"]:
            dt = local_datetime(event["created_at"])

            time_text = (
                dt.strftime("%H:%M")
                if dt
                else "—"
            )

            parts.append(
                f"• {time_text} — "
                + html.escape(event["title"])
            )

        parts.append("")

    parts.extend([
        "━━━━━━━━━━━━━━━━━━",
        (
            "🕐 Сформировано: "
            + data["generated_at"].strftime("%H:%M:%S")
        ),
        "",
        "<i>Atlas Owner Report · v0.1</i>",
    ])

    return "\n".join(parts)


if __name__ == "__main__":
    print(render_owner_report_html())
