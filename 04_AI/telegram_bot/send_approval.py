import asyncio
from pathlib import Path

from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode


ENV_PATH = Path(__file__).with_name(".env")


def load_env():
    values = {}

    for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()

        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        values[key.strip()] = value.strip()

    return values


async def main():
    env = load_env()

    token = env.get("TELEGRAM_BOT_TOKEN", "").strip()

    owner_ids = [
        int(x.strip())
        for x in env.get("TELEGRAM_OWNER_IDS", "").split(",")
        if x.strip().isdigit()
    ]

    if not token or not owner_ids:
        print("❌ Не найдены Telegram настройки")
        return

    approval_id = "TEST-001"

    text = (
        "⚠️ <b>ATLAS · ТРЕБУЕТСЯ РЕШЕНИЕ</b>\n\n"
        "━━━━━━━━━━━━━━━━━━\n\n"

        "📨 <b>Действие</b>\n"
        "Отправить коммерческое предложение\n\n"

        "🏢 <b>Компания</b>\n"
        "Example GmbH 🇩🇪\n\n"

        "💰 <b>Сумма предложения</b>\n"
        "€3 500\n\n"

        "🎯 <b>Причина</b>\n"
        "Компания соответствует целевому профилю и имеет "
        "потенциальную потребность в автоматизации клиентской поддержки.\n\n"

        "🤖 <b>Оценка Atlas</b>\n"
        "Уверенность: 87%\n"
        "Риск: 🟢 НИЗКИЙ\n\n"

        "🔐 <b>Политика</b>\n"
        "Без решения владельца действие выполнено не будет.\n\n"

        "━━━━━━━━━━━━━━━━━━\n"
        f"🔖 ID: <code>{approval_id}</code>\n\n"

        "<i>Atlas Approval Inbox · v0.1</i>"
    )

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
            )
        ],
    ])

    async with Bot(token=token) as bot:
        for owner_id in owner_ids:
            await bot.send_message(
                chat_id=owner_id,
                text=text,
                parse_mode=ParseMode.HTML,
                reply_markup=keyboard,
            )

    print("✅ Тестовый Approval отправлен")
    print(f"👤 Получателей: {len(owner_ids)}")
    print(f"🔖 Approval ID: {approval_id}")
    print("🛡 Реальное действие за этим тестом НЕ выполняется")


if __name__ == "__main__":
    asyncio.run(main())
