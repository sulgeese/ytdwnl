import os
import asyncio
import logging

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import base_router


async def main():
    load_dotenv()
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)
    bot = Bot(os.environ.get("BOT_TOKEN"))
    dp = Dispatcher(bot=bot, storage=MemoryStorage())
    dp.include_router(base_router)

    URL = "https://www.youtube.com/watch?v=ZVkcjgTfLHU&ab_channel=NetflixAnime"

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())