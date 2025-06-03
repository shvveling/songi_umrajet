import os
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
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "🤍 *UmraJet — Premium Umra xizmatlari markazi* 🤍\n\n"
        "Assalomu alaykum!\nQuyidagi xizmatlardan birini tanlang 👇",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

# --- Xizmat panel funksiyalari ---
async def ravza_service(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🍇 *Ravzaga tashrif xizmati* 🍇\n\n"
        "🕌 Madinadagi eng muqaddas joy — Ravza.\n"
        "👥 Jamoaviy yoki shaxsiy tashriflar\n"
        "💳 To‘lov: Uzcard / Humo / Visa / Crypto\n"
        "📄 Hujjatni rasm yoki PDF ko‘rinishida yuboring.\n\n"
        f"📞 Aloqa: {MANAGER_RAVZA} yoki {MANAGER_ASSISTANT}",
        parse_mode="Markdown"
    )

async def umra_packages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🕋 *Umra paketlari* 🌙\n\n"
        "📦 Paketlar tarkibi:\n"
        "✅ Viza, Mehmonxona, Transport, Gid, Ovqat\n"
        "💼 Narxlar: Standard — 1100$, VIP — 2000$ dan\n\n"
        f"📞 Aloqa: {MANAGER_ASSISTANT} yoki {MANAGER_RAVZA}",
        parse_mode="Markdown"
    )

async def hotels(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🏨 *Mehmonxona/Hostel bron qilish* 🛏\n\n"
        "📍 Makka va Madinadagi markaziy joylashuvlar\n"
        "🕰 Har qanday muddatga\n"
        "🍱 Ovqatli yoki ovqatsiz variantlar\n\n"
        f"📞 Aloqa: {MANAGER_ASSISTANT} yoki {MANAGER_RAVZA}",
        parse_mode="Markdown"
    )

async def train_tickets(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🚄 *Poezd chiptalari — HHR liniyasi* 🚅\n\n"
        "📍 Yo‘nalish: Makka ↔ Madina\n"
        "💺 Ekanom / Biznes klass\n"
        "📅 Istalgan sana uchun bron qilish mumkin\n\n"
        f"📞 Aloqa: {MANAGER_ASSISTANT} yoki {MANAGER_RAVZA}",
        parse_mode="Markdown"
    )

async def transport_service(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🚐 *Transport xizmati* 🚖\n\n"
        "🚌 Guruh va shaxsiy mashinalar\n"
        "🏘 Mehmonxonadan masjidlargacha yetkazish\n"
        "👨‍✈️ Tajribali haydovchilar\n\n"
        f"📞 Aloqa: {MANAGER_ASSISTANT} yoki {MANAGER_RAVZA}",
        parse_mode="Markdown"
    )

async def group_food(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🍽 *Guruh ovqatlari* 🍛\n\n"
        "👥 10+ kishilik guruhlar uchun\n"
        "🥘 O‘zbekcha taomlar\n"
        "🍱 1, 2 yoki 3 mahal taom menyusi\n\n"
        f"📞 Aloqa: {MANAGER_ASSISTANT} yoki {MANAGER_RAVZA}",
        parse_mode="Markdown"
    )

async def plane_tickets(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"✈️ *Avia chiptalar* 🌍\n\n"
        "📅 Har qanday sana\n"
        "🛫 Har qanday manzilga\n"
        "📎 Vizali yoki vizasiz variantlar\n\n"
        f"📞 Aloqa: {MANAGER_ASSISTANT} yoki {MANAGER_RAVZA}",
        parse_mode="Markdown"
    )

async def admin_contacts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"📞 *Administratorlar bilan bog‘lanish:*\n\n"
        f"🍇 Ravza xizmatlari: {MANAGER_RAVZA}\n"
        f"🕋 Umra & boshqa xizmatlar: {MANAGER_ASSISTANT}",
        parse_mode="Markdown"
    )

async def official_channels(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"📢 *Rasmiy axborot kanallari:*\n\n"
        f"📌 UmraJet yangiliklari: {CHANNEL_UMRAJET}\n"
        f"📌 Ravza tashriflari: {CHANNEL_RAVZA}",
        parse_mode="Markdown"
    )

# --- Har bir tugma xabarini qayta ishlovchi ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    handlers = {
        "🍇 Ravzaga tashrif": ravza_service,
        "🕋 Umra paketlari": umra_packages,
        "🏨 Mehmonxona/Hostel": hotels,
        "🚄 Poezd chiptalari": train_tickets,
        "🚐 Transport xizmati": transport_service,
        "🍽 Guruh ovqatlari": group_food,
        "✈️ Avia chiptalar": plane_tickets,
        "📞 Admin bilan bog‘lanish": admin_contacts,
        "📢 Rasmiy kanallar": official_channels,
    }
    handler = handlers.get(text)
    if handler:
        await handler(update, context)
    else:
        await update.message.reply_text("Iltimos, pastdagi tugmalardan birini tanlang.")

# --- Komandalar menyusi ---
async def set_menu_commands(application: Application):
    await application.bot.set_my_commands([
        BotCommand("start", "🔄 Botni qayta ishga tushirish"),
    ])

# --- Botni ishga tushirish ---
def main():
    application = Application.builder().token(TOKEN).post_init(set_menu_commands).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()

if __name__ == "__main__":
    main()
