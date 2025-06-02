import os
import asyncio
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, BotCommand
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from datetime import datetime, timedelta

# .env fayldan tokenni yuklash
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN muhit o'zgaruvchisi o'rnatilmagan!")

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
        [KeyboardButton("🍍 Ravzaga tashrif"), KeyboardButton("📦 Umra paketlari")],
        [KeyboardButton("🏨 Mehmonxona/Hostel"), KeyboardButton("🚆 Poezd chiptalari")],
        [KeyboardButton("🚐 Transport xizmati"), KeyboardButton("🍱 Guruhlarga ovqat")],
        [KeyboardButton("✈️ Avia chiptalar"), KeyboardButton("📞 Admin bilan bog‘lanish")],
        [KeyboardButton("📢 Kanalimiz"), KeyboardButton("🤖 Savol-javob & maslahat")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        """
*UmraJet — Premium xizmatlar bot 🤍*

Assalomu alaykum! Quyidagi xizmatlardan birini tanlang:
        """,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# Foydalanuvchi xabarlariga javob berish
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    discount_active = is_discount_active()

    if text == "🍍 Ravzaga tashrif":
        price_viza = "10 SAR (aksiyada!)" if discount_active else "15 SAR"
        price_no_viza = "15 SAR (aksiyada!)" if discount_active else "20 SAR"

        await update.message.reply_text(f"""
*🍍 Ravzaga tashrif xizmati*

🔸 Viza bilan: {price_viza}
🔸 Vizasiz: {price_no_viza}

🎉 *Aksiya:* Bot ishga tushganidan keyingi 7 kun ichida har bir tashrif xizmati faqat {price_viza}!

💼 Ko‘p sonli buyurtmalarda chegirmalar mavjud.
💳 To‘lov: Uzcard / Humo / Visa / Crypto
📌 Hujjatni rasm yoki PDF ko‘rinishida yuboring.

📲 Bog‘lanish: {MANAGER_RAVZA}
        """, parse_mode="Markdown")

    elif text == "📦 Umra paketlari":
        await update.message.reply_text(f"""
*📦 Umra paketlari*

🔹 Standard: 1100$ dan
🔹 VIP: 2000$ dan

✅ Vizani rasmiylashtirish
✅ Mehmonxona joyi
✅ Transport xizmati
✅ Guruh ovqatlanishi
✅ Gid xizmati

💳 To‘lov: Uzcard / Humo / Visa / Crypto
📲 Yordamchi: {MANAGER_ASSISTANT}
        """, parse_mode="Markdown")

    elif text == "🏨 Mehmonxona/Hostel":
        await update.message.reply_text(f"""
*🏨 Mehmonxona va Hostel bron qilish*

📍 Makka va Madina shaharlarida joylar
📆 Qisqa yoki uzoq muddatli
🍽 3 mahal ovqat bilan yoki ovqatsiz

📲 Bog‘lanish: {MANAGER_ASSISTANT}
        """, parse_mode="Markdown")

    elif text == "🚆 Poezd chiptalari":
        await update.message.reply_text(f"""
*🚆 HHR Poezd chiptalari*

🔹 Yo‘nalishlar: Makkadan → Madina va boshqa shaharlar
📅 Buyurtma: Istalgan kunga
🛫 Vizangiz bo‘lsa kifoya
💺 Ekanom / Biznes sinf

📲 Buyurtma: {MANAGER_ASSISTANT}
        """, parse_mode="Markdown")

    elif text == "🚐 Transport xizmati":
        await update.message.reply_text(f"""
*🚐 Transport xizmati*

🚌 Avtobuslar, 🚙 Toyota, 🚖 VIP avtomobillar
🏠 Makkaga olib kirish xizmati
🤝 Tajribali haydovchilar

📲 Buyurtma: {MANAGER_ASSISTANT}
        """, parse_mode="Markdown")

    elif text == "🍱 Guruhlarga ovqat":
        await update.message.reply_text(f"""
*🍱 Guruhlarga ovqat xizmati*

👥 10+ kishilik buyurtmalar
🍛 O'zbek taomlari
📦 1-3 mahal xizmatlar
🍻 VIP ziyofatlar

📲 Bog‘lanish: {MANAGER_ASSISTANT}
        """, parse_mode="Markdown")

    elif text == "✈️ Avia chiptalar":
        await update.message.reply_text(f"""
*✈️ Avia chiptalar xizmati*

🌍 Istalgan davlatga chipta
💳 Vizali/vizasiz
📅 Xaridor istagan sana

📲 Buyurtma: {MANAGER_ASSISTANT}
        """, parse_mode="Markdown")

    elif text == "📞 Admin bilan bog‘lanish":
        await update.message.reply_text(f"""
*📞 Adminlar bilan bog‘lanish*

🍍 Ravza: {MANAGER_RAVZA}
📦 Boshqa xizmatlar: {MANAGER_ASSISTANT}
        """, parse_mode="Markdown")

    elif text == "📢 Kanalimiz":
        await update.message.reply_text(f"""
*📢 Rasmiy kanallarimiz:*

🔜 UmraJet yangiliklari: {CHANNEL_UMRAJET}
🔜 Ravza tashriflari: {CHANNEL_RAVZA}
        """, parse_mode="Markdown")

    elif text == "🤖 Savol-javob & maslahat":
        await update.message.reply_text(f"""
*🤖 Savol-javoblar:*

❓ *Vizasi yo‘q odam Ravzaga bora oladimi?*
✅ Ha, biz yordam beramiz.

❓ *To‘lov usullari qanday?*
✅ Uzcard, Humo, Visa, Crypto.

❓ *Umra narxiga nimalar kiradi?*
✅ Viza, mehmonxona, transport va boshqalar.

📞 Bog‘lanish: {MANAGER_RAVZA} | {MANAGER_ASSISTANT}
        """, parse_mode="Markdown")
    else:
        await update.message.reply_text("Iltimos, menyudan biror xizmatni tanlang.")

# Komandalar menyusi
async def set_menu_commands(application):
    await application.bot.set_my_commands([
        BotCommand("start", "🔄 Botni qayta ishga tushirish"),
        BotCommand("ravza", "🍍 Ravzaga tashrif"),
        BotCommand("umra", "📦 Umra paketlari")
    ])

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == "__main__":
    main()
