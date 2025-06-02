import os
import asyncio
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, BotCommand
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from datetime import datetime, timedelta

# --- YUKLANISHLAR --- #
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN topilmadi! .env faylni tekshiring.")

# --- ADMIN KONTAKTLAR --- #
MANAGER_RAVZA = "@vip_arabiy"
MANAGER_ASSISTANT = "@V001VB"
CHANNEL_UMRAJET = "@umrajet"
CHANNEL_RAVZA = "@the_ravza"

# --- AKSIYA MUDDATI --- #
BOT_START_DATE = datetime(2025, 6, 2)

def is_discount_active():
    return datetime.now() < BOT_START_DATE + timedelta(days=7)

# --- START KOMANDASI --- #
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("🍇 Ravzaga tashrif"), KeyboardButton("🕋 Umra paketlari")],
        [KeyboardButton("🏨 Mehmonxona/Hostel"), KeyboardButton("🚄 Poezd chiptalari")],
        [KeyboardButton("🚐 Transport xizmati"), KeyboardButton("🍽 Guruh ovqatlari")],
        [KeyboardButton("✈️ Avia chiptalar"), KeyboardButton("📞 Admin bilan bog‘lanish")],
        [KeyboardButton("📢 Rasmiy kanallar"), KeyboardButton("💬 Yordamchi AI")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        """
🤍 *UmraJet — Premium Umra xizmatlari markazi* 🤍

Assalomu alaykum!
Sizga qulaylik yaratish uchun quyidagi xizmatlardan birini tanlang:
        """,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# --- XABARLARGA JAVOB BERISH --- #
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    discount_active = is_discount_active()

    if text == "🍇 Ravzaga tashrif":
        price_viza = "10 SAR (aksiyada!)" if discount_active else "15 SAR"
        price_no_viza = "15 SAR (aksiyada!)" if discount_active else "20 SAR"

        await update.message.reply_text(f"""
🍇 *Ravzaga tashrif xizmati* — Ruhiy yangilanish manbai

🔹 *Viza bilan:* {price_viza}
🔹 *Vizasiz:* {price_no_viza}

🎁 *Chegirma:* Bot ishga tushganidan keyingi 7 kun davomida maxsus narxlar
📌 *Xizmat turi:* Jamoaviy yoki shaxsiy tashriflar
💳 *To‘lov:* Uzcard / Humo / Visa / Crypto

📄 *Hujjat yuboring:* Rasm yoki PDF ko‘rinishida
📞 *Bog‘lanish:* {MANAGER_RAVZA} yoki {MANAGER_ASSISTANT}
        """, parse_mode="Markdown")

    elif text == "🕋 Umra paketlari":
        await update.message.reply_text(f"""
🕋 *Umra paketlari — Armon emas, imkon!* 🌙

✨ *Standard:* 1100$ dan
✨ *VIP:* 2000$ dan

Paketga quyidagilar kiradi:
✅ Vizani rasmiylashtirish
✅ Mehmonxona
✅ Transport
✅ Gid xizmatlari
✅ Guruh uchun ovqat

💳 *To‘lov:* Uzcard / Humo / Visa / Crypto
📞 *Bog‘lanish:* {MANAGER_ASSISTANT} yoki {MANAGER_RAVZA}
        """, parse_mode="Markdown")

    elif text == "🏨 Mehmonxona/Hostel":
        await update.message.reply_text(f"""
🏨 *Mehmonxona va Hostel bron qilish* 🛏

📍 Makka va Madina markazlarida joylashgan
🕰 Har qanday muddatga
🍴 Ovqatli yoki ovqatsiz

💼 Ishonchli xizmat va xavfsizlik kafolati
📞 Aloqa: {MANAGER_ASSISTANT}
        """, parse_mode="Markdown")

    elif text == "🚄 Poezd chiptalari":
        await update.message.reply_text(f"""
🚄 *HHR Poezd chiptalari* 🚅

📍 Yo‘nalishlar: Makka, Madina va boshqa shaharlar
🕓 Buyurtma: Istalgan kunga
💺 Joylar: Ekanom / Biznes

🛂 Faqat viza bo‘lishi kifoya
📞 Bog‘lanish: {MANAGER_ASSISTANT}
        """, parse_mode="Markdown")

    elif text == "🚐 Transport xizmati":
        await update.message.reply_text(f"""
🚐 *Shaxsiy va guruh transporti* 🚖

🚍 Avtobus, Toyota, VIP mashinalar
🏘 Mehmonxonadan masjidlargacha yetkazish
👨‍✈️ Tajribali haydovchilar

📞 Buyurtma uchun: {MANAGER_ASSISTANT}
        """, parse_mode="Markdown")

    elif text == "🍽 Guruh ovqatlari":
        await update.message.reply_text(f"""
🍽 *10+ kishilik guruh ovqatlari* 🍛

🥘 O‘zbekcha taomlar
🍱 1, 2 yoki 3 mahal
🎉 Ziyofatlar uchun maxsus menyular

📞 Bog‘lanish: {MANAGER_ASSISTANT}
        """, parse_mode="Markdown")

    elif text == "✈️ Avia chiptalar":
        await update.message.reply_text(f"""
✈️ *Avia chiptalar — Istalgan manzilga* 🌍

📆 Istalgan sana, istalgan davlat
🛂 Vizali yoki vizasiz variantlar

📞 Buyurtma: {MANAGER_ASSISTANT} yoki {MANAGER_RAVZA}
        """, parse_mode="Markdown")

    elif text == "📞 Admin bilan bog‘lanish":
        await update.message.reply_text(f"""
📞 *Adminlar bilan to‘g‘ridan-to‘g‘ri bog‘laning:*

🍇 Ravza xizmatlari: {MANAGER_RAVZA}
🕋 Umra & boshqa xizmatlar: {MANAGER_ASSISTANT}
        """, parse_mode="Markdown")

    elif text == "📢 Rasmiy kanallar":
        await update.message.reply_text(f"""
📢 *Rasmiy axborot manbalarimiz:*

✅ UmraJet yangiliklari: {CHANNEL_UMRAJET}
✅ Ravza tashriflari: {CHANNEL_RAVZA}
        """, parse_mode="Markdown")

    elif text == "💬 Yordamchi AI":
        await update.message.reply_text("""
🧠 *AI yordamchi* faollashtirildi. Endi oddiy savollarni yozing, va javob olasiz.
(Masalan: "Umra necha kun davom etadi?" yoki "Vizasiz Ravzaga bora olamanmi?")
        """, parse_mode="Markdown")

    else:
        # AI YORDAMCHI — sodda versiya, API talab qilmaydi
        lower = text.lower()
        if "ravza" in lower:
            await update.message.reply_text("✅ Ha, vizasiz ham Ravzaga olib kiramiz.")
        elif "umra" in lower:
            await update.message.reply_text("🕋 Umra xizmatimiz to‘liq paketdan iborat — sizga faqat pasport yetarli.")
        elif "to‘lov" in lower or "tolov" in lower:
            await update.message.reply_text("💳 To‘lov: Uzcard, Humo, Visa, yoki Crypto orqali amalga oshiriladi.")
        else:
            await update.message.reply_text("🤖 Savolingizni tushunmadim. Iltimos, aniqroq yozing yoki menyudan xizmat tanlang.")

# --- KOMANDALAR MENYUSI --- #
async def set_menu_commands(application):
    await application.bot.set_my_commands([
        BotCommand("start", "🔄 Botni qayta ishga tushirish"),
    ])

# --- ASOSIY FUNKSIYA --- #
async def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    await set_menu_commands(application)
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
