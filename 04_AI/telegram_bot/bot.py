import os
import html
import logging
from datetime import datetime

from telegram import Update, BotCommand
from telegram.constants import ParseMode
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

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not authorized(update):
        await deny_access(update)
        return

    now = datetime.now().strftime("%H:%M:%S")

    text = (
        "🟢 <b>ATLAS LAB · СОСТОЯНИЕ СИСТЕМЫ</b>\n\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "🧠 <b>Система</b>\n"
        "Статус: 🟢 РАБОТАЕТ\n"
        "Режим: 👤 КОНТРОЛЬ ВЛАДЕЛЬЦА\n\n"
        "🤖 <b>AI Operations</b>\n"
        "Telegram Gateway: 🟢 В СЕТИ\n"
        "Atlas Control Bot: 🟢 АКТИВЕН\n"
        "Notification Engine: 🟢 АКТИВЕН\n"
        "Approval Inbox: 🟢 MVP\n\n"
        "🔐 <b>Безопасность</b>\n"
        "Авторизация владельца: ✅ АКТИВНА\n"
        "Политика доступа: 🔒 ТОЛЬКО ВЛАДЕЛЬЦЫ\n\n"
        "📡 <b>Инфраструктура</b>\n"
        "Python: 🟢 3.13\n"
        "Интерфейс: 🟢 Telegram\n"
        "Среда: 💻 Локальный Atlas Lab\n\n"
        "━━━━━━━━━━━━━━━━━━\n"
        f"🕐 Обновлено: {now}\n\n"
        "<i>Atlas Control · v0.2</i>"
    )

    await update.effective_message.reply_text(
        text,
        parse_mode=ParseMode.HTML,
    )


# ─────────────────────────────────────────────
# /HELP
# ─────────────────────────────────────────────

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not authorized(update):
        await deny_access(update)
        return

    text = (
        "🤖 <b>ATLAS · КОМАНДНЫЙ ЦЕНТР</b>\n\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "🏠 /start — центр управления\n"
        "📊 /status — состояние Atlas\n"
        "❓ /help — список команд\n\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "🟢 <b>Активные возможности</b>\n\n"
        "🔔 Системные уведомления\n"
        "⚠️ Approval Inbox\n"
        "🔐 Owner Authentication\n\n"
        "🔜 <b>Следующие этапы</b>\n\n"
        "💼 Возможности и клиенты\n"
        "💰 Финансы\n"
        "🧠 Аналитика\n"
        "🛡 Безопасность\n\n"
        "<i>Atlas Control · v0.2</i>"
    )

    await update.effective_message.reply_text(
        text,
        parse_mode=ParseMode.HTML,
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

    if action == "details":
        await query.answer()

        await query.message.reply_text(
            "📋 <b>ATLAS · ДЕТАЛИ РЕШЕНИЯ</b>\n\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            f"🔖 ID: <code>{html.escape(approval_id)}</code>\n\n"
            "🤖 <b>Почему Atlas запрашивает решение</b>\n"
            "Действие выходит за рамки полностью "
            "автоматизированных полномочий и требует "
            "подтверждения владельца.\n\n"
            "🛡 <b>Политика</b>\n"
            "Без подтверждения действие выполнено не будет.\n\n"
            "━━━━━━━━━━━━━━━━━━\n"
            "<i>Atlas Approval Inbox · v0.1</i>",
            parse_mode=ParseMode.HTML,
        )

        return

    if action == "approve":
        await query.answer("✅ Решение подтверждено")

        await query.edit_message_reply_markup(reply_markup=None)

        await query.message.reply_text(
            "✅ <b>ATLAS · РЕШЕНИЕ ПРИНЯТО</b>\n\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            f"🔖 ID: <code>{html.escape(approval_id)}</code>\n"
            "Статус: 🟢 <b>ПОДТВЕРЖДЕНО</b>\n\n"
            "🤖 Atlas получил разрешение владельца.\n\n"
            "━━━━━━━━━━━━━━━━━━\n"
            "<i>Atlas Approval Inbox</i>",
            parse_mode=ParseMode.HTML,
        )

        return

    if action == "reject":
        await query.answer("❌ Действие отклонено")

        await query.edit_message_reply_markup(reply_markup=None)

        await query.message.reply_text(
            "❌ <b>ATLAS · ДЕЙСТВИЕ ОТКЛОНЕНО</b>\n\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            f"🔖 ID: <code>{html.escape(approval_id)}</code>\n"
            "Статус: 🔴 <b>ОТКЛОНЕНО</b>\n\n"
            "🛑 Atlas не будет выполнять это действие.\n\n"
            "━━━━━━━━━━━━━━━━━━\n"
            "<i>Atlas Approval Inbox</i>",
            parse_mode=ParseMode.HTML,
        )

        return

    await query.answer("Неизвестное действие.")


# ─────────────────────────────────────────────
# TELEGRAM MENU
# ─────────────────────────────────────────────

async def post_init(application: Application):
    await application.bot.set_my_commands(
        [
            BotCommand("start", "🏠 Центр управления"),
            BotCommand("status", "📊 Состояние Atlas"),
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
    application.add_handler(CommandHandler("help", help_command))

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
