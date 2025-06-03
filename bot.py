import os
from datetime import datetime
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, BotCommand
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

# --- Muhit o'zgaruvchilarini yuklash ---
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN topilmadi! .env faylni tekshiring.")

# --- Admin kontaklar ---
MANAGER_RAVZA = "@vip_arabiy"
MANAGER_ASSISTANT = "@V001VB"
CHANNEL_UMRAJET = "@umrajet"
CHANNEL_RAVZA = "@the_ravza"

# --- Start komandasi ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("🍇 Ravzaga tashrif"), KeyboardButton("🕋 Umra paketlari")],
        [KeyboardButton("🏨 Mehmonxona/Hostel"), KeyboardButton("🚄 Poezd chiptalari")],
        [KeyboardButton("🚐 Transport xizmati"), KeyboardButton("🍽 Guruh ovqatlari")],
        [KeyboardButton("✈️ Avia chiptalar"), KeyboardButton("📞 Admin bilan bog‘lanish")],
        [KeyboardButton("📢 Rasmiy kanallar")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)

    await update.message.reply_text(
        "🤍 *UmraJet — Premium Umra xizmatlari markazi* 🤍\n\n"
        "Assalomu alaykum! Quyidagi xizmatlardan birini tanlang:",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

# --- Har bir xizmat uchun alohida funksiya --- #
async def ravza_service(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🍇 *Ravzaga tashrif* — Ruhiy yangilanish uchun ajoyib imkoniyat.\n\n"
        "🔹 Viza bilan: 15 SAR\n"
        "🔹 Vizsiz: 20 SAR\n\n"
        "📄 Hujjatlarni rasm yoki PDF ko‘rinishida yuboring.\n"
        f"📞 Bog‘lanish: {MANAGER_RAVZA} yoki {MANAGER_ASSISTANT}",
        parse_mode="Markdown"
    )

async def umra_packages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🕋 *Umra paketlari* — Orzuingizni ro‘yobga chiqaramiz!\n\n"
        "✨ Standard: 1100$\n"
        "✨ VIP: 2000$\n\n"
        "Paketlarga quyidagilar kiradi:\n"
        "✅ Viza rasmiylashtirish\n"
        "✅ Mehmonxona\n"
        "✅ Transport\n"
        "✅ Gid xizmatlari\n"
        "✅ Guruh ovqati\n\n"
        f"📞 Bog‘lanish: {MANAGER_ASSISTANT} yoki {MANAGER_RAVZA}",
        parse_mode="Markdown"
    )

async def hotels(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏨 *Mehmonxona va Hostel bron qilish* — Makka va Madina markazida.\n\n"
        "🕰 Istalgan muddat uchun.\n"
        "🍴 Ovqat bilan yoki ovqatsiz.\n\n"
        f"📞 Aloqa: {MANAGER_ASSISTANT}",
        parse_mode="Markdown"
    )

async def train_tickets(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚄 *Poezd chiptalari* — Makka, Madina va boshqa yo‘nalishlarga.\n\n"
        "🕓 Istalgan sana uchun buyurtma qiling.\n"
        "💺 Ekanom yoki Biznes sinf.\n\n"
        f"📞 Bog‘lanish: {MANAGER_ASSISTANT}",
        parse_mode="Markdown"
    )

async def transport_service(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚐 *Transport xizmati* — Shaxsiy va guruh uchun.\n\n"
        "🚍 Avtobus, Toyota, VIP mashinalar.\n"
        "🏘 Mehmonxonadan masjidlargacha yetkazish.\n"
        f"📞 Buyurtma uchun: {MANAGER_ASSISTANT}",
        parse_mode="Markdown"
    )

async def group_food(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🍽 *Guruh ovqatlari* — 10+ kishilik guruhlar uchun.\n\n"
        "🥘 O‘zbekcha taomlar.\n"
        "🎉 Maxsus menyular.\n\n"
        f"📞 Bog‘lanish: {MANAGER_ASSISTANT}",
        parse_mode="Markdown"
    )

async def plane_tickets(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✈️ *Avia chiptalar* — Istalgan manzilga.\n\n"
        "📆 Istalgan sana va davlat.\n"
        f"📞 Buyurtma: {MANAGER_ASSISTANT} yoki {MANAGER_RAVZA}",
        parse_mode="Markdown"
    )

async def admin_contacts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 *Adminlar bilan bog‘laning:*\n\n"
        f"🍇 Ravza xizmati: {MANAGER_RAVZA}\n"
        f"🕋 Umra va boshqa xizmatlar: {MANAGER_ASSISTANT}",
        parse_mode="Markdown"
    )

async def official_channels(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📢 *Rasmiy kanallarimiz:*\n\n"
        f"✅ UmraJet yangiliklari: {CHANNEL_UMRAJET}\n"
        f"✅ Ravza yangiliklari: {CHANNEL_RAVZA}",
        parse_mode="Markdown"
    )

# --- Xabarlarni qayta ishlovchi funksiya --- #
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🍇 Ravzaga tashrif":
        await ravza_service(update, context)
    elif text == "🕋 Umra paketlari":
        await umra_packages(update, context)
    elif text == "🏨 Mehmonxona/Hostel":
        await hotels(update, context)
    elif text == "🚄 Poezd chiptalari":
        await train_tickets(update, context)
    elif text == "🚐 Transport xizmati":
        await transport_service(update, context)
    elif text == "🍽 Guruh ovqatlari":
        await group_food(update, context)
    elif text == "✈️ Avia chiptalar":
        await plane_tickets(update, context)
    elif text == "📞 Admin bilan bog‘lanish":
        await admin_contacts(update, context)
    elif text == "📢 Rasmiy kanallar":
        await official_channels(update, context)
    else:
        await update.message.reply_text(
            "Iltimos, menyudan xizmat tanlang yoki /start ni bosing."
        )

# --- Bot komandalarini sozlash ---
async def set_menu_commands(application: Application):
    await application.bot.set_my_commands([
        BotCommand("start", "🔄 Botni qayta ishga tushirish"),
    ])

def main():
    application = Application.builder().token(TOKEN).post_init(set_menu_commands).build()

    # Handlerlarni qo‘shish
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Botni ishga tushirish
    application.run_polling()

if __name__ == "__main__":
    main()
