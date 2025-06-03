import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import Message
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message()
async def start_handler(message: Message):
    await message.answer(
        "<b>Assalomu alaykum!</b>\n\n"
        "Bu <b>UmraJet</b> xizmatlari botidir. Xizmatlarimizdan foydalanish uchun menyudan tanlang.\n\n"
        "📲 @vip_arabiy\n📲 @V001VB\n🔗 Bot: @umrajet_bot\n📣 Kanal: @umrajet, @the_ravza"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
