import asyncio

from telegram import Bot
from telegram.constants import ParseMode

from bot import BOT_TOKEN, OWNER_IDS
from owner_report import render_owner_report_html


async def send_owner_report():
    report = render_owner_report_html()

    async with Bot(token=BOT_TOKEN) as bot:
        sent = 0

        for owner_id in OWNER_IDS:
            await bot.send_message(
                chat_id=owner_id,
                text=report,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
            )
            sent += 1

    print("✅ Atlas Owner Report отправлен")
    print(f"👤 Получателей: {sent}")
    print("🔐 Bot Token не выводился")

    return sent


async def main():
    await send_owner_report()


if __name__ == "__main__":
    asyncio.run(main())
