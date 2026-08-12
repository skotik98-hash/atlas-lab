from datetime import datetime
import html

from activity_store import list_events
from atlas_status import get_atlas_status


def local_datetime(value):
    try:
        return datetime.fromisoformat(value).astimezone()
    except Exception:
        return None


def humanize_commit(message):
    translations = {
        "Package Atlas background services":
            "Фоновая инфраструктура Atlas подготовлена для автономной работы",

        "Add Atlas Activity Feed":
            "Добавлен журнал активности Atlas",

        "Refine Atlas Activity Feed":
            "Улучшен журнал активности Atlas",

        "Add commit file details to Atlas Activity Feed":
            "Журнал активности теперь показывает изменённые файлы",

        "Add Atlas Owner Report":
            "Добавлен отчёт владельцу Atlas",

        "Add live Atlas system status":
            "Добавлен живой статус системы Atlas",

        "Add persistent Atlas Approval Inbox":
            "Добавлен постоянный центр подтверждений Atlas",

        "Add Atlas state watcher":
            "Добавлен автоматический наблюдатель состояния Atlas",
    }

    return translations.get(message, message)


def build_owner_report():
    status = get_atlas_status()
    events = list_events(150)

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

    decisions = [
        event
        for event in today_events
        if event["event_type"] == "APPROVAL_DECIDED"
    ]

    created_approvals = {}

    for event in today_events:
        if event["event_type"] != "APPROVAL_CREATED":
            continue

        metadata = event.get("metadata") or {}
        approval_id = metadata.get("approval_id")

        if approval_id:
            created_approvals[approval_id] = event

    decided_ids = {
        (event.get("metadata") or {}).get("approval_id")
        for event in decisions
    }

    pending_created = [
        event
        for event in today_events
        if (
            event["event_type"] == "APPROVAL_CREATED"
            and (event.get("metadata") or {}).get("approval_id")
            not in decided_ids
        )
    ]

    approved_today = sum(
        1
        for event in decisions
        if (event.get("metadata") or {}).get("decision")
        == "APPROVED"
    )

    rejected_today = sum(
        1
        for event in decisions
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

    return {
        "generated_at": now,
        "status": status,
        "today_events": len(today_events),
        "commits": commits,
        "decisions": decisions,
        "created_approvals": created_approvals,
        "pending_created": pending_created,
        "approved_today": approved_today,
        "rejected_today": rejected_today,
        "latest_hash": latest_hash,
        "latest_message": latest_message,
        "commit_files": commit_files,
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
        f"Выполнено обновлений: <b>{len(data['commits'])}</b>",
        (
            "Решения владельца: "
            f"✅ {data['approved_today']} · "
            f"❌ {data['rejected_today']}"
        ),
        "",
    ]

    # -------------------------------------------------
    # Выполненная работа
    # -------------------------------------------------

    parts.append("✅ <b>Выполнено</b>")

    if data["commits"]:
        for event in data["commits"][:5]:
            metadata = event.get("metadata") or {}

            message = metadata.get(
                "commit_message",
                event["title"],
            )

            dt = local_datetime(event["created_at"])

            time_text = (
                dt.strftime("%H:%M")
                if dt
                else "—"
            )

            parts.append(
                f"• {time_text} — "
                + html.escape(
                    humanize_commit(str(message))
                )
            )
    else:
        parts.append(
            "• Сегодня новых завершённых обновлений пока нет."
        )

    parts.append("")

    # -------------------------------------------------
    # Решения владельца
    # -------------------------------------------------

    parts.append("👤 <b>Решения владельца</b>")

    if data["decisions"]:
        for decision_event in data["decisions"][:5]:
            metadata = decision_event.get("metadata") or {}

            approval_id = metadata.get("approval_id")
            decision = metadata.get("decision")

            original = data["created_approvals"].get(
                approval_id
            )

            title = (
                original["title"]
                if original
                else "Запрос Atlas"
            )

            if decision == "APPROVED":
                result = "✅ ПОДТВЕРЖДЕНО"
            elif decision == "REJECTED":
                result = "❌ ОТКЛОНЕНО"
            else:
                result = str(decision)

            parts.append(
                "• "
                + html.escape(str(title))
                + " — "
                + result
            )
    else:
        parts.append(
            "• Сегодня решений владельца не требовалось."
        )

    parts.append("")

    # -------------------------------------------------
    # Требует внимания
    # -------------------------------------------------

    parts.append("⚠️ <b>Требует внимания</b>")

    if status["pending"] == 0:
        parts.append(
            "🟢 Активных запросов на решение нет."
        )
    else:
        parts.append(
            f"🟡 Ожидают решения: <b>{status['pending']}</b>"
        )

        for event in data["pending_created"][:3]:
            parts.append(
                "• " + html.escape(event["title"])
            )

    parts.append("")

    # -------------------------------------------------
    # Последний результат
    # -------------------------------------------------

    parts.extend([
        "📦 <b>Последний результат</b>",
        html.escape(
            humanize_commit(
                str(data["latest_message"])
            )
        ),
        (
            "Commit: <code>"
            + html.escape(str(data["latest_hash"]))
            + "</code>"
        ),
    ])

    if data["commit_files"]:
        parts.append("")
        parts.append("📁 <b>Изменено:</b>")

        shown = data["commit_files"][:8]

        for file_name in shown:
            parts.append(
                "• <code>"
                + html.escape(str(file_name))
                + "</code>"
            )

        remaining = (
            len(data["commit_files"])
            - len(shown)
        )

        if remaining > 0:
            parts.append(
                f"• … ещё {remaining}"
            )

    parts.append("")

    # -------------------------------------------------
    # Состояние системы
    # -------------------------------------------------

    parts.extend([
        "💻 <b>Состояние Atlas</b>",
        f"Рабочее дерево: {tree}",
        f"Git: {sync}",
        (
            f"Ahead: <b>{status['ahead']}</b> · "
            f"Behind: <b>{status['behind']}</b>"
        ),
        "",
    ])

    if (
        status["working_tree_clean"]
        and status["ahead"] == 0
        and status["behind"] == 0
        and status["pending"] == 0
    ):
        parts.extend([
            "🟢 <b>Итог</b>",
            "Atlas работает штатно. "
            "Действий владельца сейчас не требуется.",
            "",
        ])
    else:
        parts.extend([
            "🟡 <b>Итог</b>",
            "Atlas работает, но есть состояние, "
            "требующее внимания или завершения.",
            "",
        ])

    parts.extend([
        "━━━━━━━━━━━━━━━━━━",
        (
            "🕐 Сформировано: "
            + data["generated_at"].strftime("%H:%M:%S")
        ),
        "",
        "<i>Atlas Owner Report · v0.2</i>",
    ])

    return "\n".join(parts)


if __name__ == "__main__":
    print(render_owner_report_html())
