from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

MANAGER_RAVZA = "@vip_arabiy"
MANAGER_ASSISTANT = "@V001VB"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("🕌 Ravzaga tashrif"), KeyboardButton("📦 Umra paketlari")],
        [KeyboardButton("🏨 Mehmonxona/Hostel"), KeyboardButton("🚆 Poezd chiptalari")],
        [KeyboardButton("🚐 Transport xizmati"), KeyboardButton("🍱 Guruhlarga ovqat")],
        [KeyboardButton("✈️ Avia chiptalar"), KeyboardButton("📞 Admin bilan bog‘lanish")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "🕌 *UmraJet — Premium xizmatlar bot* 🤍\n"
        "Sizga yordam berish uchun tayyorman.\n\n"
        "Quyidagi menyudan xizmatni tanlang:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🕌 Ravzaga tashrif":
        await update.message.reply_text(
            "🕌 *Ravzaga tashrif xizmati*\n\n"
            "🔸 Viza bilan: 15 SAR\n"
            "🔸 Vizasiz: 20 SAR\n\n"
            "💳 To‘lov: Uzcard / Humo / Visa / Crypto\n"
            "📎 Hujjatni rasm yoki PDF ko‘rinishida yuboring.\n"
            f"📲 Bog‘lanish: {MANAGER_RAVZA}",
            parse_mode="Markdown"
        )
    elif text == "📦 Umra paketlari":
        await update.message.reply_text(
            "📦 *Umra paketlari*\n\n"
            "🔹 Standard — 1100$ dan boshlanadi\n"
            "🔹 VIP — 2000$ dan\n\n"
            "💳 To‘lov: Uzcard / Humo / Visa / Crypto\n"
            f"📲 Yordamchi: {MANAGER_ASSISTANT}",
            parse_mode="Markdown"
        )
    elif text == "🏨 Mehmonxona/Hostel":
        await update.message.reply_text(
            "🏨 *Mehmonxona/Hostel xizmati*\n\n"
            "Narxlar o‘zgaruvchan. Iltimos, tafsilotlar uchun biz bilan bog‘laning.\n"
            f"📲 {MANAGER_ASSISTANT}",
            parse_mode="Markdown"
        )
    elif text == "🚆 Poezd chiptalari":
        await update.message.reply_text(
            "🚆 *Poezd chiptalari xizmati*\n\n"
            "Chipta narxlari o‘zgaruvchan. Tafsilotlar uchun yozing:\n"
            f"📲 {MANAGER_ASSISTANT}",
            parse_mode="Markdown"
        )
    elif text == "🚐 Transport xizmati":
        await update.message.reply_text(
            "🚐 *Transport xizmati*\n\n"
            "Tafsilotlar va narxlar uchun biz bilan bog‘laning:\n"
            f"📲 {MANAGER_ASSISTANT}",
            parse_mode="Markdown"
        )
    elif text == "🍱 Guruhlarga ovqat":
        await update.message.reply_text(
            "🍱 *Guruhlarga ovqat xizmati*\n\n"
            "Kattaroq guruhlar uchun maxsus ovqatlanish xizmatlari mavjud.\n"
            f"📲 {MANAGER_ASSISTANT}",
            parse_mode="Markdown"
        )
    elif text == "✈️ Avia chiptalar":
        await update.message.reply_text(
            "✈️ *Avia chiptalar xizmati*\n\n"
            "Har qanday davlatga chipta bron qilish mumkin. Narxlar o‘zgaruvchan.\n"
            f"📲 {MANAGER_ASSISTANT}",
            parse_mode="Markdown"
        )
    elif text == "📞 Admin bilan bog‘lanish":
        await update.message.reply_text(
            "📞 *Adminlar bilan bog‘lanish*\n\n"
            f"🕌 Ravza uchun: {MANAGER_RAVZA}\n"
            f"📦 Boshqa xizmatlar uchun: {MANAGER_ASSISTANT}",
            parse_mode="Markdown"
        )
    else:
        await update.message.reply_text("Iltimos, menyudan biror xizmatni tanlang.")

def main():
    application = Application.builder().token(os.getenv("BOT_TOKEN")).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()

if __name__ == "__main__":
    main()
