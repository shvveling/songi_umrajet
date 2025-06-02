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
        "\U0001F54C *UmraJet — Premium xizmatlar botiga xush kelibsiz!* 🤍\n\n"
        "Biz orqali siz Umra va Ravza tashrifi, transport, mehmonxona, chipta va boshqa ko‘plab xizmatlardan foydalanishingiz mumkin.\n\n"
        "Quyidagi menyudan kerakli xizmatni tanlang:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🕌 Ravzaga tashrif":
        await update.message.reply_text(
            "🕌 *Ravzaga tashrif xizmati*\n\n"
            "🔹 Viza bilan: *15 SAR*\n"
            "🔹 Vizasiz: *20 SAR*\n"
            "📉 Guruhli buyurtmalarda chegirmalar mavjud!\n\n"
            "💳 To‘lov: Uzcard / Humo / Visa / Crypto\n"
            "📎 Hujjatni rasm yoki PDF ko‘rinishida yuboring.\n"
            f"📲 Bog‘lanish: {MANAGER_RAVZA}",
            parse_mode="Markdown"
        )

    elif text == "📦 Umra paketlari":
        await update.message.reply_text(
            "📦 *Umra paketlari*\n\n"
            "🔸 *Standard paket* — 1100$ dan boshlanadi (avia, mehmonxona, transfer, viza, taomlar)\n"
            "🔸 *VIP paket* — 2000$ dan (premium xizmatlar bilan)\n\n"
            "✅ Har bir paketga to‘liq xizmatlar kiritilgan.\n"
            "🕋 Makka va Madina uchun alohida tanlovlar mavjud.\n\n"
            "📌 Tafsilotlar va buyurtma uchun bog‘laning:"
            f"\n📲 {MANAGER_ASSISTANT}",
            parse_mode="Markdown"
        )

    elif text == "🏨 Mehmonxona/Hostel":
        await update.message.reply_text(
            "🏨 *Mehmonxona va hostel xizmatlari*\n\n"
            "📍 Makka, Madina va boshqa shaharlarda mavjud.\n"
            "⏳ Uzoq va qisqa muddatli turar joylar.\n"
            "🥣 3 mahal nonushta xizmati qo‘shilishi mumkin.\n"
            "💰 Narxlar ehtiyoj va joylashuvga qarab farqlanadi.\n\n"
            f"📲 Bog‘lanish: {MANAGER_ASSISTANT}",
            parse_mode="Markdown"
        )

    elif text == "🚆 Poezd chiptalari":
        await update.message.reply_text(
            "🚆 *HHR (Haramain) Poezd chiptalari*\n\n"
            "📍 Yo‘nalishlar: Makka — Madina — Jidda — KAEC\n"
            "💼 Ekanom va biznes klass mavjud.\n"
            "🗓 Istalgan sana uchun zakaz qilish mumkin.\n"
            "📎 Faqat Saudiya vizasi talab etiladi.\n\n"
            f"📲 Bog‘lanish: {MANAGER_ASSISTANT}",
            parse_mode="Markdown"
        )

    elif text == "🚐 Transport xizmati":
        await update.message.reply_text(
            "🚐 *Transport xizmatlari*\n\n"
            "🚖 Avtobuslar, GMC, Toyota va VIP mashinalar mavjud.\n"
            "🕋 Makkaga olib kirish xizmati mavjud.\n"
            "👨‍✈️ Haydovchilar xizmat bilan birga taqdim etiladi.\n\n"
            f"📲 Tafsilotlar uchun: {MANAGER_ASSISTANT}",
            parse_mode="Markdown"
        )

    elif text == "🍱 Guruhlarga ovqat":
        await update.message.reply_text(
            "🍱 *Guruhlar uchun ovqat yetkazish*\n\n"
            "👥 Kamida 10–15 kishilik buyurtmalar qabul qilinadi.\n"
            "🍲 O‘zbek taomlari, VIP ziyofatlar tashkil qilish mumkin.\n"
            "📅 1, 2, 3 mahal bo‘yicha buyurtmalar olinadi.\n\n"
            f"📲 Tafsilotlar: {MANAGER_ASSISTANT}",
            parse_mode="Markdown"
        )

    elif text == "✈️ Avia chiptalar":
        await update.message.reply_text(
            "✈️ *Avia chipta bron qilish xizmati*\n\n"
            "🌍 Har qanday davlatga avia chipta buyurtma qilishingiz mumkin.\n"
            "📅 Sana va yo‘nalishga mos takliflar.\n"
            "💼 Vizali yoki vizasiz farqi yo‘q.\n\n"
            f"📲 Buyurtma uchun: {MANAGER_ASSISTANT}",
            parse_mode="Markdown"
        )

    elif text == "📞 Admin bilan bog‘lanish":
        await update.message.reply_text(
            "📞 *Administratorlar bilan bog‘lanish*\n\n"
            f"🕌 Ravza xizmatlari: {MANAGER_RAVZA}\n"
            f"📦 Umra, transport, chipta va boshqa xizmatlar: {MANAGER_ASSISTANT}",
            parse_mode="Markdown"
        )

    else:
        await update.message.reply_text("Iltimos, menyudan kerakli xizmatni tanlang.")

def main():
    application = Application.builder().token("7667056220:AAEc8DwQ0WJrBfVk_yLN8wLWGpxUfRKT-5A").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()

if __name__ == "__main__":
    main()
