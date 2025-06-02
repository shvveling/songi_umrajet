from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, BotCommand
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from datetime import datetime, timedelta
import asyncio

# Admin kontaktlari
MANAGER_RAVZA = "@vip_arabiy"
MANAGER_ASSISTANT = "@V001VB"
CHANNEL_UMRAJET = "@umrajet"
CHANNEL_RAVZA = "@the_ravza"

# Bot ishga tushgan sana (aksiyalar uchun)
BOT_START_DATE = datetime(2025, 6, 2)

def is_discount_active():
    return datetime.now() < BOT_START_DATE + timedelta(days=7)

# Start komandasi uchun
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("🕌 Ravzaga tashrif"), KeyboardButton("📦 Umra paketlari")],
        [KeyboardButton("🏨 Mehmonxona/Hostel"), KeyboardButton("🚆 Poezd chiptalari")],
        [KeyboardButton("🚐 Transport xizmati"), KeyboardButton("🍱 Guruhlarga ovqat")],
        [KeyboardButton("✈️ Avia chiptalar"), KeyboardButton("📞 Admin bilan bog‘lanish")],
        [KeyboardButton("📢 Kanalimiz"), KeyboardButton("🤖 Savol-javob & maslahat")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        """
*🕋 UmraJet — Premium xizmatlar bot 🤍*

Assalomu alaykum va rahmatulloh! Sizga Saudiya Arabistoni Umra xizmatlari bo‘yicha professional yordam beramiz. Quyidagi bo‘limlardan keraklisini tanlang:
        """,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

    await update.message.reply_text(
        f"""
📢 *Bizning rasmiy kanallarimiz:*
🔹 Umra xizmatlari yangiliklari: {CHANNEL_UMRAJET}
🔹 Ravza tashriflari va aksiyalar: {CHANNEL_RAVZA}

Obuna bo‘ling va eng so‘nggi xabarlarni o‘tkazib yubormang!
        """,
        parse_mode="Markdown"
    )

# Xabarlarni qabul qilish va javob berish
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🕌 Ravzaga tashrif":
        discount_active = is_discount_active()
        price_viza = "10 SAR (aksiyada!)" if discount_active else "15 SAR"
        price_no_viza = "15 SAR (aksiyada!)" if discount_active else "20 SAR"

        await update.message.reply_text(
            f"""
*🕌 Ravzaga tashrif xizmati*

🔸 Viza bilan: {price_viza}
🔸 Vizasiz: {price_no_viza}

🎉 *Aksiya:* Bot ishga tushganidan keyingi 7 kun ichida har bir tashrif xizmati faqat {price_viza}!

💼 Ko‘p sonli buyurtmalarda qo‘shimcha chegirmalar mavjud.
💳 To‘lov: Uzcard / Humo / Visa / Crypto
📎 Hujjatni rasm yoki PDF ko‘rinishida yuboring.

📲 Bog‘lanish: {MANAGER_RAVZA}
            """,
            parse_mode="Markdown"
        )
    elif text == "📦 Umra paketlari":
        await update.message.reply_text(
            f"""
*📦 Umra paketlari*

🔹 Standard: 1100$ dan
🔹 VIP: 2000$ dan

Paketga quyidagilar kiradi:
✅ Vizani rasmiylashtirish
✅ Mehmonxona joyi (Makka/Madina)
✅ Transport xizmati
✅ Guruh ovqatlanishi
✅ Gid xizmati va yo‘l-yo‘riq

💳 To‘lov: Uzcard / Humo / Visa / Crypto
📲 Yordamchi: {MANAGER_ASSISTANT}
            """,
            parse_mode="Markdown"
        )
    elif text == "🏨 Mehmonxona/Hostel":
        await update.message.reply_text(
            f"""
*🏨 Mehmonxona va Hostel bron qilish*

📍 Makka va Madina shaharlarida barcha toifadagi mehmonxonalar mavjud.
📆 Qisqa yoki uzoq muddatli bron qilish imkoniyati.
🍽 3 mahal nonushta bilan yoki nonushtasiz variantlar mavjud.

📲 Bog‘lanish: {MANAGER_ASSISTANT}
            """,
            parse_mode="Markdown"
        )
    elif text == "🚆 Poezd chiptalari":
        await update.message.reply_text(
            f"""
*🚆 HHR Poezd chiptalari*

🔹 Yo‘nalishlar: Makkadan → Madina, Jidda, Yanbu va boshqa shaharlarga
📅 Buyurtma: Istalgan kunga
🪪 Faqat Saudiya vizasi bo‘lsa kifoya
💺 Ekanom / Biznes sinflar mavjud

📲 Buyurtma uchun: {MANAGER_ASSISTANT}
            """,
            parse_mode="Markdown"
        )
    elif text == "🚐 Transport xizmati":
        await update.message.reply_text(
            f"""
*🚐 Transport xizmati*

🚌 Avtobuslar, 🚙 GMC / Toyota, 🚖 VIP mashinalar
🏙 Makkaga olib kirish xizmati
🧑‍✈️ Tajribali haydovchilar bilan

📲 Buyurtma: {MANAGER_ASSISTANT}
            """,
            parse_mode="Markdown"
        )
    elif text == "🍱 Guruhlarga ovqat":
        await update.message.reply_text(
            f"""
*🍱 Guruhlarga ovqat xizmati*

👥 10-15 kishilik kamida buyurtmalar
🍛 Asosan o‘zbek taomlari
📦 1, 2, 3 mahal xizmatlar
🥂 VIP ziyofatlar ham tashkil qilinadi

📲 Bog‘lanish: {MANAGER_ASSISTANT}
            """,
            parse_mode="Markdown"
        )
    elif text == "✈️ Avia chiptalar":
        await update.message.reply_text(
            f"""
*✈️ Avia chiptalar xizmati*

🌍 Istalgan davlatga chipta bron qilish
💳 Vizali yoki vizasiz, muhim emas
📆 Xaridor istagan sana uchun

📲 Buyurtma: {MANAGER_ASSISTANT}
            """,
            parse_mode="Markdown"
        )
    elif text == "📞 Admin bilan bog‘lanish":
        await update.message.reply_text(
            f"""
*📞 Adminlar bilan bog‘lanish*

🕌 Ravza xizmatlari: {MANAGER_RAVZA}
📦 Boshqa xizmatlar: {MANAGER_ASSISTANT}
            """,
            parse_mode="Markdown"
        )
    elif text == "📢 Kanalimiz":
        await update.message.reply_text(
            f"""
*📢 Rasmiy kanallarimiz:*

✅ UmraJet yangiliklari: {CHANNEL_UMRAJET}
✅ Ravza tashrif xizmati: {CHANNEL_RAVZA}

Obuna bo‘ling va yangiliklardan xabardor bo‘ling!
            """,
            parse_mode="Markdown"
        )
    elif text == "🤖 Savol-javob & maslahat":
        await update.message.reply_text(
            f"""
*🤖 Umra bo‘yicha tez-tez so‘raladigan savollar:*

❓ *Vizasi bo‘lmagan kishi Ravzaga bora oladimi?*
✅ Ha, biz viza olgan holda tashrifni tashkil qilamiz.

❓ *Qanday to‘lov turlari bor?*
✅ Uzcard, Humo, Visa, Crypto.

❓ *Umra narxida nima kiradi?*
✅ Vizadan tortib mehmonxonagacha, barcha xizmatlar.

Agar boshqa savolingiz bo‘lsa, adminlar bilan bog‘laning:
📞 {MANAGER_RAVZA} | {MANAGER_ASSISTANT}
            """,
            parse_mode="Markdown"
        )
    else:
        await update.message.reply_text("Iltimos, menyudan biror xizmatni tanlang.")

# Bot komandalar menyusini sozlash
async def set_menu_commands(application):
    await application.bot.set_my_commands([
        BotCommand("start", "🔄 Botni qayta ishga tushirish"),
        BotCommand("ravza", "🕌 Ravzaga tashrif"),
        BotCommand("umra", "📦 Umra paketlari"),
        BotCommand("mehmonxona", "🏨 Mehmonxona/Hostel"),
        BotCommand("poezd", "🚆 Poezd chiptalari"),
        BotCommand("transport", "🚐 Transport xizmati"),
        BotCommand("ovqat", "🍱 Guruhlarga ovqat"),
        BotCommand("avia", "✈️ Avia chiptalar"),
        BotCommand("admin", "📞 Admin bilan bog‘lanish"),
        BotCommand("kanal", "📢 Rasmiy kanallar")
    ])

# Botni ishga tushirish
async def main():
    TOKEN = "7667056220:AAEc8DwQ0WJrBfVk_yLN8wLWGpxUfRKT-5A"  # Tokeningizni shu yerga joylashtiring

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    await set_menu_commands(application)
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
