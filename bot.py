import os
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, BotCommand
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv

# Tokenni yuklash
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN topilmadi. .env faylni tekshiring.")

# Adminlar
MANAGER_RAVZA = "@vip_arabiy"
MANAGER_ASSISTANT = "@V001VB"

# Start komandasi
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
        "Quyidagi xizmatlardan birini tanlang:",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

# Xizmat funksiyalari
async def ravza_service(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🍇 *Ravza tashrifi — Ilohiy iltijo va ruhiy yangilanish!* ✨\n\n"
        "🔹 Viza bilan — 15 SAR\n"
        "🔹 Vizasiz — 20 SAR\n\n"
        "📌 Shaxsiy va guruhli tashriflar\n"
        "📄 Hujjat: rasm yoki PDF ko‘rinishida\n"
        "💳 To‘lov: Uzcard, Humo, Visa, Crypto\n\n"
        f"📞 Bog‘lanish: {MANAGER_RAVZA} | {MANAGER_ASSISTANT}",
        parse_mode="Markdown"
    )

async def umra_packages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🕋 *Umra paketlari — Orzu emas, haqiqat!* 🌙\n\n"
        "✨ *Standard paket:* $1100 dan\n"
        "✨ *VIP paket:* $2000 dan\n\n"
        "✅ Viza rasmiylashtirish\n"
        "✅ Mehmonxona\n"
        "✅ Transport\n"
        "✅ Gid xizmatlari\n"
        "✅ Ovqat\n\n"
        "💳 To‘lov: Uzcard, Humo, Visa, Crypto\n"
        f"📞 Bog‘lanish: {MANAGER_ASSISTANT} | {MANAGER_RAVZA}",
        parse_mode="Markdown"
    )

async def hotels(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏨 *Mehmonxona va Hostel bron qilish* 🛏\n\n"
        "📍 Makka va Madina markazida\n"
        "🕰 Har qanday muddatga\n"
        "🍽 Ovqatli va ovqatsiz variantlar\n"
        "🔐 Xavfsiz va ishonchli xizmat\n\n"
        f"📞 Bog‘lanish: {MANAGER_ASSISTANT} | {MANAGER_RAVZA}",
        parse_mode="Markdown"
    )

async def train_tickets(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚄 *HHR Poezd chiptalari* 🚅\n\n"
        "📍 Yo‘nalish: Makka ↔ Madina\n"
        "🗓 Istalgan kunga buyurtma\n"
        "💺 Joylar: Ekanom va Biznes\n\n"
        f"📞 Bog‘lanish: {MANAGER_ASSISTANT} | {MANAGER_RAVZA}",
        parse_mode="Markdown"
    )

async def transport(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚐 *Transport xizmati — qulay va xavfsiz* 🚘\n\n"
        "🚍 Avtobus, Toyota, VIP mashinalar\n"
        "🕌 Masjidlarga, aeroportlarga yetkazish\n"
        "👨‍✈️ Tajribali haydovchilar\n\n"
        f"📞 Bog‘lanish: {MANAGER_ASSISTANT} | {MANAGER_RAVZA}",
        parse_mode="Markdown"
    )

async def group_food(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🍽 *Guruh ovqatlari (10+ kishilik)* 🍛\n\n"
        "🥘 O‘zbekcha taomlar\n"
        "🍱 1, 2 yoki 3 mahal menyular\n"
        "🎉 Ziyofatlar uchun maxsus variantlar\n\n"
        f"📞 Bog‘lanish: {MANAGER_ASSISTANT} | {MANAGER_RAVZA}",
        parse_mode="Markdown"
    )

async def plane_tickets(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✈️ *Avia chiptalar — Istalgan yo‘nalish bo‘yicha* 🌍\n\n"
        "📆 Sana va davlat tanlovi erkin\n"
        "🛂 Vizali yoki vizasiz variantlar\n\n"
        f"📞 Bog‘lanish: {MANAGER_ASSISTANT} | {MANAGER_RAVZA}",
        parse_mode="Markdown"
    )

async def contact_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 *Adminlar bilan bog‘lanish:*\n\n"
        f"🍇 Ravza: {MANAGER_RAVZA}\n"
        f"🕋 Umra & boshqa xizmatlar: {MANAGER_ASSISTANT}",
        parse_mode="Markdown"
    )

async def official_channels(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📢 *Rasmiy kanallar:*\n\n"
        "🔗 @umrajet — Yangiliklar va e’lonlar\n"
        "🔗 @the_ravza — Ravza tashrifi haqida\n\n"
        f"📞 Savollar uchun: {MANAGER_RAVZA} | {MANAGER_ASSISTANT}",
        parse_mode="Markdown"
    )

# Message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "🍇 Ravza tashrifi":
        await ravza_service(update, context)
    elif text == "🕋 Umra paketlari":
        await umra_packages(update, context)
    elif text == "🏨 Mehmonxona / Hostel":
        await hotels(update, context)
    elif text == "🚄 Poezd chiptalari":
        await train_tickets(update, context)
    elif text == "🚐 Transport xizmati":
        await transport(update, context)
    elif text == "🍽 Guruh ovqatlari":
        await group_food(update, context)
    elif text == "✈️ Avia chiptalar":
        await plane_tickets(update, context)
    elif text == "📞 Admin bilan bog‘lanish":
        await contact_admin(update, context)
    elif text == "📢 Rasmiy kanallar":
        await official_channels(update, context)
    else:
        await update.message.reply_text("Iltimos, menyudan xizmat tanlang.")

# Menu komandasi
async def set_commands(application: Application):
    await application.bot.set_my_commands([
        BotCommand("start", "🔁 Botni ishga tushirish")
    ])

# Main
def main():
    application = Application.builder().token(TOKEN).post_init(set_commands).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == "__main__":
    main()
