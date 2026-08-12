import argparse
import asyncio
import html
from datetime import datetime
from pathlib import Path

from telegram import Bot
from telegram.constants import ParseMode
from telegram.error import InvalidToken, TelegramError


ENV_PATH = Path(__file__).with_name(".env")


TYPES = {
    "info": {
        "emoji": "🔵",
        "label": "ИНФОРМАЦИЯ",
    },
    "success": {
        "emoji": "🟢",
        "label": "УСПЕШНО",
    },
    "warning": {
        "emoji": "🟡",
        "label": "ТРЕБУЕТ ВНИМАНИЯ",
    },
    "critical": {
        "emoji": "🔴",
        "label": "КРИТИЧЕСКОЕ СОБЫТИЕ",
    },
    "finance": {
        "emoji": "💰",
        "label": "ФИНАНСЫ",
    },
    "opportunity": {
        "emoji": "💼",
        "label": "НОВАЯ ВОЗМОЖНОСТЬ",
    },
    "approval": {
        "emoji": "⚠️",
        "label": "ТРЕБУЕТСЯ РЕШЕНИЕ",
    },
}


def load_env():
    values = {}

    for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()

        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        values[key.strip()] = value.strip()

    return values


def build_message(notification_type, title, message):
    config = TYPES[notification_type]

    emoji = config["emoji"]
    label = config["label"]

    safe_title = html.escape(title)
    safe_message = html.escape(message)

    now = datetime.now().strftime("%H:%M")

    return (
        f"{emoji} <b>ATLAS · {label}</b>\n\n"
        "━━━━━━━━━━━━━━━━━━\n\n"

        f"📌 <b>{safe_title}</b>\n\n"
        f"{safe_message}\n\n"

        "━━━━━━━━━━━━━━━━━━\n"
        f"🕐 {now}\n\n"

        "<i>Atlas Control · Notification Engine v0.1</i>"
    )


async def send_notification(notification_type, title, message):
    if notification_type not in TYPES:
        raise ValueError(f"Неизвестный тип уведомления: {notification_type}")

    env = load_env()

    token = env.get("TELEGRAM_BOT_TOKEN", "").strip()

    owner_ids = [
        int(x.strip())
        for x in env.get("TELEGRAM_OWNER_IDS", "").split(",")
        if x.strip().isdigit()
    ]

    if not token:
        print("❌ TELEGRAM_BOT_TOKEN отсутствует")
        return False

    if not owner_ids:
        print("❌ TELEGRAM_OWNER_IDS отсутствует")
        return False

    text = build_message(
        notification_type,
        title,
        message,
    )

    try:
        async with Bot(token=token) as bot:
            for owner_id in owner_ids:
                await bot.send_message(
                    chat_id=owner_id,
                    text=text,
                    parse_mode=ParseMode.HTML,
                )

    except InvalidToken:
        print("❌ Telegram отклонил Bot Token")
        print("🔐 Значение токена скрыто")
        return False

    except TelegramError:
        print("❌ Ошибка Telegram API")
        print("🔐 Секретные данные не выводятся")
        return False

    print("✅ Atlas Notification отправлено")
    print(f"📨 Тип: {notification_type}")
    print(f"👤 Получателей: {len(owner_ids)}")
    print("🔐 Секретные данные не выводились")

    return True


async def main():
    parser = argparse.ArgumentParser(
        description="Atlas Notification Engine"
    )

    parser.add_argument(
        "--type",
        choices=TYPES.keys(),
        required=True,
    )

    parser.add_argument(
        "--title",
        required=True,
    )

    parser.add_argument(
        "--message",
        required=True,
    )

    args = parser.parse_args()

    await send_notification(
        args.type,
        args.title,
        args.message,
    )


if __name__ == "__main__":
    asyncio.run(main())
