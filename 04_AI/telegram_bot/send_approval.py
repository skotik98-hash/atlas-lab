import asyncio
from datetime import datetime
from pathlib import Path

from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode

from approval_store import create_approval


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

    approval_id = datetime.now().strftime(
        "TEST-%Y%m%d-%H%M%S-%f"
    )

    created = create_approval(
        approval_id=approval_id,
        title="Отправить коммерческое предложение",
        action_type="COMMERCIAL_PROPOSAL",
        details=(
            "Тестовый запрос: отправить коммерческое предложение "
            "Example GmbH на сумму €3 500."
        ),
    )

    if not created:
        print("❌ Approval с таким ID уже существует")
        return

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
        "потенциальную потребность в автоматизации "
        "клиентской поддержки.\n\n"

        "🤖 <b>Оценка Atlas</b>\n"
        "Уверенность: 87%\n"
        "Риск: 🟢 НИЗКИЙ\n\n"

        "🔐 <b>Политика</b>\n"
        "Без решения владельца действие выполнено не будет.\n\n"

        "━━━━━━━━━━━━━━━━━━\n"
        f"🔖 ID: <code>{approval_id}</code>\n"
        "📊 Статус: 🟡 <b>PENDING</b>\n\n"

        "<i>Atlas Approval Inbox · v0.2</i>"
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
            ),
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

    print("✅ Новый Approval создан и отправлен")
    print(f"🔖 Approval ID: {approval_id}")
    print("📊 Начальный статус: PENDING")
    print(f"👤 Получателей: {len(owner_ids)}")
    print("🛡 Реальное внешнее действие НЕ выполняется")


if __name__ == "__main__":
    asyncio.run(main())
