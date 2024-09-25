import sys
import logging
import asyncio

from aiogram import Bot, Dispatcher

from src.app.settings import load_config
from src.app.user.handler import router as user_router

config = load_config()

bot = Bot(config.tg_bot.token)
dp = Dispatcher()
dp.include_routers(user_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exit")
