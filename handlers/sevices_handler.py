from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# --- Xizmat tugmalari ---
def get_services_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("🧳 Umra paketlari", callback_data="umra_packages"),
        InlineKeyboardButton("🛂 Umra vizasi ($160)", callback_data="umra_visa"),
        InlineKeyboardButton("🧾 Turist vizasi ($120)", callback_data="tourist_visa"),
        InlineKeyboardButton("🏨 Mehmonxona & Hostel", callback_data="hotel_booking"),
        InlineKeyboardButton("🚌 Transfer xizmatlari", callback_data="transfer_service"),
        InlineKeyboardButton("📄 Tasreh (Rawdah ruxsatnomasi)", callback_data="tasreh"),
        InlineKeyboardButton("🚅 Poezd chiptalari (HHR)", callback_data="train_tickets"),
        InlineKeyboardButton("🍽 Guruh ovqatlanish", callback_data="group_meals"),
    )
    return keyboard

# --- Xizmatlar haqida malumotlar ---
async def handle_services(callback_query: types.CallbackQuery):
    data = callback_query.data

    if data == "umra_packages":
        msg = (
            "🧳 <b>Umra paketlari</b>\n"
            "• Oddiy Umra: <b>1100$</b> dan boshlanadi\n"
            "• VIP Umra: <b>2000$</b> dan\n\n"
            "📦 Paket ichida: vizalar, mehmonxona, transfer, tasreh, ovqatlanish va boshqalar\n"
            "To‘liq ma'lumot uchun menejerga yozing: @vip_arabiy yoki @V001VB"
        )

    elif data == "umra_visa":
        msg = (
            "🛂 <b>Umra vizasi</b>\n"
            "Narxi: <b>160$</b>\n"
            "Vaqti: 2-5 ish kuni\n"
            "Kafolat: 100%\n"
            "Murojaat uchun: @vip_arabiy yoki @V001VB"
        )

    elif data == "tourist_visa":
        msg = (
            "🧾 <b>Turistik vizalar</b>\n"
            "Narxi: <b>120$</b>\n"
            "Amal qilish muddati: 1 yilgacha\n"
            "Shaxsiy va ishbilarmonlik maqsadlar uchun\n"
            "Murojaat uchun: @vip_arabiy yoki @V001VB"
        )

    elif data == "hotel_booking":
        msg = (
            "🏨 <b>Mehmonxona & Hostel bron qilish</b>\n"
            "• Makkada va Madinada qulay joylashuv\n"
            "• Guruh yoki yakka mijozlar uchun\n"
            "• Narxlar bozor holatiga qarab belgilanadi\n"
            "📝 Batafsil: @vip_arabiy yoki @V001VB"
        )

    elif data == "transfer_service":
        msg = (
            "🚌 <b>Transfer xizmatlari</b>\n"
            "• Aeroport ↔ Mehmonxona\n"
            "• Makkah ↔ Madinah\n"
            "• Shaxsiy yoki umumiy\n"
            "🚗 Yangi va qulay transport\n"
            "📌 @vip_arabiy yoki @V001VB orqali buyurtma bering"
        )

    elif data == "tasreh":
        msg = (
            "📄 <b>Tasreh - Rawdah ruxsatnomasi</b>\n"
            "• Agar <b>oldin ro‘yxatdan o‘tilmagan</b> va viza berilgan bo‘lsa: <b>15 SAR</b>\n"
            "• Agar viza yo‘q yoki oldin ruxsatnoma olingan bo‘lsa: <b>20 SAR</b>\n"
            "• Guruh bo‘yicha chegirmalar mavjud\n"
            "💬 Batafsil: @vip_arabiy yoki @V001VB"
        )

    elif data == "train_tickets":
        msg = (
            "🚅 <b>Poezd chiptalari (HHR Train)</b>\n"
            "Yo‘nalishlar: Makkah, Madinah, KAIA, KAEC va boshqa stansiyalar\n"
            "Narx va jadval: mavjud holatga qarab\n"
            "📤 Buyurtma: @vip_arabiy yoki @V001VB"
        )

    elif data == "group_meals":
        msg = (
            "🍽 <b>Guruh ovqatlanish xizmati</b>\n"
            "• Nonushta, tushlik, kechki ovqat\n"
            "• Halol, sifatli va pokiza\n"
            "• Menyular moslashtiriladi\n"
            "🥘 Buyurtma: @vip_arabiy yoki @V001VB"
        )

    else:
        msg = "Xizmat topilmadi. Iltimos, boshqatdan urinib ko‘ring."

    await callback_query.message.edit_text(msg, parse_mode="HTML")


def register_services(dp: Dispatcher):
    dp.register_callback_query_handler(handle_services, lambda c: c.data in [
        "umra_packages", "umra_visa", "tourist_visa", "hotel_booking",
        "transfer_service", "tasreh", "train_tickets", "group_meals"
    ])
