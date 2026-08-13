import os
import plistlib
import subprocess
import html
import logging
from datetime import datetime

from telegram import Update, BotCommand, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from atlas_status import get_atlas_status
from activity_store import list_events, log_event
from owner_report import render_owner_report_html
from sales_outreach_store import list_outreach, count_stages, get_outreach, update_stage, record_inbound_reply

from approval_store import (
    get_approval,
    apply_approval_decision,
    recover_pending_propagations,
    list_approvals,
    count_approvals,
    list_pending,
)

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
from task_store import (
    list_tasks,
    count_tasks,
    get_task,
    update_task_status,
    create_task,
)
from telegram.ext import MessageHandler, filters
import datetime as dt

# Task statuses that may be owner-started via /tasks.
# First version: only NEW -> IN_PROGRESS.
TASK_STARTABLE_STATUSES = {
    "NEW",
}

# Task statuses that may be owner-completed via /tasks.
# First version: only IN_PROGRESS -> DONE.
TASK_COMPLETABLE_STATUSES = {
    "IN_PROGRESS",
}

# ─────────────────────────────────────────────
# ЛОГИ
# ─────────────────────────────────────────────

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
)

logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)

logger = logging.getLogger("atlas.telegram")


# ─────────────────────────────────────────────
# ENV
# ─────────────────────────────────────────────

def load_env_file():
    env_path = os.path.join(os.path.dirname(__file__), ".env")

    if not os.path.exists(env_path):
        raise RuntimeError(".env не найден")

    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not line or line.startswith("#") or "=" not in line:
                continue

            key, value = line.split("=", 1)

            # .env всегда имеет приоритет
            os.environ[key.strip()] = value.strip()


load_env_file()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()

OWNER_IDS = {
    int(x.strip())
    for x in os.getenv("TELEGRAM_OWNER_IDS", "").split(",")
    if x.strip().isdigit()
}

if not BOT_TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN отсутствует")

if not OWNER_IDS:
    raise RuntimeError("TELEGRAM_OWNER_IDS отсутствует")


# ─────────────────────────────────────────────
# БЕЗОПАСНОСТЬ
# ─────────────────────────────────────────────

def authorized(update: Update) -> bool:
    user = update.effective_user
    return bool(user and user.id in OWNER_IDS)


async def deny_access(update: Update):
    if update.effective_message:
        await update.effective_message.reply_text(
            "🔒 <b>ATLAS CONTROL</b>\n\n"
            "⛔ Доступ к системе запрещён.\n\n"
            "<i>Atlas Security</i>",
            parse_mode=ParseMode.HTML,
        )


# ─────────────────────────────────────────────
# /START
# ─────────────────────────────────────────────

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not authorized(update):
        await deny_access(update)
        return

    name = html.escape(update.effective_user.first_name or "Владелец")

    text = (
        "🟢 <b>ATLAS LAB · ЦЕНТР УПРАВЛЕНИЯ</b>\n\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "👤 <b>Владелец</b>\n"
        f"{name}\n\n"
        "🧠 <b>Ядро Atlas</b>\n"
        "Статус: 🟢 ГОТОВО\n"
        "Режим: 👤 КОНТРОЛЬ ВЛАДЕЛЬЦА\n\n"
        "🤖 <b>Telegram Gateway</b>\n"
        "Статус: 🟢 В СЕТИ\n\n"
        "🔐 <b>Безопасность</b>\n"
        "Доступ: ✅ АВТОРИЗОВАН\n\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "📊 /status — состояние Atlas\n"
        "🧠 /activity — журнал активности\n"
        "⚠️ /approvals — журнал решений\n"
        "🟡 /pending — ожидают решения\n"
        "❓ /help — команды управления\n\n"
        "<i>Atlas Control · v0.2</i>"
    )

    await update.effective_message.reply_text(
        text,
        parse_mode=ParseMode.HTML,
    )


# ─────────────────────────────────────────────
# /STATUS
# ─────────────────────────────────────────────


def get_owner_report_scheduler_status():
    plist_path = os.path.expanduser(
        "~/Library/LaunchAgents/com.atlaslab.ownerreport.plist"
    )

    if not os.path.exists(plist_path):
        return "🔴 OFF", "—"

    hour = 22
    minute = 0

    try:
        with open(plist_path, "rb") as f:
            config = plistlib.load(f)

        schedule = config.get(
            "StartCalendarInterval",
            {},
        )

        hour = int(schedule.get("Hour", hour))
        minute = int(schedule.get("Minute", minute))

    except Exception:
        pass

    label = (
        f"gui/{os.getuid()}/"
        "com.atlaslab.ownerreport"
    )

    try:
        result = subprocess.run(
            ["launchctl", "print", label],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )

        loaded = result.returncode == 0

    except Exception:
        loaded = False

    schedule_text = (
        f"ежедневно · {hour:02d}:{minute:02d}"
    )

    if loaded:
        return "🟢 ACTIVE", schedule_text

    return "🟡 INSTALLED", schedule_text


async def status(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if not authorized(update):
        await deny_access(update)
        return

    data = get_atlas_status()

    branch = html.escape(data["branch"])
    commit_hash = html.escape(data["commit_hash"])
    commit_message = html.escape(data["commit_message"])

    if data["working_tree_clean"]:
        tree_status = "🟢 ЧИСТО"
    else:
        tree_status = "🟡 ЕСТЬ ИЗМЕНЕНИЯ"

    if data["ahead"] == 0 and data["behind"] == 0:
        sync_status = "🟢 СИНХРОНИЗИРОВАНО"
    else:
        sync_status = "🟡 ТРЕБУЕТ СИНХРОНИЗАЦИИ"

    now = datetime.now().strftime("%H:%M:%S")

    report_status, report_schedule = get_owner_report_scheduler_status()

    text = (
        "🟢 <b>ATLAS LAB · СОСТОЯНИЕ СИСТЕМЫ</b>\n\n"
        "━━━━━━━━━━━━━━━━━━\n\n"

        "🧠 <b>Atlas Core</b>\n"
        "Статус: 🟢 РАБОТАЕТ\n"
        "Режим: 👤 КОНТРОЛЬ ВЛАДЕЛЬЦА\n\n"

        "📦 <b>Репозиторий</b>\n"
        f"Ветка: <code>{branch}</code>\n"
        f"Рабочее дерево: {tree_status}\n"
        f"Git Sync: {sync_status}\n"
        f"Ahead: <b>{data['ahead']}</b> · "
        f"Behind: <b>{data['behind']}</b>\n\n"

        "🧾 <b>Последний commit</b>\n"
        f"<code>{commit_hash}</code>\n"
        f"{commit_message}\n\n"

        "⚠️ <b>Approval Inbox</b>\n"
        f"🟡 Ожидают решения: <b>{data['pending']}</b>\n"
        f"🟢 Подтверждено: <b>{data['approved']}</b>\n"
        f"🔴 Отклонено: <b>{data['rejected']}</b>\n\n"

        "🤖 <b>Telegram Control</b>\n"
        "Gateway: 🟢 ONLINE\n"
        "Notification Engine: 🟢 READY\n"
        "Approval Engine: 🟢 READY\n"
        "Owner Authentication: 🔐 ACTIVE\n\n"

        "📊 <b>Автоматические отчёты</b>\n"
        f"Daily Owner Report: {report_status}\n"
        f"Расписание: {report_schedule}\n\n"

        "━━━━━━━━━━━━━━━━━━\n"
        f"🕐 Обновлено: {now}\n\n"

        "<i>Atlas Control · Live Status v0.7</i>"
    )

    await update.effective_message.reply_text(
        text,
        parse_mode=ParseMode.HTML,
    )


# ─────────────────────────────────────────────
# /HELP
# ─────────────────────────────────────────────

async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if not authorized(update):
        await deny_access(update)
        return

    text = (
        "🤖 <b>ATLAS · КОМАНДНЫЙ ЦЕНТР</b>\n\n"
        "━━━━━━━━━━━━━━━━━━\n\n"

        "🏠 <b>Управление</b>\n\n"

        "🏠 /start\n"
        "Открыть главный центр управления Atlas.\n\n"

        "📊 /status\n"
        "Показать живое состояние Atlas Lab: "
        "Git, синхронизацию, последний commit, "
        "Approval Inbox и Telegram Control.\n\n"

        "🧠 /activity\n"
        "Открыть журнал последних действий и событий Atlas.\n\n"

        "📊 /report\n"
        "Сформировать сводный отчёт владельцу: результаты, "
        "commit, решения и текущее состояние Atlas.\n\n"

        "━━━━━━━━━━━━━━━━━━\n\n"

        "🎯 <b>Работа Atlas</b>\n\n"
        "🎯 /tasks\n"
        "Показать текущие задачи Atlas, их статусы, "
        "приоритеты и очередь выполнения.\n\n"

        "➕ /newtask\n"
        "Создать новую задачу Atlas.\n"
        "Формат: /newtask название | описание | приоритет\n\n"
        "──────────────────\n\n"
        "⚠️ <b>Решения владельца</b>\n\n"

        "⚠️ /approvals\n"
        "История запросов и принятых решений.\n\n"

        "🟡 /pending\n"
        "Показать только запросы, которые прямо сейчас "
        "ожидают решения владельца.\n\n"

        "━━━━━━━━━━━━━━━━━━\n\n"

        "❓ <b>Помощь</b>\n\n"

        "❓ /help\n"
        "Показать этот список команд.\n\n"

        "━━━━━━━━━━━━━━━━━━\n\n"

        "🟢 <b>Активные системы</b>\n\n"
        "🔔 Система уведомлений · АКТИВНА\n"
        "⚠️ Approval Inbox · АКТИВЕН\n"
        "🧠 Activity Feed · АКТИВЕН\n"
        "👁 Atlas Watcher · АКТИВЕН\n"
        "📊 Live Status · АКТИВЕН\n"
        "🔐 Авторизация владельца · АКТИВНА\n\n"

        "━━━━━━━━━━━━━━━━━━\n\n"

        "💡 <i>Все основные команды также доступны "
        "через кнопку «Меню» в Telegram.</i>\n\n"

        "<i>Atlas Control · Command Center v0.5</i>"
    )

    await update.effective_message.reply_text(
        text,
        parse_mode=ParseMode.HTML,
    )



# ─────────────────────────────────────────────
# /REPORT
# ─────────────────────────────────────────────

async def report_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if not authorized(update):
        await deny_access(update)
        return

    text = render_owner_report_html()

    await update.effective_message.reply_text(
        text,
        parse_mode=ParseMode.HTML,
    )


# ─────────────────────────────────────────────
# /ACTIVITY
# ─────────────────────────────────────────────

async def activity_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if not authorized(update):
        await deny_access(update)
        return

    # Берём больше записей, потому что часть технических
    # событий скрывается из пользовательской ленты.
    raw_events = list_events(30)

    # Эти события остаются в Activity Store для аудита,
    # но не дублируются в обычном Telegram-интерфейсе.
    hidden_types = {
        "APPROVAL_PENDING",
        "APPROVAL_CLEARED",
    }

    events = list(reversed([
        event
        for event in raw_events
        if event["event_type"] not in hidden_types
    ][:10]))

    event_labels = {
        "SYSTEM": ("⚙️", "СИСТЕМА"),
        "GIT_COMMIT": ("🧾", "НОВЫЙ COMMIT"),
        "GIT_DIRTY": ("🟡", "ЛОКАЛЬНЫЕ ИЗМЕНЕНИЯ"),
        "GIT_CLEAN": ("🟢", "GIT ЧИСТ"),
        "GIT_SYNC_REQUIRED": (
            "🟠",
            "НУЖНА СИНХРОНИЗАЦИЯ",
        ),
        "GIT_SYNC_RESTORED": (
            "🟢",
            "СИНХРОНИЗАЦИЯ ВОССТАНОВЛЕНА",
        ),
        "APPROVAL_CREATED": (
            "⚠️",
            "СОЗДАН ЗАПРОС",
        ),
        "APPROVAL_DECIDED": (
            "✅",
            "РЕШЕНИЕ ПРИНЯТО",
        ),
    }

    source_labels = {
        "Approval Engine": "Система решений Atlas",
        "Atlas Watcher": "Наблюдатель Atlas",
        "Atlas Infrastructure": "Инфраструктура Atlas",
        "Atlas Control": "Центр управления Atlas",
    }

    parts = [
        "🧠 <b>ATLAS · ЖУРНАЛ АКТИВНОСТИ</b>",
        "",
        "━━━━━━━━━━━━━━━━━━",
        "",
    ]

    if not events:
        parts.extend([
            "📭 Событий пока нет.",
            "",
        ])
    else:
        for event in events:
            event_type = event["event_type"]
            metadata = event.get("metadata") or {}

            emoji, label = event_labels.get(
                event_type,
                ("🔵", event_type),
            )

            # Для решения владельца показываем результат
            # человеческим языком.
            if event_type == "APPROVAL_DECIDED":
                decision = metadata.get("decision")

                if decision == "APPROVED":
                    emoji = "✅"
                    label = "ЗАПРОС ПОДТВЕРЖДЁН"
                    title = "Владелец подтвердил действие"
                elif decision == "REJECTED":
                    emoji = "❌"
                    label = "ЗАПРОС ОТКЛОНЁН"
                    title = "Владелец отклонил действие"
                else:
                    title = event["title"]
            else:
                title = event["title"]

            try:
                dt = datetime.fromisoformat(
                    event["created_at"]
                ).astimezone()

                time_text = dt.strftime(
                    "%d.%m · %H:%M"
                )
            except Exception:
                time_text = "—"

            source = source_labels.get(
                event["source"],
                event["source"],
            )

            parts.extend([
                f"{emoji} <b>{label}</b> · {time_text}",
                html.escape(title),
                f"<i>{html.escape(source)}</i>",
            ])

            # Для Git commit показываем hash + сообщение.
            if event_type == "GIT_COMMIT":
                commit_hash = metadata.get(
                    "commit_hash"
                )
                commit_message = metadata.get(
                    "commit_message"
                )
                commit_files = metadata.get("files") or []

                if commit_hash:
                    parts.append(
                        f"🔖 <code>{html.escape(str(commit_hash))}</code>"
                    )

                if commit_message:
                    parts.append(
                        html.escape(str(commit_message))
                    )

                if commit_files:
                    parts.append("")
                    parts.append("📁 <b>Изменено:</b>")

                    shown_files = commit_files[:8]

                    for file_name in shown_files:
                        parts.append(
                            "• <code>"
                            + html.escape(str(file_name))
                            + "</code>"
                        )

                    remaining = len(commit_files) - len(shown_files)

                    if remaining > 0:
                        parts.append(
                            f"• … ещё {remaining}"
                        )

            parts.append("")

    parts.extend([
        "━━━━━━━━━━━━━━━━━━",
        "",
        "⚠️ /pending — ожидают решения",
        "📊 /status — состояние системы",
        "⚠️ /approvals — история решений",
        "",
        "<i>Atlas Activity Feed · v0.4</i>",
    ])

    await update.effective_message.reply_text(
        "\n".join(parts),
        parse_mode=ParseMode.HTML,
    )


# ─────────────────────────────────────────────

# ============================================================
# /TASKS — ATLAS WORK CENTER
# ============================================================

async def tasks_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if not authorized(update):
        await deny_access(update)
        return

    counts = count_tasks()
    tasks = list_tasks(10)

    status_map = {
        "NEW": ("🆕", "НОВАЯ"),
        "IN_PROGRESS": ("🔵", "В РАБОТЕ"),
        "WAITING_APPROVAL": ("🟡", "ЖДЁТ РЕШЕНИЯ"),
        "BLOCKED": ("🔴", "ЗАБЛОКИРОВАНА"),
        "DONE": ("✅", "ВЫПОЛНЕНО"),
        "CANCELLED": ("⚫️", "ОТМЕНЕНА"),
    }

    priority_map = {
        "LOW": "⚪️ LOW",
        "NORMAL": "🟢 NORMAL",
        "HIGH": "🔥 HIGH",
        "CRITICAL": "🚨 CRITICAL",
    }

    source_map = {
        "OWNER": "ВЛАДЕЛЕЦ",
        "ATLAS": "ATLAS",
        "SYSTEM": "СИСТЕМА",
    }

    parts = [
        "🎯 <b>ATLAS · ЦЕНТР ЗАДАЧ</b>",
        "",
        "━━━━━━━━━━━━━━━━━━",
        "",
        "📊 <b>Сводка</b>",
        f"🆕 Новые: <b>{counts.get('NEW', 0)}</b>",
        f"🔵 В работе: <b>{counts.get('IN_PROGRESS', 0)}</b>",
        (
            "🟡 Ждут решения: "
            f"<b>{counts.get('WAITING_APPROVAL', 0)}</b>"
        ),
        f"🔴 Заблокировано: <b>{counts.get('BLOCKED', 0)}</b>",
        f"✅ Выполнено: <b>{counts.get('DONE', 0)}</b>",
        "",
        "━━━━━━━━━━━━━━━━━━",
        "",
    ]

    keyboard = []

    if not tasks:
        parts.extend([
            "📭 Задач пока нет.",
            "",
        ])
    else:
        for task in tasks:
            emoji, status_text = status_map.get(
                task["status"],
                ("⚪️", task["status"]),
            )

            priority = priority_map.get(
                task["priority"],
                task["priority"],
            )

            source = source_map.get(
                task["source"],
                task["source"],
            )

            parts.extend([
                (
                    f"{emoji} <b>{html.escape(task['task_id'])}</b>"
                    f" · {priority}"
                ),
                html.escape(task["title"]),
                f"Статус: {emoji} {status_text}",
                f"Источник: {html.escape(source)}",
            ])

            if task.get("description"):
                description = task["description"]

                if len(description) > 180:
                    description = description[:177] + "..."

                parts.append(
                    "📝 "
                    + html.escape(description)
                )

            parts.append("")

            if task["status"] in TASK_STARTABLE_STATUSES:
                keyboard.append(
                    [
                        InlineKeyboardButton(
                            (
                                "▶️ В работу "
                                f"{task['task_id']}"
                            ),
                            callback_data=(
                                "task:start:"
                                f"{task['task_id']}"
                            ),
                        )
                    ]
                )

            if task["status"] in TASK_COMPLETABLE_STATUSES:
                keyboard.append(
                    [
                        InlineKeyboardButton(
                            (
                                "✅ Завершить "
                                f"{task['task_id']}"
                            ),
                            callback_data=(
                                "task:complete:"
                                f"{task['task_id']}"
                            ),
                        )
                    ]
                )

    parts.extend([
        "━━━━━━━━━━━━━━━━━━",
        "🧠 Work Engine · v0.1",
    ])

    reply_markup = (
        InlineKeyboardMarkup(keyboard)
        if keyboard
        else None
    )

    await update.effective_message.reply_text(
        "\n".join(parts),
        parse_mode=ParseMode.HTML,
        reply_markup=reply_markup,
    )


# ============================================================
# /NEWTASK — OWNER CREATE TASK
# ============================================================

NEWTASK_USAGE = (
    "➕ <b>ATLAS · НОВАЯ ЗАДАЧА</b>\n\n"
    "━━━━━━━━━━━━━━━━━━\n\n"
    "Формат:\n"
    "<code>/newtask название | описание | приоритет</code>\n\n"
    "Название — обязательно.\n"
    "Описание — необязательно.\n"
    "Приоритет — необязательно, по умолчанию "
    "<b>NORMAL</b>.\n\n"
    "Приоритеты: LOW, NORMAL, HIGH, CRITICAL\n\n"
    "Примеры:\n"
    "<code>/newtask Find second AI automation prospect</code>\n"
    "<code>/newtask Find second AI automation prospect | "
    "Research one real company and identify a concrete "
    "AI automation opportunity | HIGH</code>\n\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "<i>Atlas Work Engine · v0.1</i>"
)


async def newtask_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if not authorized(update):
        await deny_access(update)
        return

    raw = " ".join(context.args or []).strip()

    if not raw:
        await update.effective_message.reply_text(
            NEWTASK_USAGE,
            parse_mode=ParseMode.HTML,
        )
        return

    parts = [p.strip() for p in raw.split("|")]

    if len(parts) > 3:
        await update.effective_message.reply_text(
            "❌ Слишком много полей.\n\n"
            + NEWTASK_USAGE,
            parse_mode=ParseMode.HTML,
        )
        return

    title = parts[0]
    description = parts[1] if len(parts) >= 2 else ""
    priority = parts[2] if len(parts) >= 3 else "NORMAL"

    if not priority:
        priority = "NORMAL"

    if not title:
        await update.effective_message.reply_text(
            "❌ Название задачи обязательно.\n\n"
            + NEWTASK_USAGE,
            parse_mode=ParseMode.HTML,
        )
        return

    try:
        task = create_task(
            title=title,
            description=description,
            priority=priority,
            source="OWNER",
        )
    except ValueError as exc:
        await update.effective_message.reply_text(
            f"❌ {html.escape(str(exc))}\n\n"
            + NEWTASK_USAGE,
            parse_mode=ParseMode.HTML,
        )
        return

    status_map = {
        "NEW": ("🆕", "НОВАЯ"),
        "IN_PROGRESS": ("🔵", "В РАБОТЕ"),
        "WAITING_APPROVAL": ("🟡", "ЖДЁТ РЕШЕНИЯ"),
        "BLOCKED": ("🔴", "ЗАБЛОКИРОВАНА"),
        "DONE": ("✅", "ВЫПОЛНЕНО"),
        "CANCELLED": ("⚫️", "ОТМЕНЕНА"),
    }

    priority_map = {
        "LOW": "⚪️ LOW",
        "NORMAL": "🟢 NORMAL",
        "HIGH": "🔥 HIGH",
        "CRITICAL": "🚨 CRITICAL",
    }

    emoji, status_text = status_map.get(
        task["status"],
        ("⚪️", task["status"]),
    )

    priority_label = priority_map.get(
        task["priority"],
        task["priority"],
    )

    text = (
        "✅ <b>ATLAS · ЗАДАЧА СОЗДАНА</b>\n\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        f"🔖 ID: <b>{html.escape(task['task_id'])}</b>\n"
        f"📌 {html.escape(task['title'])}\n"
        f"Приоритет: {html.escape(str(priority_label))}\n"
        f"Статус: {emoji} {html.escape(str(status_text))}\n\n"
        "Просмотр: /tasks\n\n"
        "━━━━━━━━━━━━━━━━━━\n"
        "<i>Atlas Work Engine · v0.1</i>"
    )

    await update.effective_message.reply_text(
        text,
        parse_mode=ParseMode.HTML,
    )


# ============================================================
# TASK CALLBACK — OWNER START + COMPLETE
# ============================================================


async def task_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query

    if not query:
        return

    if not authorized(update):
        await query.answer(
            "⛔ Нет доступа",
            show_alert=True,
        )
        return

    data = query.data or ""
    parts = data.split(":", 2)

    if len(parts) != 3:
        await query.answer(
            "❌ Некорректная команда",
            show_alert=True,
        )
        return

    _, action, task_id = parts

    task = get_task(task_id)

    if not task:
        await query.answer(
            "❌ Задача не найдена",
            show_alert=True,
        )
        return

    # Start: NEW -> IN_PROGRESS only (no confirmation)
    if action == "start":
        if task["status"] not in TASK_STARTABLE_STATUSES:
            await query.answer(
                (
                    "Задача уже в статусе "
                    f"{task['status']}"
                ),
                show_alert=True,
            )
            return

        updated = update_task_status(
            task_id,
            "IN_PROGRESS",
        )

        if not updated:
            current = get_task(task_id)
            current_status = (
                current["status"]
                if current
                else "не найдена"
            )
            await query.answer(
                (
                    "Задача уже в статусе "
                    f"{current_status}"
                ),
                show_alert=True,
            )
            return

        await query.answer("▶️ Задача в работе")

        await query.message.reply_text(
            (
                "▶️ <b>ATLAS · ЗАДАЧА "
                "В РАБОТЕ</b>\n\n"
                "━━━━━━━━━━━━━━━━━━\n\n"
                "🆔 "
                f"<code>{html.escape(task_id)}</code>"
                "\n"
                "📌 "
                f"{html.escape(updated['title'])}"
                "\n"
                "Статус: 🔵 <b>В РАБОТЕ</b> "
                "(IN_PROGRESS)\n\n"
                "Обнови список: /tasks\n\n"
                "━━━━━━━━━━━━━━━━━━\n"
                "<i>Atlas Work Engine · v0.1</i>"
            ),
            parse_mode=ParseMode.HTML,
        )
        return

    # Step 1: ask for explicit confirmation (no state change)
    if action == "complete":
        if task["status"] not in TASK_COMPLETABLE_STATUSES:
            await query.answer(
                (
                    "Задача уже в статусе "
                    f"{task['status']}"
                ),
                show_alert=True,
            )
            return

        await query.answer()

        confirm_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Да, завершить",
                        callback_data=(
                            "task:confirm_done:"
                            f"{task_id}"
                        ),
                    ),
                    InlineKeyboardButton(
                        "❌ Отмена",
                        callback_data=(
                            "task:cancel_done:"
                            f"{task_id}"
                        ),
                    ),
                ]
            ]
        )

        await query.message.reply_text(
            (
                "⚠️ <b>ATLAS · ПОДТВЕРЖДЕНИЕ "
                "ЗАВЕРШЕНИЯ</b>\n\n"
                "━━━━━━━━━━━━━━━━━━\n\n"
                "🆔 "
                f"<code>{html.escape(task_id)}</code>"
                "\n"
                "📌 "
                f"{html.escape(task['title'])}"
                "\n"
                "Статус сейчас: "
                f"<b>{html.escape(task['status'])}</b>"
                "\n\n"
                "Завершить эту задачу?\n"
                "Статус станет "
                "✅ <b>DONE</b> / ВЫПОЛНЕНО.\n\n"
                "⚠️ Это не меняет Sales Pipeline "
                "и не отправляет внешних сообщений.\n\n"
                "━━━━━━━━━━━━━━━━━━\n"
                "<i>Atlas Work Engine · v0.1</i>"
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=confirm_markup,
        )
        return

    # Step 2a: cancel confirmation
    if action == "cancel_done":
        await query.answer("Отменено")
        await query.edit_message_reply_markup(
            reply_markup=None
        )
        await query.message.reply_text(
            (
                "↩️ Завершение "
                f"<code>{html.escape(task_id)}</code> "
                "отменено.\n"
                "Статус задачи не изменён."
            ),
            parse_mode=ParseMode.HTML,
        )
        return

    # Step 2b: confirmed → persist DONE only
    if action == "confirm_done":
        if task["status"] not in TASK_COMPLETABLE_STATUSES:
            await query.answer(
                (
                    "Задача уже в статусе "
                    f"{task['status']}"
                ),
                show_alert=True,
            )
            return

        updated = update_task_status(
            task_id,
            "DONE",
        )

        if not updated:
            current = get_task(task_id)
            current_status = (
                current["status"]
                if current
                else "не найдена"
            )
            await query.answer(
                (
                    "Задача уже в статусе "
                    f"{current_status}"
                ),
                show_alert=True,
            )
            return

        await query.answer("✅ Задача завершена")
        await query.edit_message_reply_markup(
            reply_markup=None
        )

        await query.message.reply_text(
            (
                "✅ <b>ATLAS · ЗАДАЧА "
                "ЗАВЕРШЕНА</b>\n\n"
                "━━━━━━━━━━━━━━━━━━\n\n"
                "🆔 "
                f"<code>{html.escape(task_id)}</code>"
                "\n"
                "📌 "
                f"{html.escape(updated['title'])}"
                "\n"
                "Статус: ✅ <b>ВЫПОЛНЕНО</b> "
                "(DONE)\n\n"
                "Обнови список: /tasks\n\n"
                "━━━━━━━━━━━━━━━━━━\n"
                "<i>Atlas Work Engine · v0.1</i>"
            ),
            parse_mode=ParseMode.HTML,
        )
        return

    await query.answer(
        "Неизвестное действие.",
        show_alert=True,
    )


# /APPROVALS
# ─────────────────────────────────────────────


# ============================================================
# /PIPELINE — ATLAS SALES PIPELINE
# ============================================================


FOLLOWUP_WORKDAYS = 4


def followup_wait_info(item):
    """
    Return:
        (business_days_waiting, followup_due)

    Send day itself is day 0.
    Saturday and Sunday are ignored.
    """

    sent_at = item.get("sent_at")

    if not sent_at:
        return 0, False

    try:
        sent_dt = dt.datetime.fromisoformat(
            str(sent_at)
        )

        if sent_dt.tzinfo is None:
            sent_dt = sent_dt.replace(
                tzinfo=dt.timezone.utc
            )

        sent_date = sent_dt.astimezone().date()
        today = (
            dt.datetime.now()
            .astimezone()
            .date()
        )

    except Exception:
        return 0, False

    if today <= sent_date:
        return 0, False

    business_days = 0
    cursor = sent_date

    while cursor < today:
        cursor += dt.timedelta(days=1)

        if cursor.weekday() < 5:
            business_days += 1

    return (
        business_days,
        business_days >= FOLLOWUP_WORKDAYS,
    )


def build_pipeline_view():
    counts = count_stages()

    all_items = list_outreach(50)
    items = all_items[:8]

    followup_due_count = sum(
        1
        for item in all_items
        if (
            str(item.get("stage") or "")
            == "WAITING_REPLY"
            and followup_wait_info(item)[1]
        )
    )

    stage_map = {
        "READY_TO_SEND": (
            "🟣",
            "ГОТОВО К ОТПРАВКЕ",
        ),
        "SENT": (
            "📤",
            "ОТПРАВЛЕНО",
        ),
        "WAITING_REPLY": (
            "🟡",
            "ЖДЁТ ОТВЕТА",
        ),
        "REPLIED": (
            "💬",
            "ПОЛУЧЕН ОТВЕТ",
        ),
        "MEETING": (
            "📅",
            "ВСТРЕЧА",
        ),
        "PROPOSAL": (
            "📄",
            "ПРЕДЛОЖЕНИЕ",
        ),
        "WON": (
            "🏆",
            "ВЫИГРАНО",
        ),
        "LOST": (
            "❌",
            "ПОТЕРЯНО",
        ),
    }

    parts = [
        "💼 <b>ATLAS · SALES PIPELINE</b>",
        "",
        "━━━━━━━━━━━━━━━━━━",
        "",
        "📊 <b>Сводка</b>",
        (
            "🟣 Готово к отправке: "
            f"<b>{counts['READY_TO_SEND']}</b>"
        ),
        (
            "📤 Отправлено: "
            f"<b>{counts['SENT']}</b>"
        ),
        (
            "🟡 Ждут ответа: "
            f"<b>{counts['WAITING_REPLY']}</b>"
        ),
        (
            "⏰ Follow-up пора: "
            f"<b>{followup_due_count}</b>"
        ),
        (
            "💬 Ответили: "
            f"<b>{counts['REPLIED']}</b>"
        ),
        (
            "📅 Встречи: "
            f"<b>{counts['MEETING']}</b>"
        ),
        (
            "📄 Предложения: "
            f"<b>{counts['PROPOSAL']}</b>"
        ),
        (
            "🏆 Выиграно: "
            f"<b>{counts['WON']}</b>"
        ),
        (
            "❌ Потеряно: "
            f"<b>{counts['LOST']}</b>"
        ),
        "",
        "━━━━━━━━━━━━━━━━━━",
        "",
        "🏢 <b>Контакты</b>",
        "",
    ]

    keyboard = []

    if not items:
        parts.append(
            "Пока нет компаний в Sales Pipeline."
        )

    else:
        for item in items:
            stage = str(
                item.get("stage") or ""
            )

            emoji, label = stage_map.get(
                stage,
                (
                    "⚪",
                    stage or "НЕИЗВЕСТНО",
                ),
            )

            raw_outreach_id = str(
                item.get("outreach_id") or "—"
            )

            outreach_id = html.escape(
                raw_outreach_id
            )

            company = html.escape(
                str(
                    item.get("company")
                    or "—"
                )
            )

            contact = html.escape(
                str(
                    item.get("contact_name")
                    or "—"
                )
            )

            role = html.escape(
                str(
                    item.get("contact_role")
                    or "—"
                )
            )

            channel = html.escape(
                str(
                    item.get("channel")
                    or "—"
                )
            )

            solution = html.escape(
                str(
                    item.get("solution")
                    or "—"
                )
            )

            task_id = html.escape(
                str(
                    item.get("task_id")
                    or "—"
                )
            )

            parts.extend(
                [
                    (
                        f"{emoji} <b>"
                        f"{outreach_id} · "
                        f"{company}</b>"
                    ),
                    (
                        f"Статус: {emoji} "
                        f"<b>{label}</b>"
                    ),
                    (
                        f"👤 {contact} · "
                        f"{role}"
                    ),
                    f"💡 {solution}",
                    f"🌐 {channel}",
                    (
                        f"🎯 "
                        f"<code>{task_id}</code>"
                    ),
                    "",
                ]
            )

            if stage == "WAITING_REPLY":
                wait_days, followup_due = (
                    followup_wait_info(item)
                )

                if followup_due:
                    parts.extend(
                        [
                            (
                                "⏰ <b>FOLLOW-UP ПОРА</b>"
                            ),
                            (
                                "Ожидание: "
                                f"<b>{wait_days}</b> "
                                "рабочих дней"
                            ),
                            "",
                        ]
                    )
                else:
                    parts.extend(
                        [
                            (
                                "⏳ Ожидание: "
                                f"<b>{wait_days}/"
                                f"{FOLLOWUP_WORKDAYS}</b> "
                                "рабочих дней"
                            ),
                            "",
                        ]
                    )

            # ---------------------------------------------
            # READY TO SEND
            # ---------------------------------------------

            if stage == "READY_TO_SEND":
                keyboard.append(
                    [
                        InlineKeyboardButton(
                            (
                                "📄 "
                                f"{raw_outreach_id} · "
                                "Текст обращения"
                            ),
                            callback_data=(
                                "pipeline:text:"
                                f"{raw_outreach_id}"
                            ),
                        ),
                    ]
                )

                keyboard.append(
                    [
                        InlineKeyboardButton(
                            (
                                "📤 "
                                f"{raw_outreach_id} · "
                                "Я отправил"
                            ),
                            callback_data=(
                                "pipeline:sent:"
                                f"{raw_outreach_id}"
                            ),
                        ),
                    ]
                )

            # ---------------------------------------------
            # WAITING FOR COMPANY
            # ---------------------------------------------

            if stage == "WAITING_REPLY":
                keyboard.append(
                    [
                        InlineKeyboardButton(
                            (
                                "💬 "
                                f"{raw_outreach_id} · "
                                "Компания ответила"
                            ),
                            callback_data=(
                                "pipeline:reply:"
                                f"{raw_outreach_id}"
                            ),
                        ),
                    ]
                )

            if stage == "WAITING_REPLY":
                _, followup_due = (
                    followup_wait_info(item)
                )

                if followup_due:
                    keyboard.append(
                        [
                            InlineKeyboardButton(
                                (
                                    "📝 "
                                    f"{raw_outreach_id} · "
                                    "Подготовить follow-up"
                                ),
                                callback_data=(
                                    "pipeline:followup:"
                                    f"{raw_outreach_id}"
                                ),
                            ),
                        ]
                    )

            # ---------------------------------------------
            # REPLIED
            # ---------------------------------------------

            if stage == "REPLIED":
                keyboard.append(
                    [
                        InlineKeyboardButton(
                            (
                                "📨 "
                                f"{raw_outreach_id} · "
                                "Показать ответ"
                            ),
                            callback_data=(
                                "pipeline:showreply:"
                                f"{raw_outreach_id}"
                            ),
                        ),
                    ]
                )

                keyboard.append(
                    [
                        InlineKeyboardButton(
                            (
                                "📅 "
                                f"{raw_outreach_id} · "
                                "Встреча назначена"
                            ),
                            callback_data=(
                                "pipeline:meeting:"
                                f"{raw_outreach_id}"
                            ),
                        ),
                    ]
                )

            # ---------------------------------------------
            # MEETING
            # ---------------------------------------------

            if stage == "MEETING":
                keyboard.append(
                    [
                        InlineKeyboardButton(
                            (
                                "📄 "
                                f"{raw_outreach_id} · "
                                "Предложение отправлено"
                            ),
                            callback_data=(
                                "pipeline:proposal:"
                                f"{raw_outreach_id}"
                            ),
                        ),
                    ]
                )

                keyboard.append(
                    [
                        InlineKeyboardButton(
                            (
                                "❌ "
                                f"{raw_outreach_id} · "
                                "Потеряно"
                            ),
                            callback_data=(
                                "pipeline:lost:"
                                f"{raw_outreach_id}"
                            ),
                        ),
                    ]
                )

            # ---------------------------------------------
            # PROPOSAL
            # ---------------------------------------------

            if stage == "PROPOSAL":
                keyboard.append(
                    [
                        InlineKeyboardButton(
                            (
                                "✅ "
                                f"{raw_outreach_id} · "
                                "Выиграно"
                            ),
                            callback_data=(
                                "pipeline:won:"
                                f"{raw_outreach_id}"
                            ),
                        ),
                    ]
                )

                keyboard.append(
                    [
                        InlineKeyboardButton(
                            (
                                "❌ "
                                f"{raw_outreach_id} · "
                                "Потеряно"
                            ),
                            callback_data=(
                                "pipeline:lost:"
                                f"{raw_outreach_id}"
                            ),
                        ),
                    ]
                )

    parts.extend(
        [
            "━━━━━━━━━━━━━━━━━━",
            "",
            (
                "🔐 Atlas не выполняет внешние "
                "действия этими кнопками."
            ),
            (
                "📤 Отправка и 💬 получение ответа "
                "фиксируются владельцем по факту."
            ),
            "",
            "<i>Atlas Sales Pipeline · v0.4</i>",
        ]
    )

    markup = (
        InlineKeyboardMarkup(keyboard)
        if keyboard
        else None
    )

    return "\n".join(parts), markup


async def pipeline_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if not authorized(update):
        await deny_access(update)
        return

    text, markup = build_pipeline_view()

    await update.effective_message.reply_text(
        text,
        parse_mode=ParseMode.HTML,
        reply_markup=markup,
    )


async def pipeline_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query

    if not query:
        return

    if not authorized(update):
        await query.answer(
            "⛔ Нет доступа",
            show_alert=True,
        )
        return

    data = query.data or ""
    parts = data.split(":", 2)

    if len(parts) != 3:
        await query.answer(
            "❌ Некорректная команда",
            show_alert=True,
        )
        return

    _, action, outreach_id = parts

    item = get_outreach(outreach_id)

    if not item:
        await query.answer(
            "❌ Контакт не найден",
            show_alert=True,
        )
        return

    # ====================================================
    # SHOW OUTBOUND MESSAGE
    # ====================================================

    if action == "text":
        await query.answer()

        company = html.escape(
            str(
                item.get("company")
                or "—"
            )
        )

        message = html.escape(
            str(
                item.get("message")
                or "—"
            )
        )

        await query.message.reply_text(
            (
                "📄 <b>ATLAS · "
                "ТЕКСТ ОБРАЩЕНИЯ</b>\n\n"
                "━━━━━━━━━━━━━━━━━━\n\n"
                f"🏢 <b>{company}</b>\n"
                "🆔 "
                f"<code>{html.escape(outreach_id)}</code>"
                "\n\n"
                f"{message}\n\n"
                "━━━━━━━━━━━━━━━━━━\n\n"
                "🔐 Просмотр текста ничего "
                "компании не отправляет.\n\n"
                "<i>Atlas Sales Pipeline · v0.4</i>"
            ),
            parse_mode=ParseMode.HTML,
        )

        return

    # ====================================================
    # OWNER CONFIRMS MANUAL SEND
    # ====================================================

    if action == "sent":
        current_stage = str(
            item.get("stage") or ""
        )

        if current_stage == "WAITING_REPLY":
            await query.answer(
                (
                    "🟡 Уже отмечено "
                    "как отправленное"
                ),
                show_alert=True,
            )
            return

        if current_stage != "READY_TO_SEND":
            await query.answer(
                (
                    "Текущая стадия: "
                    f"{current_stage}"
                ),
                show_alert=True,
            )
            return

        if not update_stage(
            outreach_id,
            "SENT",
        ):
            await query.answer(
                "❌ Не удалось сохранить SENT",
                show_alert=True,
            )
            return

        if not update_stage(
            outreach_id,
            "WAITING_REPLY",
        ):
            await query.answer(
                (
                    "⚠️ SENT сохранён, "
                    "но WAITING_REPLY "
                    "не удалось сохранить"
                ),
                show_alert=True,
            )
            return

        log_event(
            event_type="OUTREACH_SENT",
            source="Atlas Sales Engine",
            title=(
                "Первое обращение "
                "отмечено отправленным"
            ),
            details=(
                f"{outreach_id} · "
                f"{item.get('company') or '—'} · "
                "Владелец подтвердил ручную "
                "отправку. Atlas технически "
                "сообщение не отправлял. "
                "Контакт переведён "
                "в WAITING_REPLY."
            ),
            metadata={
                "outreach_id": outreach_id,
                "task_id": item.get("task_id"),
                "company": item.get("company"),
                "stage": "WAITING_REPLY",
                "external_action": True,
                "atlas_executed": False,
                "execution_mode": (
                    "manual_owner_confirmation"
                ),
            },
        )

        await query.answer(
            "✅ Отправка зафиксирована"
        )

        text, markup = build_pipeline_view()

        await query.edit_message_text(
            text,
            parse_mode=ParseMode.HTML,
            reply_markup=markup,
        )

        await query.message.reply_text(
            (
                "📤 <b>ATLAS · "
                "ОТПРАВКА ЗАФИКСИРОВАНА</b>"
                "\n\n"
                "🆔 "
                f"<code>{html.escape(outreach_id)}</code>"
                "\n"
                "✅ Фактическая отправка "
                "подтверждена владельцем.\n"
                "🟡 Теперь Atlas ожидает "
                "ответ компании.\n\n"
                "🔐 Atlas сам сообщение "
                "не отправлял."
            ),
            parse_mode=ParseMode.HTML,
        )

        return

    # ====================================================
    # COMPANY REPLIED -> WAIT FOR OWNER TO PASTE TEXT
    # ====================================================

    if action == "reply":
        current_stage = str(
            item.get("stage") or ""
        )

        if current_stage == "REPLIED":
            await query.answer(
                "💬 Ответ уже зарегистрирован",
                show_alert=True,
            )
            return

        if current_stage != "WAITING_REPLY":
            await query.answer(
                (
                    "Текущая стадия: "
                    f"{current_stage}"
                ),
                show_alert=True,
            )
            return

        context.user_data[
            "pipeline_reply_outreach_id"
        ] = outreach_id

        await query.answer(
            "💬 Жду текст ответа компании"
        )

        cancel_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❌ Отмена",
                        callback_data=(
                            "pipeline:cancelreply:"
                            f"{outreach_id}"
                        ),
                    )
                ]
            ]
        )

        await query.message.reply_text(
            (
                "💬 <b>ATLAS · "
                "РЕГИСТРАЦИЯ ОТВЕТА</b>\n\n"
                "🆔 "
                f"<code>{html.escape(outreach_id)}</code>"
                "\n\n"
                "Вставь следующим сообщением "
                "<b>реальный текст ответа "
                "компании</b>.\n\n"
                "Atlas сохранит его локально "
                "и переведёт контакт в "
                "💬 <b>REPLIED</b>.\n\n"
                "⚠️ Следующее обычное текстовое "
                "сообщение будет считаться "
                "ответом компании."
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=cancel_markup,
        )

        return

    # ====================================================
    # PREPARE FOLLOW-UP DRAFT
    # ====================================================

    if action == "followup":
        current_stage = str(
            item.get("stage") or ""
        )

        if current_stage != "WAITING_REPLY":
            await query.answer(
                (
                    "Текущая стадия: "
                    f"{current_stage}"
                ),
                show_alert=True,
            )
            return

        wait_days, followup_due = (
            followup_wait_info(item)
        )

        if not followup_due:
            await query.answer(
                (
                    "⏳ Follow-up ещё рано: "
                    f"{wait_days}/"
                    f"{FOLLOWUP_WORKDAYS} "
                    "рабочих дней"
                ),
                show_alert=True,
            )
            return

        company = str(
            item.get("company")
            or "the team"
        )

        draft = (
            f"Hello {company} team,\n\n"
            "I’m following up on my previous "
            "message from Atlas Lab regarding "
            "AI-assisted automation for "
            "recruitment operations.\n\n"
            "If this is relevant to your "
            "operations team, we’d be happy "
            "to prepare a small prototype "
            "around one repetitive workflow "
            "and show it in a short "
            "15-minute call.\n\n"
            "If there is someone else "
            "responsible for recruitment "
            "operations or process "
            "improvement, I’d appreciate it "
            "if you could forward this "
            "message to them.\n\n"
            "Best regards,\n"
            "Atlas Lab"
        )

        await query.answer()

        await query.message.reply_text(
            (
                "📝 <b>ATLAS · "
                "FOLLOW-UP DRAFT</b>\n\n"
                "🆔 "
                f"<code>{html.escape(outreach_id)}</code>"
                "\n"
                "🏢 "
                f"<b>{html.escape(company)}</b>\n"
                "⏰ Ожидание: "
                f"<b>{wait_days}</b> "
                "рабочих дней\n\n"
                "━━━━━━━━━━━━━━━━━━\n\n"
                f"{html.escape(draft)}"
                "\n\n"
                "━━━━━━━━━━━━━━━━━━\n\n"
                "🔐 Это только черновик.\n"
                "Atlas ничего компании "
                "не отправил.\n"
                "Для реальной отправки будет "
                "нужно отдельное разрешение "
                "владельца."
            ),
            parse_mode=ParseMode.HTML,
        )

        return

    # ====================================================
    # CANCEL REPLY CAPTURE
    # ====================================================

    if action == "cancelreply":
        active_id = context.user_data.get(
            "pipeline_reply_outreach_id"
        )

        if active_id == outreach_id:
            context.user_data.pop(
                "pipeline_reply_outreach_id",
                None,
            )

        await query.answer(
            "✅ Регистрация ответа отменена"
        )

        try:
            await query.edit_message_reply_markup(
                reply_markup=None
            )
        except Exception:
            pass

        return

    # ====================================================
    # SHOW SAVED INBOUND REPLY
    # ====================================================

    if action == "showreply":
        metadata = item.get("metadata") or {}

        reply_text = str(
            metadata.get("last_reply_text")
            or ""
        ).strip()

        if not reply_text:
            await query.answer(
                "Ответ ещё не сохранён",
                show_alert=True,
            )
            return

        await query.answer()

        display_reply = reply_text

        if len(display_reply) > 3500:
            display_reply = (
                display_reply[:3500]
                + "\n\n…"
            )

        await query.message.reply_text(
            (
                "📨 <b>ATLAS · "
                "ОТВЕТ КОМПАНИИ</b>\n\n"
                "🆔 "
                f"<code>{html.escape(outreach_id)}</code>"
                "\n"
                "🏢 "
                f"<b>{html.escape(str(item.get('company') or '—'))}</b>"
                "\n\n"
                "━━━━━━━━━━━━━━━━━━\n\n"
                f"{html.escape(display_reply)}"
                "\n\n"
                "━━━━━━━━━━━━━━━━━━\n\n"
                "<i>Atlas Sales Pipeline · v0.4</i>"
            ),
            parse_mode=ParseMode.HTML,
        )

        return

    # ====================================================
    # MEETING SCHEDULED (REPLIED -> MEETING)
    # ====================================================

    if action == "meeting":
        current_stage = str(
            item.get("stage") or ""
        )

        if current_stage == "MEETING":
            await query.answer(
                "🟡 Уже отмечено как MEETING",
                show_alert=True,
            )
            return

        if current_stage != "REPLIED":
            await query.answer(
                (
                    "Текущая стадия: "
                    f"{current_stage}"
                ),
                show_alert=True,
            )
            return

        if not update_stage(
            outreach_id,
            "MEETING",
        ):
            await query.answer(
                "❌ Не удалось сохранить MEETING",
                show_alert=True,
            )
            return

        log_event(
            event_type="OUTREACH_MEETING_SCHEDULED",
            source="Atlas Sales Engine",
            title="Встреча назначена",
            details=(
                f"{outreach_id} · "
                f"{item.get('company') or '—'} · "
                "Владелец подтвердил назначение "
                "встречи вручную. Контакт "
                "переведён в MEETING."
            ),
            metadata={
                "outreach_id": outreach_id,
                "task_id": item.get("task_id"),
                "company": item.get("company"),
                "stage": "MEETING",
                "external_action": True,
                "atlas_executed": False,
                "execution_mode": (
                    "manual_owner_confirmation"
                ),
            },
        )

        await query.answer(
            "✅ Встреча зафиксирована"
        )

        text, markup = build_pipeline_view()

        await query.edit_message_text(
            text,
            parse_mode=ParseMode.HTML,
            reply_markup=markup,
        )

        await query.message.reply_text(
            (
                "📅 <b>ATLAS · "
                "ВСТРЕЧА НАЗНАЧЕНА</b>"
                "\n\n"
                "🆔 "
                f"<code>{html.escape(outreach_id)}</code>"
                "\n"
                "✅ Владелец подтвердил "
                "назначение встречи.\n\n"
                "🔐 Atlas ничего компании "
                "не отправлял."
            ),
            parse_mode=ParseMode.HTML,
        )

        return

    # ====================================================
    # PROPOSAL SENT (MEETING -> PROPOSAL)
    # ====================================================

    if action == "proposal":
        current_stage = str(
            item.get("stage") or ""
        )

        if current_stage == "PROPOSAL":
            await query.answer(
                "🟡 Уже отмечено как PROPOSAL",
                show_alert=True,
            )
            return

        if current_stage != "MEETING":
            await query.answer(
                (
                    "Текущая стадия: "
                    f"{current_stage}"
                ),
                show_alert=True,
            )
            return

        if not update_stage(
            outreach_id,
            "PROPOSAL",
        ):
            await query.answer(
                "❌ Не удалось сохранить PROPOSAL",
                show_alert=True,
            )
            return

        log_event(
            event_type="OUTREACH_PROPOSAL_SENT",
            source="Atlas Sales Engine",
            title="Предложение отправлено",
            details=(
                f"{outreach_id} · "
                f"{item.get('company') or '—'} · "
                "Владелец подтвердил отправку "
                "предложения вручную. Atlas "
                "технически ничего не отправлял. "
                "Контакт переведён в PROPOSAL."
            ),
            metadata={
                "outreach_id": outreach_id,
                "task_id": item.get("task_id"),
                "company": item.get("company"),
                "stage": "PROPOSAL",
                "external_action": True,
                "atlas_executed": False,
                "execution_mode": (
                    "manual_owner_confirmation"
                ),
            },
        )

        await query.answer(
            "✅ Предложение зафиксировано"
        )

        text, markup = build_pipeline_view()

        await query.edit_message_text(
            text,
            parse_mode=ParseMode.HTML,
            reply_markup=markup,
        )

        await query.message.reply_text(
            (
                "📄 <b>ATLAS · "
                "ПРЕДЛОЖЕНИЕ ОТПРАВЛЕНО</b>"
                "\n\n"
                "🆔 "
                f"<code>{html.escape(outreach_id)}</code>"
                "\n"
                "✅ Фактическая отправка "
                "предложения подтверждена "
                "владельцем.\n\n"
                "🔐 Atlas сам ничего "
                "не отправлял."
            ),
            parse_mode=ParseMode.HTML,
        )

        return

    # ====================================================
    # WON (PROPOSAL -> WON)
    # ====================================================

    if action == "won":
        current_stage = str(
            item.get("stage") or ""
        )

        if current_stage == "WON":
            await query.answer(
                "🟡 Уже отмечено как WON",
                show_alert=True,
            )
            return

        if current_stage != "PROPOSAL":
            await query.answer(
                (
                    "Текущая стадия: "
                    f"{current_stage}"
                ),
                show_alert=True,
            )
            return

        if not update_stage(
            outreach_id,
            "WON",
        ):
            await query.answer(
                "❌ Не удалось сохранить WON",
                show_alert=True,
            )
            return

        log_event(
            event_type="OUTREACH_WON",
            source="Atlas Sales Engine",
            title="Сделка выиграна",
            details=(
                f"{outreach_id} · "
                f"{item.get('company') or '—'} · "
                "Владелец подтвердил победу "
                "вручную. Контакт переведён "
                "в WON."
            ),
            metadata={
                "outreach_id": outreach_id,
                "task_id": item.get("task_id"),
                "company": item.get("company"),
                "stage": "WON",
                "external_action": True,
                "atlas_executed": False,
                "execution_mode": (
                    "manual_owner_confirmation"
                ),
            },
        )

        await query.answer(
            "🏆 Победа зафиксирована"
        )

        text, markup = build_pipeline_view()

        await query.edit_message_text(
            text,
            parse_mode=ParseMode.HTML,
            reply_markup=markup,
        )

        await query.message.reply_text(
            (
                "✅ <b>ATLAS · "
                "СДЕЛКА ВЫИГРАНА</b>"
                "\n\n"
                "🆔 "
                f"<code>{html.escape(outreach_id)}</code>"
                "\n"
                "🏆 Владелец подтвердил "
                "выигрыш сделки вручную.\n\n"
                "🔐 Atlas ничего компании "
                "не отправлял."
            ),
            parse_mode=ParseMode.HTML,
        )

        return

    # ====================================================
    # LOST (MEETING or PROPOSAL -> LOST)
    # ====================================================

    if action == "lost":
        current_stage = str(
            item.get("stage") or ""
        )

        if current_stage == "LOST":
            await query.answer(
                "🟡 Уже отмечено как LOST",
                show_alert=True,
            )
            return

        if current_stage not in (
            "MEETING",
            "PROPOSAL",
        ):
            await query.answer(
                (
                    "Текущая стадия: "
                    f"{current_stage}"
                ),
                show_alert=True,
            )
            return

        if not update_stage(
            outreach_id,
            "LOST",
        ):
            await query.answer(
                "❌ Не удалось сохранить LOST",
                show_alert=True,
            )
            return

        log_event(
            event_type="OUTREACH_LOST",
            source="Atlas Sales Engine",
            title="Сделка потеряна",
            details=(
                f"{outreach_id} · "
                f"{item.get('company') or '—'} · "
                "Владелец отметил сделку как "
                "потерянную вручную. Контакт "
                "переведён в LOST."
            ),
            metadata={
                "outreach_id": outreach_id,
                "task_id": item.get("task_id"),
                "company": item.get("company"),
                "stage": "LOST",
                "external_action": True,
                "atlas_executed": False,
                "execution_mode": (
                    "manual_owner_confirmation"
                ),
            },
        )

        await query.answer(
            "📉 Потеря зафиксирована"
        )

        text, markup = build_pipeline_view()

        await query.edit_message_text(
            text,
            parse_mode=ParseMode.HTML,
            reply_markup=markup,
        )

        await query.message.reply_text(
            (
                "❌ <b>ATLAS · "
                "СДЕЛКА ПОТЕРЯНА</b>"
                "\n\n"
                "🆔 "
                f"<code>{html.escape(outreach_id)}</code>"
                "\n"
                "📉 Владелец отметил сделку "
                "как потерянную вручную.\n\n"
                "🔐 Atlas ничего компании "
                "не отправлял."
            ),
            parse_mode=ParseMode.HTML,
        )

        return

    await query.answer(
        "❌ Неизвестное действие",
        show_alert=True,
    )


async def pipeline_reply_capture(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    outreach_id = context.user_data.get(
        "pipeline_reply_outreach_id"
    )

    if not outreach_id:
        return

    if not authorized(update):
        return

    message = update.effective_message

    if not message or not message.text:
        return

    reply_text = message.text.strip()

    if not reply_text:
        return

    if reply_text.lower() in {
        "отмена",
        "cancel",
        "отменить",
    }:
        context.user_data.pop(
            "pipeline_reply_outreach_id",
            None,
        )

        await message.reply_text(
            "✅ Регистрация ответа отменена."
        )

        return

    item = get_outreach(outreach_id)

    if not item:
        context.user_data.pop(
            "pipeline_reply_outreach_id",
            None,
        )

        await message.reply_text(
            "❌ Контакт Sales Pipeline не найден."
        )

        return

    current_stage = str(
        item.get("stage") or ""
    )

    if current_stage not in {
        "WAITING_REPLY",
        "SENT",
    }:
        context.user_data.pop(
            "pipeline_reply_outreach_id",
            None,
        )

        await message.reply_text(
            (
                "⚠️ Ответ не сохранён.\n"
                "Текущая стадия контакта: "
                f"{current_stage}"
            )
        )

        return

    if not record_inbound_reply(
        outreach_id,
        reply_text,
    ):
        await message.reply_text(
            "❌ Не удалось сохранить ответ."
        )
        return

    context.user_data.pop(
        "pipeline_reply_outreach_id",
        None,
    )

    preview = reply_text.replace(
        "\n",
        " ",
    )[:350]

    log_event(
        event_type="OUTREACH_REPLIED",
        source="Atlas Sales Engine",
        title="Получен ответ компании",
        details=(
            f"{outreach_id} · "
            f"{item.get('company') or '—'} · "
            "Владелец зарегистрировал "
            "реальный входящий ответ. "
            f"Preview: {preview}"
        ),
        metadata={
            "outreach_id": outreach_id,
            "task_id": item.get("task_id"),
            "company": item.get("company"),
            "stage": "REPLIED",
            "reply_length": len(reply_text),
            "captured_by": "OWNER",
        },
    )

    await message.reply_text(
        (
            "💬 <b>ATLAS · "
            "ОТВЕТ ЗАРЕГИСТРИРОВАН</b>\n\n"
            "🆔 "
            f"<code>{html.escape(outreach_id)}</code>"
            "\n"
            "✅ Текст ответа сохранён локально.\n"
            "💬 Статус изменён на "
            "<b>ПОЛУЧЕН ОТВЕТ</b>.\n\n"
            "Следующий этап Atlas определит "
            "после анализа ответа."
        ),
        parse_mode=ParseMode.HTML,
    )


async def approvals_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if not authorized(update):
        await deny_access(update)
        return

    counts = count_approvals()
    items = list_approvals(5)

    status_map = {
        "PENDING": ("🟡", "ОЖИДАЕТ РЕШЕНИЯ"),
        "APPROVED": ("🟢", "ПОДТВЕРЖДЕНО"),
        "REJECTED": ("🔴", "ОТКЛОНЕНО"),
    }

    def format_time(value):
        if not value:
            return "—"

        try:
            dt = datetime.fromisoformat(value)
            return dt.astimezone().strftime("%d.%m · %H:%M")
        except Exception:
            return "—"

    parts = [
        "⚠️ <b>ATLAS · APPROVAL INBOX</b>",
        "",
        "━━━━━━━━━━━━━━━━━━",
        "",
        "📊 <b>Сводка</b>",
        "",
        f"🟡 Ожидают решения: <b>{counts['PENDING']}</b>",
        f"🟢 Подтверждено: <b>{counts['APPROVED']}</b>",
        f"🔴 Отклонено: <b>{counts['REJECTED']}</b>",
        "",
        "━━━━━━━━━━━━━━━━━━",
        "",
        "🕘 <b>Последние запросы</b>",
        "",
    ]

    if not items:
        parts.append("Запросов пока нет.")
    else:
        for item in items:
            emoji, label = status_map.get(
                item["status"],
                ("⚪️", item["status"]),
            )

            event_time = format_time(
                item["decided_at"] or item["created_at"]
            )

            parts.extend([
                f"{emoji} <code>{html.escape(item['approval_id'])}</code>",
                f"<b>{html.escape(item['title'])}</b>",
                f"{label} · {event_time}",
                "",
            ])

    parts.extend([
        "━━━━━━━━━━━━━━━━━━",
        "",
        "<i>Atlas Approval Inbox · v0.3</i>",
    ])

    await update.effective_message.reply_text(
        "\n".join(parts),
        parse_mode=ParseMode.HTML,
    )



# ─────────────────────────────────────────────
# /PENDING
# ─────────────────────────────────────────────

async def pending_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if not authorized(update):
        await deny_access(update)
        return

    items = list_pending(10)

    if not items:
        await update.effective_message.reply_text(
            "✅ <b>ATLAS · APPROVAL INBOX</b>\n\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            "🟢 Активных запросов нет.\n\n"
            "Все решения обработаны.\n\n"
            "━━━━━━━━━━━━━━━━━━\n"
            "<i>Atlas Approval Inbox · v0.4</i>",
            parse_mode=ParseMode.HTML,
        )
        return

    await update.effective_message.reply_text(
        "⚠️ <b>ATLAS · ОЖИДАЮТ РЕШЕНИЯ</b>\n\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        f"🟡 Активных запросов: <b>{len(items)}</b>\n\n"
        "Ниже находятся действия, которые Atlas "
        "не выполнит без решения владельца.\n\n"
        "━━━━━━━━━━━━━━━━━━",
        parse_mode=ParseMode.HTML,
    )

    for item in items:
        approval_id = item["approval_id"]

        try:
            created = datetime.fromisoformat(
                item["created_at"]
            ).astimezone().strftime("%d.%m · %H:%M")
        except Exception:
            created = "—"

        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "✅ Подтвердить",
                    callback_data=f"approval:approve:{approval_id}",
                ),
                InlineKeyboardButton(
                    "❌ Отклонить",
                    callback_data=f"approval:reject:{approval_id}",
                ),
            ],
            [
                InlineKeyboardButton(
                    "📋 Подробнее",
                    callback_data=f"approval:details:{approval_id}",
                ),
            ],
        ])

        text = (
            "🟡 <b>ОЖИДАЕТ РЕШЕНИЯ</b>\n\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            f"📌 <b>{html.escape(item['title'])}</b>\n\n"
            f"🧩 Тип: <code>{html.escape(item['action_type'])}</code>\n\n"
            f"📝 {html.escape(item['details'])}\n\n"
            f"🕐 Создан: {created}\n"
            f"🔖 ID: <code>{html.escape(approval_id)}</code>\n\n"
            "🔐 Без подтверждения действие не выполняется.\n\n"
            "━━━━━━━━━━━━━━━━━━\n"
            "<i>Atlas Approval Inbox · v0.4</i>"
        )

        await update.effective_message.reply_text(
            text,
            parse_mode=ParseMode.HTML,
            reply_markup=keyboard,
        )


# ─────────────────────────────────────────────
# APPROVAL INBOX
# ─────────────────────────────────────────────

async def approval_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query

    if not query:
        return

    user = query.from_user

    if not user or user.id not in OWNER_IDS:
        await query.answer(
            "⛔ У вас нет доступа к этому действию.",
            show_alert=True,
        )
        return

    data = query.data or ""
    parts = data.split(":", 2)

    if len(parts) != 3 or parts[0] != "approval":
        await query.answer("Некорректная команда.")
        return

    action = parts[1]
    approval_id = parts[2]

    approval = get_approval(approval_id)

    if not approval:
        await query.answer(
            "❌ Approval не найден в хранилище.",
            show_alert=True,
        )
        return

    if action == "details":
        await query.answer()

        status_map = {
            "PENDING": "🟡 ОЖИДАЕТ РЕШЕНИЯ",
            "APPROVED": "🟢 ПОДТВЕРЖДЕНО",
            "REJECTED": "🔴 ОТКЛОНЕНО",
        }

        await query.message.reply_text(
            "📋 <b>ATLAS · ДЕТАЛИ РЕШЕНИЯ</b>\n\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            f"🔖 <b>ID</b>\n<code>{html.escape(approval_id)}</code>\n\n"
            f"📌 <b>Действие</b>\n{html.escape(approval['title'])}\n\n"
            f"🧩 <b>Тип</b>\n{html.escape(approval['action_type'])}\n\n"
            f"📝 <b>Описание</b>\n{html.escape(approval['details'])}\n\n"
            f"📊 <b>Статус</b>\n"
            f"{status_map.get(approval['status'], approval['status'])}\n\n"
            "━━━━━━━━━━━━━━━━━━\n"
            "<i>Atlas Approval Inbox · v0.2</i>",
            parse_mode=ParseMode.HTML,
        )
        return

    if action not in {"approve", "reject"}:
        await query.answer("Неизвестное действие.")
        return

    decision = "APPROVED" if action == "approve" else "REJECTED"

    outcome = apply_approval_decision(
        approval_id=approval_id,
        decision=decision,
        decided_by=user.id,
    )

    result = outcome["reason"]
    propagation = outcome.get("propagation") or "NONE"

    if result == "NOT_FOUND":
        await query.answer(
            "❌ Approval не найден.",
            show_alert=True,
        )
        return

    if result == "ALREADY_DECIDED":
        current = outcome.get("approval") or get_approval(approval_id)

        status_text = (
            "🟢 уже подтверждено"
            if current and current["status"] == "APPROVED"
            else "🔴 уже отклонено"
        )

        await query.answer(
            f"Это решение {status_text}.",
            show_alert=True,
        )
        return

    await query.edit_message_reply_markup(reply_markup=None)

    task_note = ""
    if propagation == "INCOMPATIBLE":
        task_note = (
            "⚠️ Связанная задача не изменена — "
            "текущий статус не допускает переход.\n\n"
        )
    elif propagation == "PENDING":
        task_note = (
            "⚠️ Решение сохранено, но связанная "
            "задача ещё не синхронизирована.\n\n"
        )

    if result == "APPROVED":
        await query.answer("✅ Решение подтверждено")

        await query.message.reply_text(
            "✅ <b>ATLAS · РЕШЕНИЕ ЗАРЕГИСТРИРОВАНО</b>\n\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            f"🔖 ID: <code>{html.escape(approval_id)}</code>\n"
            "Статус: 🟢 <b>ПОДТВЕРЖДЕНО</b>\n\n"
            "👤 Решение владельца сохранено в Approval Store.\n\n"
            f"{task_note}"
            "⚠️ Само внешнее действие пока автоматически "
            "не выполняется.\n\n"
            "━━━━━━━━━━━━━━━━━━\n"
            "<i>Atlas Approval Inbox · v0.2</i>",
            parse_mode=ParseMode.HTML,
        )
        return

    await query.answer("❌ Действие отклонено")

    await query.message.reply_text(
        "❌ <b>ATLAS · РЕШЕНИЕ ЗАРЕГИСТРИРОВАНО</b>\n\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        f"🔖 ID: <code>{html.escape(approval_id)}</code>\n"
        "Статус: 🔴 <b>ОТКЛОНЕНО</b>\n\n"
        "👤 Решение владельца сохранено в Approval Store.\n\n"
        f"{task_note}"
        "🛑 Atlas не будет выполнять это действие.\n\n"
        "━━━━━━━━━━━━━━━━━━\n"
        "<i>Atlas Approval Inbox · v0.2</i>",
        parse_mode=ParseMode.HTML,
    )


# ─────────────────────────────────────────────
# TELEGRAM MENU
# ─────────────────────────────────────────────

async def post_init(application: Application):
    await application.bot.set_my_commands(
        [
            BotCommand("start", "🏠 Центр управления"),
            BotCommand("status", "📊 Состояние Atlas"),
            BotCommand("activity", "🧠 Журнал активности"),
            BotCommand("report", "📊 Отчёт владельцу"),
            BotCommand("tasks", "🎯 Задачи Atlas"),
            BotCommand("newtask", "➕ Новая задача"),
            BotCommand("pipeline", "💼 Sales Pipeline"),
            BotCommand("approvals", "⚠️ Approval Inbox"),
            BotCommand("pending", "🟡 Ожидают решения"),
            BotCommand("help", "❓ Команды"),
        ]
    )

    try:
        recover_pending_propagations()
    except Exception:
        logger.exception(
            "Approval task-propagation recovery failed"
        )


# ─────────────────────────────────────────────
# START
# ─────────────────────────────────────────────

def main():
    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .build()
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("status", status))
    application.add_handler(CommandHandler("activity", activity_command))
    application.add_handler(CommandHandler("report", report_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("tasks", tasks_command))
    application.add_handler(CommandHandler("newtask", newtask_command))
    application.add_handler(CommandHandler("pipeline", pipeline_command))
    application.add_handler(CommandHandler("approvals", approvals_command))
    application.add_handler(CommandHandler("pending", pending_command))
    application.add_handler(
        CallbackQueryHandler(
            pipeline_callback,
            pattern=r"^pipeline:",
        )
    )
    application.add_handler(
        CallbackQueryHandler(
            task_callback,
            pattern=r"^task:",
        )
    )
    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            pipeline_reply_capture,
        ),
        group=1,
    )

    application.add_handler(
        CallbackQueryHandler(
            approval_callback,
            pattern=r"^approval:",
        )
    )

    print("")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("🟢 ATLAS CONTROL BOT · В СЕТИ")
    print("🔐 Авторизация владельца · АКТИВНА")
    print("🔔 Notification Engine · READY")
    print("⚠️ Approval Inbox · READY")
    print("🛡 HTTP-логи · ЗАЩИЩЕНЫ")
    print("🇷🇺 Интерфейс · РУССКИЙ")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("⏹ Для остановки: Control + C")
    print("")

    application.run_polling(
        drop_pending_updates=False
    )


if __name__ == "__main__":
    main()
