import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import user

import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Routers
dp.include_router(user.user_router)

# Start command handler
@dp.message(Command("start"))
async def send_welcome(message):
    await message.answer("Xush kelibsiz! /start buyrug‘ini qayta bosing.")

if __name__ == "__main__":
    import asyncio
    asyncio.run(dp.start_polling(bot))
