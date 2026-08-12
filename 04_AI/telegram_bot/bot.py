import os
import html
import logging
from datetime import datetime

from telegram import Update, BotCommand, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from atlas_status import get_atlas_status
from activity_store import list_events
from owner_report import render_owner_report_html

from approval_store import (
    get_approval,
    decide_approval,
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

        "━━━━━━━━━━━━━━━━━━\n"
        f"🕐 Обновлено: {now}\n\n"

        "<i>Atlas Control · Live Status v0.5</i>"
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

    events = [
        event
        for event in raw_events
        if event["event_type"] not in hidden_types
    ][:10]

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
        "<i>Atlas Activity Feed · v0.3</i>",
    ])

    await update.effective_message.reply_text(
        "\n".join(parts),
        parse_mode=ParseMode.HTML,
    )


# ─────────────────────────────────────────────
# /APPROVALS
# ─────────────────────────────────────────────

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

    result = decide_approval(
        approval_id=approval_id,
        decision=decision,
        decided_by=user.id,
    )

    if result == "NOT_FOUND":
        await query.answer(
            "❌ Approval не найден.",
            show_alert=True,
        )
        return

    if result == "ALREADY_DECIDED":
        current = get_approval(approval_id)

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

    if result == "APPROVED":
        await query.answer("✅ Решение подтверждено")

        await query.message.reply_text(
            "✅ <b>ATLAS · РЕШЕНИЕ ЗАРЕГИСТРИРОВАНО</b>\n\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            f"🔖 ID: <code>{html.escape(approval_id)}</code>\n"
            "Статус: 🟢 <b>ПОДТВЕРЖДЕНО</b>\n\n"
            "👤 Решение владельца сохранено в Approval Store.\n\n"
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
            BotCommand("approvals", "⚠️ Approval Inbox"),
            BotCommand("pending", "🟡 Ожидают решения"),
            BotCommand("help", "❓ Команды"),
        ]
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
    application.add_handler(CommandHandler("approvals", approvals_command))
    application.add_handler(CommandHandler("pending", pending_command))

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
