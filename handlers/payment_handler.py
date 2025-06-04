from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import GROUP_ID
from keyboards.default.menu import main_menu

# To‘lov usullari tugmalari
def payment_methods_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("💳 Click", callback_data="pay_click"),
        InlineKeyboardButton("💰 Payme", callback_data="pay_payme")
    )
    keyboard.add(
        InlineKeyboardButton("🧾 Naqd to'lov", callback_data="pay_cash"),
        InlineKeyboardButton("🔙 Ortga", callback_data="main_menu")
    )
    return keyboard

# Buyurtma xabarini guruhga yuborish
async def send_order_to_group(bot, user, service_name):
    text = (
        f"📥 *Yangi buyurtma!*\n\n"
        f"👤 Foydalanuvchi: [{user.full_name}](tg://user?id={user.id})\n"
        f"🆔 ID: `{user.id}`\n"
        f"🔹 Xizmat turi: *{service_name}*"
    )
    await bot.send_message(chat_id=GROUP_ID, text=text, parse_mode="Markdown")

# To‘lov tugmalari orqali javob
async def handle_payment_request(message: types.Message):
    await message.answer(
        "💳 Iltimos, to‘lov turini tanlang. Quyidagi usullarda to‘lov qilishingiz mumkin:",
        reply_markup=payment_methods_keyboard()
    )

# Har bir xizmat uchun to‘lovni ko‘rsatish
async def show_service_payment_info(message: types.Message):
    service = message.text

    if service == "📄 Umra vizasi":
        text = (
            "🕋 *Umra vizasi* narxi: *160$*\n\n"
            "📌 Viza faqatgina Umra niyatidagilarga beriladi.\n"
            "⏱ Amal qilish muddati: 30 kun\n\n"
            "👉 To‘lovni amalga oshirish uchun quyidagi usullardan birini tanlang:"
        )
    elif service == "🌍 Turistik vizasi":
        text = (
            "🌐 *Turistik viza* narxi: *120$*\n\n"
            "📌 Saudiya Arabistoniga sayohat qilish uchun mos.\n"
            "✅ Amal qilish muddati: 90 kun\n\n"
            "👉 To‘lovni amalga oshirish uchun quyidagi usullardan foydalaning:"
        )
    elif service == "🌿 Ravza tashrif (Tasreh)":
        text = (
            "🕌 *Ravza tashrifi uchun Tasreh xizmatlari*\n\n"
            "📌 Agar sizda *viza orqali ruxsatnoma olinmagan* bo‘lsa:\n"
            "▫️ Narxi: *15 SAR*\n\n"
            "📌 Agar sizda *avval ruxsatnoma olingan bo‘lsa* va endi olish kerak bo‘lsa:\n"
            "▫️ Narxi: *20 SAR*\n\n"
            "💡 Narxlar shaxsiy yoki guruh asosida farq qilishi mumkin.\n\n"
            "👉 To‘lovni amalga oshirish uchun usulni tanlang:"
        )
    elif service == "🚅 Poezd chiptalari":
        text = (
            "🚄 *Haramain High Speed Train chiptalari*\n\n"
            "📍 Yo'nalishlar: Makkah ↔ Madinah ↔ Jidda\n"
            "📅 Sanani ayting – chiptalarni olib beramiz.\n"
            "💰 Narx: yo‘nalishga va sanaga qarab o‘zgaradi.\n\n"
            "👉 Iltimos, to‘lov uchun manager bilan bog‘laning:"
        )
        await message.answer(
            f"{text}\n\n📲 @vip_arabiy yoki @V001VB ga yozing.",
            reply_markup=main_menu
        )
        await send_order_to_group(message.bot, message.from_user, service)
        return
    elif service == "🏨 Mehmonxona/Hostel bron":
        text = (
            "🏨 *Mehmonxona yoki Hostel bron qilish xizmati*\n\n"
            "📍 Makkah va Madinahda joylashgan.\n"
            "💰 Narxlar mavsum va joylashuvga qarab farq qiladi.\n\n"
            "👉 Iltimos, manager bilan bog‘laning: @vip_arabiy yoki @V001VB"
        )
        await message.answer(text, reply_markup=main_menu)
        await send_order_to_group(message.bot, message.from_user, service)
        return
    elif service == "🍱 Guruh ovqatlanishi":
        text = (
            "🍛 *Guruh ovqatlanish xizmati*\n\n"
            "👥 Katta guruhlar uchun tushlik/kechki ovqat tashkil etiladi.\n"
            "📍 Manzil: Makkah yoki Madinah\n"
            "📆 Oldindan buyurtma berilishi kerak.\n\n"
            "👉 Batafsil uchun @vip_arabiy yoki @V001VB ga yozing."
        )
        await message.answer(text, reply_markup=main_menu)
        await send_order_to_group(message.bot, message.from_user, service)
        return
    elif service == "🚗 Transport xizmati":
        text = (
            "🚐 *Shaxsiy transport xizmati*\n\n"
            "📍 Makkah – Madinah – Jidda oraliq yo‘nalishlar\n"
            "🚖 VIP va odatiy variantlar mavjud\n"
            "💰 Narxlar yo‘nalish va transport turiga qarab belgilanadi.\n\n"
            "👉 @vip_arabiy yoki @V001VB ga yozing."
        )
        await message.answer(text, reply_markup=main_menu)
        await send_order_to_group(message.bot, message.from_user, service)
        return
    elif service == "🕋 Umra paketlari":
        text = (
            "🕋 *Umra paketlari – Barchasi bir joyda!*\n\n"
            "📌 Standart: 1100$ dan boshlanadi\n"
            "📌 VIP: 2000$ dan boshlanadi\n\n"
            "✅ Vizalar, mehmonxona, transport va Tasreh xizmatlari kiritilgan\n\n"
            "👉 Paketlar haqida ma'lumot va to‘lov uchun @vip_arabiy yoki @V001VB ga yozing."
        )
        await message.answer(text, reply_markup=main_menu)
        await send_order_to_group(message.bot, message.from_user, service)
        return
    else:
        await message.answer("🚧 Bu xizmat hali qo‘llab-quvvatlanmaydi.")
        return

    # Agar to‘lov usuli kerak bo‘lsa
    await message.answer(text, reply_markup=payment_methods_keyboard())
    await send_order_to_group(message.bot, message.from_user, service)
