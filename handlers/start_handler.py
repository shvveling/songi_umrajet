from aiogram import types, Dispatcher

async def cmd_start(message: types.Message):
    text = (
        "👋 Assalomu alaykum!\n\n"
        "UmraJet botiga xush kelibsiz!\n\n"
        "Sizga Umra va Turistik vizalar, Ravza tasreh, Mehmonxona, Transport, "
        "Poezd biletlar, Guruhlar uchun ovqat va boshqa ko'plab xizmatlarni taqdim etamiz.\n\n"
        "Quyidagi bo‘limlardan birini tanlang:"
    )
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("🛂 Viza xizmati", "🕌 Ravza tasreh xizmati")
    keyboard.add("🏨 Mehmonxona", "🚆 Po'ezd biletlar")
    keyboard.add("🚗 Transport", "🍽️ Guruhlar uchun ovqat")
    keyboard.add("💳 To‘lovlar")
    
    await message.answer(text, reply_markup=keyboard)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start", "help"])
