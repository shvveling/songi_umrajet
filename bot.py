import os
import asyncio
from datetime import datetime, timedelta
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, BotCommand
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

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
BOT_START_DATE = datetime(2025, 6, 2)

# 7 kunlik aksiya tekshiruvi
def is_discount_active():
    return datetime.now() < BOT_START_DATE + timedelta(days=7)

# Asosiy menyu
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("🍃 Ravzaga tashrif"), KeyboardButton("🕋 Umra paketlari")],
        [KeyboardButton("🏨 Mehmonxonalar"), KeyboardButton("🚄 Poezd chiptalari")],
        [KeyboardButton("🚐 Premium transport"), KeyboardButton("🍽 Guruh ovqatlari")],
        [KeyboardButton("🛫 Avia chiptalar"), KeyboardButton("📞 Admin bilan bog‘lanish")],
        [KeyboardButton("📢 Rasmiy kanallar"), KeyboardButton("🧠 AI yordamchi")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        f"""
🌟 *UmraJet — Premium Umra xizmatlari* 🌟

Assalomu alaykum, {update.effective_user.first_name}!

Biz orqali siz eng ishonchli, qulay va tezkor xizmatlardan foydalanishingiz mumkin. Quyidagi bo‘limlardan birini tanlang 👇
        """,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# Xabarlar uchun asosiy handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    discount = is_discount_active()

    if text == "🍃 Ravzaga tashrif":
        viza_price = "10 SAR (aksiyada!)" if discount else "15 SAR"
        no_viza_price = "15 SAR (aksiyada!)" if discount else "20 SAR"

        await update.message.reply_text(f"""
🌿 *Ravzaga tashrif* — qalbingizga yaqin yo‘l ✨

🎫 *Viza bilan*: {viza_price}
🛂 *Vizasiz*: {no_viza_price}

📆 *Aksiya!* Faqat 7 kun davomida chegirmali narxlarda xizmatlardan foydalaning!
📄 Hujjatlarni rasm yoki PDF ko‘rinishida yuboring.
💳 To‘lov: Uzcard, Humo, Visa, Crypto

📞 Bog‘lanish: {MANAGER_RAVZA} | {MANAGER_ASSISTANT}
        """, parse_mode="Markdown")

    elif text == "🕋 Umra paketlari":
        await update.message.reply_text(f"""
🕋 *Umra paketlari — Standard va VIP* 🌍

🔹 *Standard paket*: 1100$ dan boshlab
🔸 *VIP paket*: 2000$ dan boshlab

✅ Viza
✅ Mehmonxona
✅ Transport
✅ Ovqatlanish
✅ Gid xizmati

💳 To‘lov: Uzcard / Humo / Visa / Crypto
📲 Murojaat: {MANAGER_ASSISTANT}
        """, parse_mode="Markdown")

    elif text == "🏨 Mehmonxonalar":
        await update.message.reply_text(f"""
🏨 *Mehmonxona va Hostel bron qilish*

📍 Makka & Madina shaharlarida joylashgan
🛏 3 yulduzdan 5 yulduzgacha
🍽 Ovqatli va ovqatsiz variantlar
📅 Istalgan muddatga bron qilish

📲 Bog‘lanish: {MANAGER_ASSISTANT}
        """, parse_mode="Markdown")

    elif text == "🚄 Poezd chiptalari":
        await update.message.reply_text(f"""
🚄 *HHR Poezd chiptalari* — qulay, tez va ishonchli

📍 Yo‘nalish: Makka ↔ Madina
🗓 Istalgan kunga bron
💺 Ekanom / Biznes sinf

📲 Buyurtma: {MANAGER_ASSISTANT}
        """, parse_mode="Markdown")

    elif text == "🚐 Premium transport":
        await update.message.reply_text(f"""
🚐 *Shaxsiy va guruh transport xizmatlari*

🚖 VIP avtomobillar
🚌 Avtobuslar / Minivenlar
🏠 Aeroportdan olib kirish
👨‍✈️ Tajribali haydovchilar

📲 Buyurtma: {MANAGER_ASSISTANT}
        """, parse_mode="Markdown")

    elif text == "🍽 Guruh ovqatlari":
        await update.message.reply_text(f"""
🍽 *10+ kishilik guruhlarga ovqat yetkazib berish*

🍛 Milliy va xalqaro menyular
🕰 1 mahal, 2 mahal, 3 mahal variantlar
🎉 VIP ziyofatlar uchun alohida xizmat

📲 Buyurtma: {MANAGER_ASSISTANT}
        """, parse_mode="Markdown")

    elif text == "🛫 Avia chiptalar":
        await update.message.reply_text(f"""
🛫 *Xalqaro avia chiptalar*

🌍 Istalgan yo‘nalishga
🛂 Vizali / vizasiz qatnovlar
📆 Mos sanalarni tanlash imkoniyati

📲 Buyurtma: {MANAGER_ASSISTANT}
        """, parse_mode="Markdown")

    elif text == "📞 Admin bilan bog‘lanish":
        await update.message.reply_text(f"""
📞 *Administratorlar bilan bog‘lanish:*

📍 Ravza xizmatlari: {MANAGER_RAVZA}
📍 Umra va boshqa xizmatlar: {MANAGER_ASSISTANT}
        """, parse_mode="Markdown")

    elif text == "📢 Rasmiy kanallar":
        await update.message.reply_text(f"""
📢 *Bizning rasmiy kanallarimiz:*

🔗 UmraJet yangiliklari: {CHANNEL_UMRAJET}
🔗 Ravza tashriflari: {CHANNEL_RAVZA}
        """, parse_mode="Markdown")

    elif text == "🧠 AI yordamchi":
        await update.message.reply_text("""
🧠 *AI Yordamchi (beta)*

Savolingizni yozing, biz sun’iy intellekt asosida javob beramiz!
(Bu demo versiyada API ishlatilmaydi)
        """, parse_mode="Markdown")

    else:
        await update.message.reply_text("🤖 Savolingiz uchun rahmat! Biz tez orada sizga javob beramiz yoki menyudan xizmatni tanlang.")

# Komandalar menyusi
async def set_menu_commands(application):
    await application.bot.set_my_commands([
        BotCommand("start", "🔄 Botni qayta ishga tushirish")
    ])

# Botni ishga tushirish
def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == "__main__":
    main()
