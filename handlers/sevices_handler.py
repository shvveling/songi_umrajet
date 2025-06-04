from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp

# Xizmatlar tugmalari
services_menu = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton("🎫 Umra va Turist Vizalari", callback_data="visa"),
    InlineKeyboardButton("🏨 Mehmonxona va Hostel", callback_data="hotel"),
    InlineKeyboardButton("🚌 Transport Xizmatlari", callback_data="transport"),
    InlineKeyboardButton("🕌 Rawdah Tashrif (Tasreh)", callback_data="tasreh"),
    InlineKeyboardButton("🚄 Poezd Chiptalari", callback_data="train"),
    InlineKeyboardButton("🍽️ Guruh Ovqatlanishi", callback_data="meals"),
    InlineKeyboardButton("🎁 Umra Paketlari", callback_data="packages"),
)

@dp.message_handler(text="📋 Xizmatlar")
async def show_services(msg: types.Message):
    await msg.answer(
        "<b>📋 Bizning Umra xizmatlarimiz:</b>\n\n"
        "Xizmat turini tanlang. Har bir xizmat bo’yicha to’liq ma’lumot beriladi.\n"
        "Xizmatni tanlaganingizdan so’ng, buyurtmani bot orqali to’g’ridan-to’g’ri managerga yuborishingiz mumkin ✅",
        reply_markup=services_menu
    )

# Visa
@dp.callback_query_handler(lambda c: c.data == "visa")
async def visa_info(call: types.CallbackQuery):
    await call.message.answer(
        "<b>🎫 Umra va Turist Vizalari</b>\n\n"
        "📌 Turist vizasi – <b>120$</b>\n"
        "📌 Umra vizasi – <b>160$</b>\n\n"
        "🕐 Viza tayyorlash muddati: 1-3 ish kuni\n"
        "✅ Pasport nusxasi kifoya\n"
        "☎️ Managerlarimiz sizga tez orada aloqaga chiqadi."
    )
    await call.answer()

# Hotel
@dp.callback_query_handler(lambda c: c.data == "hotel")
async def hotel_info(call: types.CallbackQuery):
    await call.message.answer(
        "<b>🏨 Mehmonxona va Hostel band qilish</b>\n\n"
        "📍 Makkada, Madinada va boshqa shaharlar bo’yicha arzon narxlarda.\n"
        "⭐ 3-4-5 yulduzli mehmonxonalar\n"
        "💤 Hostel variantlari ham mavjud\n"
        "🗓️ Sanalarni ayting, biz takliflar bilan chiqamiz!"
    )
    await call.answer()

# Transport
@dp.callback_query_handler(lambda c: c.data == "transport")
async def transport_info(call: types.CallbackQuery):
    await call.message.answer(
        "<b>🚌 Transport xizmatlari</b>\n\n"
        "🚐 Airport pickup/drop (Jidda, Madina)\n"
        "🛻 Shaharlararo safarlar (Makka ↔ Madina)\n"
        "👥 Guruh va individual transport mavjud\n"
        "🔁 Kunlik/soatlik ijaralar ham bor"
    )
    await call.answer()

# Tasreh (Rawdah)
@dp.callback_query_handler(lambda c: c.data == "tasreh")
async def tasreh_info(call: types.CallbackQuery):
    await call.message.answer(
        "<b>🕌 Rawdah tashrifi (Tasreh)</b>\n\n"
        "⛔️ Dastlabki vizangiz orqali Rawdah tashrifi qilinmagan bo‘lishi kerak.\n\n"
        "✅ Viza mavjud bo‘lsa – <b>15 SAR</b>\n"
        "⛔️ Vizasiz bo‘lsa – <b>20 SAR</b>\n\n"
        "📍 Guruhlar uchun chegirmalar mavjud.\n"
        "📆 Sana va ismlarni yuboring – joy band qilamiz."
    )
    await call.answer()

# Train
@dp.callback_query_handler(lambda c: c.data == "train")
async def train_info(call: types.CallbackQuery):
    await call.message.answer(
        "<b>🚄 HHR Poezd chiptalari</b>\n\n"
        "📌 Yo‘nalishlar:\n"
        "— Makka ↔ Madina\n"
        "— Makka ↔ Jidda Airport\n"
        "— Madina ↔ Jidda Airport\n\n"
        "💺 Comfort va Business class\n"
        "🗓️ Sana va yo‘nalishni yuboring — tezkor band qilish!"
    )
    await call.answer()

# Meals
@dp.callback_query_handler(lambda c: c.data == "meals")
async def meals_info(call: types.CallbackQuery):
    await call.message.answer(
        "<b>🍽️ Guruh ovqatlanishi</b>\n\n"
        "👨‍👩‍👧‍👦 Guruh va oilaviy ovqatlar\n"
        "🍛 Nonushta, tushlik, kechki ovqat variantlari\n"
        "📦 Yetkazib beriladi (delivery)\n"
        "📅 Sana va kishi sonini ayting – narxlarni taklif qilamiz"
    )
    await call.answer()

# Packages
@dp.callback_query_handler(lambda c: c.data == "packages")
async def packages_info(call: types.CallbackQuery):
    await call.message.answer(
        "<b>🎁 Umra Paketlari</b>\n\n"
        "🔹 <b>Standard:</b> $1100 dan\n"
        "🔸 <b>VIP:</b> $2000 dan\n\n"
        "✅ Viza, mehmonxona, transport, tashriflar, ovqatlar hammasi ichida.\n"
        "👤 Yakka yoki guruh uchun\n"
        "📆 Sana va kishilar sonini yuboring – to‘liq paket jo‘natamiz"
    )
    await call.answer()


def register_services_handlers(dp: Dispatcher):
    dp.register_message_handler(show_services, text="📋 Xizmatlar")
