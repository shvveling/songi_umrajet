import os
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, BotCommand
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv

# --- Tokenni yuklash ---
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN topilmadi! .env faylni tekshiring.")

# --- Aloqa ma'lumotlari ---
MANAGER_RAVZA = "@vip_arabiy"
MANAGER_ASSISTANT = "@V001VB"
CHANNEL_UMRAJET = "@umrajet"
CHANNEL_RAVZA = "@the_ravza"

# --- Start komandasi ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("🍇 Ravzaga tashrif"), KeyboardButton("🕋 Umra paketlari")],
        [KeyboardButton("🏨 Mehmonxona / Hostel"), KeyboardButton("🚄 Poezd chiptalari")],
        [KeyboardButton("🚐 Transport xizmati"), KeyboardButton("🍽 Guruh ovqatlari")],
        [KeyboardButton("✈️ Avia chiptalar"), KeyboardButton("📞 Admin bilan bog‘lanish")],
        [KeyboardButton("📢 Rasmiy kanallar")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "🤍 *UmraJet — Premium Umra xizmatlari markazi* 🤍\n\n"
        "Assalomu alaykum!\n"
        "Quyidagi xizmatlardan birini tanlang:",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

# --- Panel xabarlari ---
async def ravza_service(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🍇 *Ravzaga tashrif* — Madina yuragidagi eng muqaddas joyga yo‘l\n\n"
        "📌 Jamoaviy va individual tashriflar\n"
        "🕒 Har kuni tashkillashtiriladi\n"
        "🛂 Viza bor yoki yo‘qligidan qat’i nazar\n"
        "💳 Uzcard, Humo, Visa, Crypto to‘lovlar\n\n"
        f"📞 Bog‘lanish: {MANAGER_RAVZA} | {MANAGER_ASSISTANT}",
        parse_mode="Markdown"
    )

async def umra_packages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🕋 *Umra paketlari — Sifatli va qulay xizmatlar jamlanmasi*\n\n"
        "✨ Standard: $1100 dan\n"
        "✨ VIP: $2000 dan\n\n"
        "✅ Viza, mehmonxona, transport, gid, ovqat kiritilgan\n"
        "🛂 Sizga faqat pasport kerak!\n\n"
        f"📞 Batafsil: {MANAGER_ASSISTANT} | {MANAGER_RAVZA}",
        parse_mode="Markdown"
    )

async def hotels(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏨 *Mehmonxona / Hostel bron qilish* — Farovon va xavfsiz dam olish\n\n"
        "📍 Makka va Madina markazida joylar\n"
        "🕰 Istalgan muddatga, oilaviy yoki individual\n"
        "🍽 Ovqatli va ovqatsiz variantlar\n\n"
        f"📞 Bron uchun: {MANAGER_ASSISTANT} | {MANAGER_RAVZA}",
        parse_mode="Markdown"
    )

async def train_tickets(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚄 *HHR Poezd chiptalari* — Makka, Madina va boshqa yo‘nalishlar\n\n"
        "💺 Ekanom va Biznes klass\n"
        "🗓 Istalgan kunga buyurtma\n"
        "🛂 Viza talab qilinadi\n\n"
        f"📞 Yordam: {MANAGER_ASSISTANT} | {MANAGER_RAVZA}",
        parse_mode="Markdown"
    )

async def transport_service(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚐 *Transport xizmati* — Shaxsiy va guruh tashish\n\n"
        "🚗 VIP mashinalar, miniven, avtobuslar\n"
        "📍 Makka-Madina ichida va shaharlararo\n"
        "👨‍✈️ Tajribali haydovchilar\n\n"
        f"📞 Buyurtma: {MANAGER_ASSISTANT} | {MANAGER_RAVZA}",
        parse_mode="Markdown"
    )

async def group_food(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🍽 *Guruh ovqatlari* — Sog‘lom va uyda tayyorlangan taomlar\n\n"
        "🥘 O‘zbekcha menyu, 1-3 mahal\n"
        "👥 10+ kishilik guruhlar uchun\n"
        "🎉 Maxsus tadbirlar menyusi\n\n"
        f"📞 Buyurtma uchun: {MANAGER_ASSISTANT} | {MANAGER_RAVZA}",
        parse_mode="Markdown"
    )

async def plane_tickets(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✈️ *Avia chiptalar* — Dunyodagi istalgan nuqtaga\n\n"
        "🌐 Vizali yoki vizasiz variantlar\n"
        "📆 Mos keluvchi sanalarni topishda yordam\n\n"
        f"📞 Aloqa: {MANAGER_ASSISTANT} | {MANAGER_RAVZA}",
        parse_mode="Markdown"
    )

async def admin_contacts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 *Adminlar bilan bog‘lanish:*\n\n"
        f"🍇 Ravza xizmatlari: {MANAGER_RAVZA}\n"
        f"🕋 Umra va boshqa xizmatlar: {MANAGER_ASSISTANT}",
        parse_mode="Markdown"
    )

async def official_channels(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📢 *Rasmiy kanallarimiz:*\n\n"
        f"📌 UmraJet yangiliklari: {CHANNEL_UMRAJET}\n"
        f"📌 Ravza tashriflari: {CHANNEL_RAVZA}",
        parse_mode="Markdown"
    )

# --- Router ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "🍇 Ravzaga tashrif":
        await ravza_service(update, context)
    elif text == "🕋 Umra paketlari":
        await umra_packages(update, context)
    elif text == "🏨 Mehmonxona / Hostel":
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
        await update.message.reply_text("Iltimos, menyudan bir xizmat tanlang.")

# --- Bot komandalar menyusi ---
async def set_commands(application: Application):
    await application.bot.set_my_commands([
        BotCommand("start", "🔄 Botni qayta ishga tushirish")
    ])

# --- Botni ishga tushirish ---
def main():
    app = Application.builder().token(TOKEN).post_init(set_commands).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
