from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

# Manager usernames
MANAGER_RAVZA = "@vip_arabiy"
MANAGER_ASSISTANT = "@V001VB"

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("🕌 Ravzaga tashrif"), KeyboardButton("📦 Umra paketlari")],
        [KeyboardButton("🏨 Mehmonxona/Hostel"), KeyboardButton("🚆 Poezd chiptalari")],
        [KeyboardButton("🚐 Transport xizmati"), KeyboardButton("🍱 Guruhlarga ovqat")],
        [KeyboardButton("✈️ Avia chiptalar"), KeyboardButton("📞 Admin bilan bog‘lanish")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        """
🕌 *UmraJet — Premium xizmatlar bot* 🤍

Assalomu alaykum! Sizga Umra va Haj safarlarida eng yuqori darajadagi xizmatlarni taqdim etamiz.
Quyidagi menyudan kerakli xizmatni tanlang:
        """,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# Message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🕌 Ravzaga tashrif":
        await update.message.reply_text(
            f"""
🕌 *Ravzaga tashrif xizmati*

🔸 *Viza bilan*: 15 SAR
🔹 *Vizasiz*: 20 SAR

📉 *Guruh uchun yoki ko‘p miqdorda buyurtmalarda chegirmalar mavjud!*

📝 Rasm yoki PDF formatda hujjatingizni yuboring. 
💳 To‘lov: Uzcard / Humo / Visa / Crypto
📲 Bog‘lanish: {MANAGER_RAVZA}
            """,
            parse_mode="Markdown"
        )

    elif text == "📦 Umra paketlari":
        await update.message.reply_text(
            f"""
📦 *Umra Paketlari* — barcha xizmatlar bitta joyda!

🔹 *Standard*: 1100$ dan
🔸 *VIP*: 2000$ dan

✅ Paketga quyidagilar kiradi:
- Mehmonxona (Makka va Madina)
- Transferlar (Aeroport, Ziyorat joylari)
- Umra uchun qo‘llab-quvvatlash
- Viza va hujjatlar
- 24/7 yordam xizmati

💳 To‘lov: Uzcard / Humo / Visa / Crypto
📲 Yordamchi: {MANAGER_ASSISTANT}
            """,
            parse_mode="Markdown"
        )

    elif text == "🏨 Mehmonxona/Hostel":
        await update.message.reply_text(
            f"""
🏨 *Mehmonxona/Hostel bron qilish xizmati*

📍 Makka, Madina va boshqa shaharlarda mavjud
🛏️ 1 kishilikdan 5 kishilikgacha xonalar
🍽 3 mahal ovqat bilan yoki ovqatsiz variantlar

💬 Narxlar: Muddat, joylashuv va xizmatga qarab o‘zgaradi.
📲 Tafsilotlar uchun bog‘laning: {MANAGER_ASSISTANT}
            """,
            parse_mode="Markdown"
        )

    elif text == "🚆 Poezd chiptalari":
        await update.message.reply_text(
            f"""
🚆 *Poezd chiptalari (HHR Train)*

📍 Yo‘nalishlar: Makka ↔ Madina ↔ Jidda ↔ King Abdullah Economic City
💺 Klasslar: Ekonom va Biznes
📆 Buyurtma: Istalgan sana uchun bron qilish mumkin

🛂 Saudiya vizasi kifoya
📲 Buyurtma uchun bog‘laning: {MANAGER_ASSISTANT}
            """,
            parse_mode="Markdown"
        )

    elif text == "🚐 Transport xizmati":
        await update.message.reply_text(
            f"""
🚐 *Transport xizmati*

🚗 Mashinalar: Toyota, GMC, Buslar, VIP transportlar
📍 Xizmatlar: Shahardan shahar, aeroportdan mehmonxonagacha, Makkaga olib kirish
👨‍✈️ Haydovchi bilan birga

📲 Buyurtma uchun bog‘laning: {MANAGER_ASSISTANT}
            """,
            parse_mode="Markdown"
        )

    elif text == "🍱 Guruhlarga ovqat":
        await update.message.reply_text(
            f"""
🍱 *Guruhlarga ovqat yetkazib berish xizmati*

👥 10–15 kishilik guruhlar uchun
🍽 O‘zbek taomlari va maxsus VIP menyular
📦 Yetkazib beriladi
💰 Narxlar taom soni va menyuga qarab belgilanadi

📲 Buyurtma va menyu uchun bog‘laning: {MANAGER_ASSISTANT}
            """,
            parse_mode="Markdown"
        )

    elif text == "✈️ Avia chiptalar":
        await update.message.reply_text(
            f"""
✈️ *Avia chiptalar bron qilish xizmati*

🌍 Istalgan davlatga chipta bron qilish
📆 Sana va yo‘nalish siz tanlaysiz
📞 Vizasiz/Viza farqi yo‘q — har bir mijozga individual xizmat

📲 Buyurtma uchun bog‘laning: {MANAGER_ASSISTANT}
            """,
            parse_mode="Markdown"
        )

    elif text == "📞 Admin bilan bog‘lanish":
        await update.message.reply_text(
            f"""
📞 *Adminlar bilan bog‘lanish*

🕌 Ravza xizmatlari uchun: {MANAGER_RAVZA}
📦 Boshqa xizmatlar uchun: {MANAGER_ASSISTANT}
            """,
            parse_mode="Markdown"
        )

    else:
        await update.message.reply_text("❗ Iltimos, menyudan biror xizmatni tanlang.")

# Bot start

def main():
    application = Application.builder().token("7667056220:AAEc8DwQ0WJrBfVk_yLN8wLWGpxUfRKT-5A").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == "__main__":
    main()
