import os
from datetime import datetime, timedelta
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, BotCommand
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("ERROR: BOT_TOKEN environment variable is not set!")

# Admin kontaktlari
MANAGER_RAVZA = "@vip_arabiy"
MANAGER_ASSISTANT = "@V001VB"
CHANNEL_UMRAJET = "@umrajet"
CHANNEL_RAVZA = "@the_ravza"

# Bot ishga tushgan sana (aksiyalar uchun)
BOT_START_DATE = datetime(2025, 6, 2)

def is_discount_active():
    return datetime.now() < BOT_START_DATE + timedelta(days=7)

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("🍊 Ravzaga tashrif"), KeyboardButton("📆 Umra paketlari")],
        [KeyboardButton("🏨 Mehmonxona/Hostel"), KeyboardButton("\ud83d\ude86 Poezd chiptalari")],
        [KeyboardButton("\ud83d\ude98 Transport xizmati"), KeyboardButton("\ud83c\udf71 Guruhlarga ovqat")],
        [KeyboardButton("\u2708\ufe0f Avia chiptalar"), KeyboardButton("\ud83d\udcde Admin bilan bog‘lanish")],
        [KeyboardButton("\ud83d\udce2 Kanalimiz"), KeyboardButton("\ud83e\udd16 Savol-javob & maslahat")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        """
*\ud83d\udd4b UmraJet — Premium xizmatlar bot ♥*

Assalomu alaykum va rahmatulloh! Sizga Saudiya Arabistoni Umra xizmatlari bo’yicha professional yordam beramiz. Quyidagi bo‘limlardan keraklisini tanlang:
        """,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# Foydalanuvchi xabarlariga javob
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    discount_active = is_discount_active()

    if text == "🍊 Ravzaga tashrif":
        price_viza = "10 SAR (aksiyada!)" if discount_active else "15 SAR"
        price_no_viza = "15 SAR (aksiyada!)" if discount_active else "20 SAR"

        await update.message.reply_text(
            f"""
*\ud83c\udf4a Ravzaga tashrif xizmati*

\ud83d\udd38 Viza bilan: {price_viza}
\ud83d\udd38 Vizasiz: {price_no_viza}

\ud83c\udf89 *Aksiya:* Bot ishga tushganidan keyingi 7 kun ichida har bir tashrif xizmati faqat {price_viza}!

\ud83d\udcbc Ko‘p sonli buyurtmalarda qo‘shimcha chegirmalar mavjud.
\ud83d\udcb3 To‘lov: Uzcard / Humo / Visa / Crypto
\ud83d\udccc Hujjatni rasm yoki PDF ko‘rinishida yuboring.

\ud83d\udcf2 Bog‘lanish: {MANAGER_RAVZA}
            """,
            parse_mode="Markdown"
        )

    elif text == "📆 Umra paketlari":
        await update.message.reply_text(
            f"""
*\ud83d\udcc6 Umra paketlari*

\ud83d\udd39 Standard: 1100$ dan
\ud83d\udd39 VIP: 2000$ dan

Paketga quyidagilar kiradi:
✅ Vizani rasmiylashtirish
✅ Mehmonxona joyi (Makka/Madina)
✅ Transport xizmati
✅ Guruh ovqatlanishi
✅ Gid xizmati va yo‘l-yo‘riq

\ud83d\udcb3 To‘lov: Uzcard / Humo / Visa / Crypto
\ud83d\udcf2 Yordamchi: {MANAGER_ASSISTANT}
            """,
            parse_mode="Markdown"
        )

    # Add other elif branches for the remaining buttons here

    else:
        await update.message.reply_text("Iltimos, menyudan biror xizmatni tanlang.")

# Komanda menyusi
async def set_menu_commands(application):
    await application.bot.set_my_commands([
        BotCommand("start", "\ud83d\udd04 Botni qayta ishga tushirish")
    ])

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == "__main__":
    main()
