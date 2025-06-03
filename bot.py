import os
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, BotCommand
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

# Muhit o'zgaruvchilarini yuklash
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN topilmadi! .env faylni tekshiring.")

# Kontaktlar
MANAGER_RAVZA = "@vip_arabiy"
MANAGER_ASSISTANT = "@V001VB"
CHANNEL_UMRAJET = "@umrajet"
CHANNEL_RAVZA = "@the_ravza"

# Start komandasi
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
        "Assalomu alaykum!\n"
        "Sizga qulaylik yaratish uchun xizmat turini tanlang:",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

# Har bir xizmat uchun alohida javob
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if text == "🍇 Ravzaga tashrif":
        await update.message.reply_text(
            "🍇 *Ravzaga tashrif xizmati*\n\n"
            "🔹 Vizali va vizasiz yuruvchilar uchun\n"
            "🔹 Jamoaviy yoki yakka tashrif imkoniyati\n"
            "🔹 Rasm/PDF hujjat yuboring — ro‘yxatga olinadi\n\n"
            "💳 To‘lov: Uzcard / Humo / Visa / Crypto\n\n"
            f"📞 Bog‘lanish: {MANAGER_RAVZA} | {MANAGER_ASSISTANT}",
            parse_mode="Markdown"
        )

    elif text == "🕋 Umra paketlari":
        await update.message.reply_text(
            "🕋 *Umra paketlari — Armon emas, imkon!* 🌙\n\n"
            "✨ Standard: 1100$ dan\n"
            "✨ VIP: 2000$ dan\n\n"
            "📦 Paketda:\n"
            "• Viza\n• Mehmonxona\n• Transport\n• Gid xizmatlari\n• Ovqatlanish\n\n"
            f"📞 Bog‘lanish: {MANAGER_ASSISTANT} | {MANAGER_RAVZA}",
            parse_mode="Markdown"
        )

    elif text == "🏨 Mehmonxona/Hostel":
        await update.message.reply_text(
            "🏨 *Makka & Madinadagi mehmonxonalar*\n\n"
            "📍 Markaziy joylashuv\n"
            "🕰 Mos muddatga bron qilish\n"
            "🍴 Ovqatli yoki ovqatsiz variantlar\n\n"
            f"📞 Aloqa: {MANAGER_ASSISTANT} | {MANAGER_RAVZA}",
            parse_mode="Markdown"
        )

    elif text == "🚄 Poezd chiptalari":
        await update.message.reply_text(
            "🚄 *HHR Poezd chiptalari* 🚅\n\n"
            "📍 Yo‘nalishlar: Makka ↔ Madina\n"
            "💺 Ekanom va Biznes klass\n"
            "🛂 Vizangiz bo‘lsa kifoya\n\n"
            f"📞 Buyurtma: {MANAGER_ASSISTANT} | {MANAGER_RAVZA}",
            parse_mode="Markdown"
        )

    elif text == "🚐 Transport xizmati":
        await update.message.reply_text(
            "🚐 *Shaxsiy va guruh transporti* 🚖\n\n"
            "🚌 Avtobus, Toyota, VIP avtomobillar\n"
            "🏘 Mehmonxonadan masjidlargacha\n"
            "👨‍✈️ Haydovchilar tajribali\n\n"
            f"📞 Bog‘lanish: {MANAGER_ASSISTANT} | {MANAGER_RAVZA}",
            parse_mode="Markdown"
        )

    elif text == "🍽 Guruh ovqatlari":
        await update.message.reply_text(
            "🍽 *Guruh ovqatlanish xizmati* 🍛\n\n"
            "🥘 O‘zbekcha menyular\n"
            "🍱 1, 2, yoki 3 mahal ovqat\n"
            "🎉 Maxsus ziyofatlar uchun ham\n\n"
            f"📞 Aloqa: {MANAGER_ASSISTANT} | {MANAGER_RAVZA}",
            parse_mode="Markdown"
        )

    elif text == "✈️ Avia chiptalar":
        await update.message.reply_text(
            "✈️ *Avia chiptalar — Butun dunyo bo‘ylab* 🌍\n\n"
            "📆 Sana: Siz istagan vaqtda\n"
            "🛫 Yo‘nalish: Har qanday davlatga\n"
            "🛂 Vizasiz ham variantlar mavjud\n\n"
            f"📞 Bog‘lanish: {MANAGER_ASSISTANT} | {MANAGER_RAVZA}",
            parse_mode="Markdown"
        )

    elif text == "📞 Admin bilan bog‘lanish":
        await update.message.reply_text(
            "📞 *Adminlar bilan bog‘lanish:*\n\n"
            f"🍇 Ravza xizmatlari: {MANAGER_RAVZA}\n"
            f"🕋 Umra & boshqa xizmatlar: {MANAGER_ASSISTANT}",
            parse_mode="Markdown"
        )

    elif text == "📢 Rasmiy kanallar":
        await update.message.reply_text(
            "📢 *Rasmiy kanallarimiz:*\n\n"
            f"🔔 UmraJet: {CHANNEL_UMRAJET}\n"
            f"🔔 Ravza tashriflari: {CHANNEL_RAVZA}",
            parse_mode="Markdown"
        )

    else:
        await update.message.reply_text(
            "🤖 Iltimos, menyudan biror xizmat tanlang.",
            parse_mode="Markdown"
        )

# Menyu komandalar
async def set_menu(application: Application):
    await application.bot.set_my_commands([
        BotCommand("start", "🔄 Botni qayta ishga tushirish")
    ])

def main():
    app = Application.builder().token(TOKEN).post_init(set_menu).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
