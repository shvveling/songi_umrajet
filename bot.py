from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, BotCommand
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from datetime import datetime, timedelta

# Admin kontaktlari
MANAGER_RAVZA = "@vip_arabiy"
MANAGER_ASSISTANT = "@V001VB"
CHANNEL_UMRAJET = "@umrajet"
CHANNEL_RAVZA = "@the_ravza"

# Bot ishga tushgan sana (aksiyalar uchun)
BOT_START_DATE = datetime(2025, 6, 2)

def is_discount_active():
    return datetime.now() < BOT_START_DATE + timedelta(days=7)

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
        "*🕋 UmraJet — Premium xizmatlar bot 🤍*\n\n"
        "Assalomu alaykum va rahmatulloh! Sizga Saudiya Arabistoni Umra xizmatlari bo‘yicha professional yordam beramiz. Quyidagi bo‘limlardan keraklisini tanlang:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

    await update.message.reply_text(
        f"📢 *Bizning rasmiy kanallarimiz:*\n"
        f"🔹 Umra xizmatlari yangiliklari: {CHANNEL_UMRAJET}\n"
        f"🔹 Ravza tashriflari va aksiyalar: {CHANNEL_RAVZA}\n\n"
        "Obuna bo‘ling va eng so‘nggi xabarlarni o‘tkazib yubormang!",
        parse_mode="Markdown"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🕌 Ravzaga tashrif":
        discount_active = is_discount_active()
        price_viza = "10 SAR (aksiyada!)" if discount_active else "15 SAR"
        price_no_viza = "15 SAR (aksiyada!)" if discount_active else "20 SAR"

        await update.message.reply_text(
            f"*🕌 Ravzaga tashrif xizmati*\n\n"
            f"🔸 Viza bilan: {price_viza}\n"
            f"🔸 Vizasiz: {price_no_viza}\n\n"
            f"🎉 *Aksiya:* Bot ishga tushganidan keyingi 7 kun ichida har bir tashrif xizmati faqat {price_viza}!\n\n"
            "💼 Ko‘p sonli buyurtmalarda qo‘shimcha chegirmalar mavjud.\n"
            "💳 To‘lov: Uzcard / Humo / Visa / Crypto\n"
            "📎 Hujjatni rasm yoki PDF ko‘rinishida yuboring.\n\n"
            f"📲 Bog‘lanish: {MANAGER_RAVZA}",
            parse_mode="Markdown"
        )
    elif text == "📦 Umra paketlari":
        await update.message.reply_text(
            f"*📦 Umra paketlari*\n\n"
            f"🔹 Standard: 1100$ dan\n"
            f"🔹 VIP: 2000$ dan\n\n"
            "Paketga quyidagilar kiradi:\n"
            "✅ Vizani rasmiylashtirish\n"
            "✅ Mehmonxona joyi (Makka/Madina)\n"
            "✅ Transport xizmati\n"
            "✅ Guruh ovqatlanishi\n"
            "✅ Gid xizmati va yo‘l-yo‘riq\n\n"
            "💳 To‘lov: Uzcard / Humo / Visa / Crypto\n"
            f"📲 Yordamchi: {MANAGER_ASSISTANT}",
            parse_mode="Markdown"
        )
    elif text == "🏨 Mehmonxona/Hostel":
        await update.message.reply_text(
            f"*🏨 Mehmonxona va Hostel bron qilish*\n\n"
            "📍 Makka va Madina shaharlarida barcha toifadagi mehmonxonalar mavjud.\n"
            "📆 Qisqa yoki uzoq muddatli bron qilish imkoniyati.\n"
            "🍽 3 mahal nonushta bilan yoki nonushtasiz variantlar mavjud.\n\n"
            f"📲 Bog‘lanish: {MANAGER_ASSISTANT}",
            parse_mode="Markdown"
        )
    elif text == "🚆 Poezd chiptalari":
        await update.message.reply_text(
            f"*🚆 HHR Poezd chiptalari*\n\n"
            "🔹 Yo‘nalishlar: Makkadan → Madina, Jidda, Yanbu va boshqa shaharlarga\n"
            "📅 Buyurtma: Istalgan kunga\n"
            "🪪 Faqat Saudiya vizasi bo‘lsa kifoya\n"
            "💺 Ekanom / Biznes sinflar mavjud\n\n"
            f"📲 Buyurtma uchun: {MANAGER_ASSISTANT}",
            parse_mode="Markdown"
        )
    elif text == "🚐 Transport xizmati":
        await update.message.reply_text(
            f"*🚐 Transport xizmati*\n\n"
            "🚌 Avtobuslar, 🚙 GMC / Toyota, 🚖 VIP mashinalar\n"
            "🏙 Makkaga olib kirish xizmati\n"
            "🧑‍✈️ Tajribali haydovchilar bilan\n\n"
            f"📲 Buyurtma: {MANAGER_ASSISTANT}",
            parse_mode="Markdown"
        )
    elif text == "🍱 Guruhlarga ovqat":
        await update.message.reply_text(
            f"*🍱 Guruhlarga ovqat xizmati*\n\n"
            "👥 10-15 kishilik kamida buyurtmalar\n"
            "🍛 Asosan o‘zbek taomlari\n"
            "📦 1, 2, 3 mahal xizmatlar\n"
            "🥂 VIP ziyofatlar ham tashkil qilinadi\n\n"
            f"📲 Bog‘lanish: {MANAGER_ASSISTANT}",
            parse_mode="Markdown"
        )
    elif text == "✈️ Avia chiptalar":
        await update.message.reply_text(
            f"*✈️ Avia chiptalar xizmati*\n\n"
            "🌍 Istalgan davlatga chipta bron qilish\n"
            "💳 Vizali yoki vizasiz, muhim emas\n"
            "📆 Xaridor istagan sana uchun\n\n"
            f"📲 Buyurtma: {MANAGER_ASSISTANT}",
            parse_mode="Markdown"
        )
    elif text == "📞 Admin bilan bog‘lanish":
        await update.message.reply_text(
            f"*📞 Adminlar bilan bog‘lanish*\n\n"
            f"🕌 Ravza xizmatlari: {MANAGER_RAVZA}\n"
            f"📦 Boshqa xizmatlar: {MANAGER_ASSISTANT}",
            parse_mode="Markdown"
        )
    elif text == "📢 Kanalimiz":
        await update.message.reply_text(
            f"*📢 Rasmiy kanallarimiz:*\n\n"
            f"✅ UmraJet yangiliklari: {CHANNEL_UMRAJET}\n"
            f"✅ Ravza tashrif xizmati: {CHANNEL_RAVZA}\n\n"
            "Obuna bo‘ling va yangiliklardan xabardor bo‘ling!",
            parse_mode="Markdown"
        )
    elif text == "🤖 Savol-javob & maslahat":
        await update.message.reply_text(
            "*🤖 Umra bo‘yicha tez-tez so‘raladigan savollar:*\n\n"
            "❓ *Vizasi bo‘lmagan kishi Ravzaga bora oladimi?*\n"
            "✅ Ha, biz viza olgan holda tashrifni tashkil qilamiz.\n\n"
            "❓ *Qanday to‘lov turlari bor?*\n"
            "✅ Uzcard, Humo, Visa, Crypto.\n\n"
            "❓ *Umra narxida nima kiradi?*\n"
            "✅ Vizadan tortib mehmonxonagacha, barcha xizmatlar.\n\n"
            f"Agar boshqa savolingiz bo‘lsa, adminlar bilan bog‘laning:\n"
            f"📞 {MANAGER_RAVZA} | {MANAGER_ASSISTANT}",
            parse_mode="Markdown"
        )
    else:
        await update.message.reply_text("Iltimos, menyudan biror xizmatni tanlang.")

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

if __name__ == "__main__":
    from telegram.ext import Application, CommandHandler, MessageHandler, filters
    import asyncio

    TOKEN = "7667056220:AAEc8DwQ0WJrBfVk_yLN8wLWGpxUfRKT-5A"

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    asyncio.run(set_menu_commands(application))

    application.run_polling()
