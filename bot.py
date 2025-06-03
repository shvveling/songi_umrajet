from aiogram import Bot, Dispatcher, types, executor
from config import BOT_TOKEN
from services import start_menu, service_handlers
from handlers import register_handlers

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

# Boshlanish
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    text = (
        "🕋 <b>Assalomu alaykum!</b>\n\n"
        "Bu <b>UmraJet</b> xizmatlari botidir.\n"
        "Quyidagi xizmatlardan birini tanlang 👇"
    )
    await message.answer(text, reply_markup=start_menu())

# Register xizmatlar va callbacklar
service_handlers(dp, bot)
register_handlers(dp, bot)

if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
