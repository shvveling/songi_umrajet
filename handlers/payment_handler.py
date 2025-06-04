from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def payment_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("📞 Menejer: @vip_arabiy", url="https://t.me/vip_arabiy"),
        InlineKeyboardButton("📞 Menejer: @V001VB", url="https://t.me/V001VB"),
    )
    return keyboard

async def payment_handler(message: types.Message):
    text = (
        "💳 *To‘lov usullari*:\n\n"
        "✅ Uzcard — O‘zbekistonda keng tarqalgan va ishonchli to‘lov kartasi.\n"
        "✅ Humo — Zamonaviy, tez va xavfsiz to‘lovlar uchun.\n"
        "✅ Visa / Mastercard — Butun dunyo bo‘ylab qabul qilinadigan xalqaro kartalar.\n"
        "✅ Kripto valyutalar — Bitcoin, Ethereum va boshqalar, zamonaviy va innovatsion to‘lov usullari.\n\n"
        "📈 *Narxlar haqida qisqacha*:\n"
        "• Umra vizasi — 160 USD / dona\n"
        "• Turist vizasi — 120 USD / dona\n"
        "• Ravza tasreh xizmati —\n"
        "    - Agar viza mavjud bo‘lsa: 15 SAR / dona\n"
        "    - Agar viza mavjud bo‘lmasa: 20 SAR / dona\n\n"
        "🔔 *Eslatma:* Ravza tasreh uchun viza oldin ro‘yxatdan o‘tgan va ruhsatnoma olganlarga taqdim etiladi. "
        "Agar viza olinmagan bo‘lsa, narx biroz yuqoriroq bo‘ladi.\n\n"
        "• Umra paketlari — 1100 USD dan boshlanadi, VIP paketlar esa 2000 USD dan.\n"
        "• Boshqa xizmatlar (poezd biletlar, transport, mehmonxona, guruhlar uchun ovqat) narxlari individual so‘rov asosida belgilanadi.\n\n"
        "To‘lov va xizmatlar bo‘yicha savollaringiz bo‘lsa, iltimos, quyidagi menejerlar bilan bog‘laning:"
    )
    await message.answer(text, reply_markup=payment_keyboard(), parse_mode="Markdown")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(payment_handler, lambda m: m.text == "💳 To‘lovlar")
