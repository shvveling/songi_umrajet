import os
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, BotCommand
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv

# --- 1. TOKEN YUKLASH ---
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("❌ BOT_TOKEN topilmadi! Iltimos .env faylni tekshiring.")

# --- 2. ADMIN MA'LUMOTLARI ---
MANAGER_RAVZA = "@vip_arabiy"
MANAGER_ASSISTANT = "@V001VB"

# --- 3. START KOMANDASI ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("🍇 Ravza tashrifi"), KeyboardButton("🕋 Umra paketlari")],
        [KeyboardButton("🏨 Mehmonxona / Hostel"), KeyboardButton("🚄 Poezd chiptalari")],
        [KeyboardButton("🚐 Transport xizmati"), KeyboardButton("🍽 Guruh ovqatlari")],
        [KeyboardButton("✈️ Avia chiptalar"), KeyboardButton("📞 Admin bilan bog‘lanish")],
        [KeyboardButton("📢 Rasmiy kanallar")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "🤍 *UmraJet — Premium Umra xizmatlari markazi* 🤍\n\n"
        "Tanlang va buyurtma bering, biz siz uchun barcha ishni qilamiz!",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

# --- 4. XIZMAT FUNKSIYALARI ---
async def send_service_message(update: Update, text: str):
    await update.message.reply_text(text, parse_mode="Markdown")

async def ravza_service(update, context):
    text = (
        "🍇 *Ravza tashrifi — Ilohiy iltijo va ruhiy yangilanish!* ✨\n\n"
        "🔹 Viza bilan — 15 SAR\n"
        "🔹 Vizasiz — 20 SAR\n\n"
        "📌 Guruhli va yakka tartibda tashrif\n"
        "📄 Hujjat: rasm yoki PDF\n"
        "💳 To‘lov: Uzcard, Humo, Visa, Crypto\n\n"
        f"📞 Bog‘lanish: {MANAGER_RAVZA} | {MANAGER_ASSISTANT}"
    )
    await send_service_message(update, text)

async def umra_packages(update, context):
    text = (
        "🕋 *Umra paketlari — Orzu emas, haqiqat!* 🌙\n\n"
        "✨ *Standard paket:* $1100\n"
        "✨ *VIP paket:* $2000\n\n"
        "✅ Vizalar\n✅ Mehmonxona\n✅ Transport\n✅ Gid xizmati\n✅ Ovqat\n\n"
        f"📞 Buyurtma: {MANAGER_ASSISTANT} | {MANAGER_RAVZA}"
    )
    await send_service_message(update, text)

async def hotels(update, context):
    text = (
        "🏨 *Mehmonxona va Hostel xizmati* 🛏\n\n"
        "📍 Makka va Madina markazida\n"
        "🍽 Ovqatli/ovqatsiz\n"
        "🔐 Xavfsiz va qulay joylar\n\n"
        f"📞 Bog‘lanish: {MANAGER_ASSISTANT} | {MANAGER_RAVZA}"
    )
    await send_service_message(update, text)

async def train_tickets(update, context):
    text = (
        "🚄 *Poezd chiptalari — HHR liniyasi* 🚅\n\n"
        "📍 Makka ↔ Madina\n"
        "🗓 Sana: istalgan kun\n"
        "💺 Joy: Ekanom yoki Biznes\n\n"
        f"📞 Buyurtma: {MANAGER_ASSISTANT}"
    )
    await send_service_message(update, text)

async def transport(update, context):
    text = (
        "🚐 *Transport xizmati — xavfsiz va qulay* 🚘\n\n"
        "🚍 VIP avtomobillar, Toyota, avtobuslar\n"
        "🕌 Masjidlar, aeroportlar uchun\n"
        "👨‍✈️ Tajribali haydovchilar\n\n"
        f"📞 Yozing: {MANAGER_ASSISTANT}"
    )
    await send_service_message(update, text)

async def group_food(update, context):
    text = (
        "🍽 *Guruh ovqatlari — 10+ kishilik buyurtmalar* 🍛\n\n"
        "🥘 O‘zbek taomlari\n"
        "🍱 1, 2, 3 mahal menyular\n"
        "🎉 Maxsus ziyofatlar uchun\n\n"
        f"📞 Buyurtma uchun: {MANAGER_ASSISTANT}"
    )
    await send_service_message(update, text)

async def plane_tickets(update, context):
    text = (
        "✈️ *Avia chiptalar — dunyo bo‘ylab* 🌍\n\n"
        "📆 Istalgan sanaga\n"
        "🛂 Vizali/vizasiz variantlar\n\n"
        f"📞 So‘rov uchun: {MANAGER_ASSISTANT}"
    )
    await send_service_message(update, text)

async def contact_admin(update, context):
    text = (
        "📞 *Adminlar bilan bog‘lanish:*\n\n"
        f"🍇 Ravza xizmatlari: {MANAGER_RAVZA}\n"
        f"🕋 Umra va umumiy xizmatlar: {MANAGER_ASSISTANT}"
    )
    await send_service_message(update, text)

async def official_channels(update, context):
    text = (
        "📢 *Rasmiy Telegram kanallar:*\n\n"
        "🔗 @umrajet — e’lonlar va yangiliklar\n"
        "🔗 @the_ravza — Ravza haqida ma’lumotlar\n\n"
        f"📞 Savollar uchun: {MANAGER_RAVZA}"
    )
    await send_service_message(update, text)

# --- 5. XIZMATLAR XARITASI ---
service_map = {
    "🍇 Ravza tashrifi": ravza_service,
    "🕋 Umra paketlari": umra_packages,
    "🏨 Mehmonxona / Hostel": hotels,
    "🚄 Poezd chiptalari": train_tickets,
    "🚐 Transport xizmati": transport,
    "🍽 Guruh ovqatlari": group_food,
    "✈️ Avia chiptalar": plane_tickets,
    "📞 Admin bilan bog‘lanish": contact_admin,
    "📢 Rasmiy kanallar": official_channels,
}

# --- 6. FOYDALANUVCHI XABARINI QABUL QILISH ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    func = service_map.get(text)
    if func:
        await func(update, context)
    else:
        await update.message.reply_text("Iltimos, menyudan xizmat tanlang.")

# --- 7. KOMANDALAR RO‘YXATI ---
async def set_commands(app: Application):
    await app.bot.set_my_commands([
        BotCommand("start", "🔁 Botni ishga tushirish")
    ])

# --- 8. BOTNI ISHGA TUSHURISH ---
def main():
    application = Application.builder().token(TOKEN).post_init(set_commands).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot ishga tushdi!")
    application.run_polling()

if __name__ == "__main__":
    main()
