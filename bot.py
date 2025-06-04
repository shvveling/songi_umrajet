import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
import os

# .env fayldan o'zgaruvchilarni yuklash
load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")
GROUP_ID = int(os.getenv("GROUP_ID"))

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Handlerlarni import qilish
from handlers import start_handler, services_handler, payment_handler, admin_handler

# Handlerlarni ro'yxatdan o'tkazish
start_handler.register_handlers(dp)
services_handler.register_handlers(dp)
payment_handler.register_handlers(dp)
admin_handler.register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
