import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand

from dotenv import load_dotenv
load_dotenv()

from admin import register_admin_handlers
from handlers.user import register_user_handlers

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN .env faylda topilmadi!")

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

async def set_commands():
    commands = [
        BotCommand(command="start", description="✨ Botni ishga tushirish"),
        BotCommand(command="admin", description="🔒 Admin panel"),
    ]
    await bot.set_my_commands(commands)

async def main():
    logging.basicConfig(level=logging.INFO)
    print("✅ UmraJetBot ishga tushdi!")

    await set_commands()

    register_admin_handlers(dp)
    register_user_handlers(dp)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
