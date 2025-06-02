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
        "🕌 *UmraJet — Premium xizmatlar bot* 🤍

"
        "Quyidagi menyudan xizmatni tanlang:", reply_markup=reply_markup, parse_mode="Markdown"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🕌 Ravzaga tashrif":
        await update.message.reply_text(
            "🕌 *Ravzaga tashrif xizmati*

"
            "🔸 Viza bilan: 15 SAR
"
            "🔸 Vizasiz: 20 SAR

"
            "💳 To‘lov: Uzcard / Humo / Visa / Crypto
"
            "📎 Hujjatni rasm yoki PDF ko‘rinishida yuboring.
"
            f"📲 Bog‘lanish: {MANAGER_RAVZA}", parse_mode="Markdown"
        )
    elif text == "📦 Umra paketlari":
        await update.message.reply_text(
            "📦 *Umra paketlari*

"
            "🔹 Standard — 1100$ dan boshlanadi
"
            "🔹 VIP — 2000$ dan

"
            "💳 To‘lov: Uzcard / Humo / Visa / Crypto
"
            f"📲 Yordamchi: {MANAGER_ASSISTANT}", parse_mode="Markdown"
        )
    elif text == "🏨 Mehmonxona/Hostel":
        await update.message.reply_text(
            "🏨 *Mehmonxona/Hostel xizmati*

"
            "Narxlar o‘zgaruvchan. Iltimos, tafsilotlar uchun biz bilan bog‘laning.
"
            f"📲 {MANAGER_ASSISTANT}", parse_mode="Markdown"
        )
    elif text == "🚆 Poezd chiptalari":
        await update.message.reply_text(
            "🚆 *Poezd chiptalari xizmati*

"
            "Chipta narxlari o‘zgaruvchan. Tafsilotlar uchun yozing:
"
            f"📲 {MANAGER_ASSISTANT}", parse_mode="Markdown"
        )
    elif text == "🚐 Transport xizmati":
        await update.message.reply_text(
            "🚐 *Transport xizmati*

"
            "Tafsilotlar va narxlar uchun biz bilan bog‘laning:
"
            f"📲 {MANAGER_ASSISTANT}", parse_mode="Markdown"
        )
    elif text == "🍱 Guruhlarga ovqat":
        await update.message.reply_text(
            "🍱 *Guruhlarga ovqat xizmati*

"
            "Kattaroq guruhlar uchun maxsus ovqatlanish xizmatlari mavjud.
"
            f"📲 {MANAGER_ASSISTANT}", parse_mode="Markdown"
        )
    elif text == "✈️ Avia chiptalar":
        await update.message.reply_text(
            "✈️ *Avia chiptalar xizmati*

"
            "Har qanday davlatga chipta bron qilish mumkin. Narxlar o‘zgaruvchan.
"
            f"📲 {MANAGER_ASSISTANT}", parse_mode="Markdown"
        )
    elif text == "📞 Admin bilan bog‘lanish":
        await update.message.reply_text(
            "📞 *Adminlar bilan bog‘lanish*

"
            f"🕌 Ravza uchun: {MANAGER_RAVZA}
"
            f"📦 Boshqa xizmatlar uchun: {MANAGER_ASSISTANT}", parse_mode="Markdown"
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
