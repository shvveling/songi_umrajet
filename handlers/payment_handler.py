from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data.config import MANAGERS

# To'lov usullari haqida inline tugma
def get_payment_options():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("💳 Click / Payme orqali to'lov", url="https://t.me/vip_arabiy"),
        InlineKeyboardButton("📞 To'lov bo'yicha manager bilan bog'lanish", url="https://t.me/V001VB")
    )
    return markup

# To'lov haqida malumot
async def payment_info(message: types.Message):
    text = (
        "📌 <b>To'lov haqida</b>\n\n"
        "Siz tanlagan xizmat uchun to'lovni quyidagi usullar orqali amalga oshirishingiz mumkin:\n\n"
        "💳 Click / Payme\n"
        "🏦 Bank o‘tkazmasi\n"
        "🤝 Naqd yoki karta orqali ofisda\n\n"
        "To'lov haqida batafsil ma'lumot yoki to'lov qilish uchun pastdagi tugmalar orqali managerlarimizga murojaat qiling."
    )
    await message.answer(text, reply_markup=get_payment_options(), parse_mode="HTML")

def register_payment_handler(dp: Dispatcher):
    dp.register_message_handler(payment_info, lambda message: "to'lov" in message.text.lower())
