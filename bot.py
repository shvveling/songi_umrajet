import os
from datetime import datetime, timedelta
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, BotCommand
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

# --- Muhit o'zgaruvchilarini yuklash ---
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN topilmadi! .env faylni tekshiring.")

# --- Admin kontaklar ---
MANAGER_RAVZA = "@vip_arabiy"
MANAGER_ASSISTANT = "@V001VB"
CHANNEL_UMRAJET = "@umrajet"
CHANNEL_RAVZA = "@the_ravza"

# --- Aksiya muddati boshlanish sanasi ---
BOT_START_DATE = datetime(2025, 6, 2)

def is_discount_active() -> bool:
    return datetime.now() < BOT_START_DATE + timedelta(days=7)

# --- Start komandasi ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("🍇 Ravzaga tashrif"), KeyboardButton("🕋 Umra paketlari")],
        [KeyboardButton("🏨 Mehmonxona/Hostel"), KeyboardButton("🚄 Poezd chiptalari")],
        [KeyboardButton("🚐 Transport xizmati"), KeyboardButton("🍽 Guruh ovqatlari")],
        [KeyboardButton("✈️ Avia chiptalar"), KeyboardButton("📞 Admin bilan bog‘lanish")],
        [KeyboardButton("📢 Rasmiy kanallar"), KeyboardButton("💬 Yordamchi AI")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)

    await update.message.reply_text(
        "🤍 *UmraJet — Premium Umra xizmatlari markazi* 🤍\n\n"
        "Assalomu alaykum!\n"
        "Sizga qulaylik yaratish uchun quyidagi xizmatlardan birini tanlang:",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

# --- Har bir xizmat uchun alohida funksiya --- #
async def ravza_service(update: Update):
    discount_active = is_discount_active()
    price_viza = "10 SAR (aksiyada!)" if discount_active else "15 SAR"
    price_no_viza = "15 SAR (aksiyada!)" if discount_active else "20 SAR"

    await update.message.reply_text(
        f"🍇 *Ravzaga tashrif xizmati* — Ruhiy yangilanish manbai\n\n"
        f"🔹 *Viza bilan:* {price_viza}\n"
        f"🔹 *Vizasiz:* {price_no_viza}\n\n"
        "🎁 *Chegirma:* Bot ishga tushganidan keyingi 7 kun davomida maxsus narxlar\n"
        "📌 *Xizmat turi:* Jamoaviy yoki shaxsiy tashriflar\n"
        "💳 *To‘lov:* Uzcard / Humo / Visa / Crypto\n\n"
        "📄 *Hujjat yuboring:* Rasm yoki PDF ko‘rinishida\n"
        f"📞 *Bog‘lanish:* {MANAGER_RAVZA} yoki {MANAGER_ASSISTANT}",
        parse_mode="Markdown"
    )

async def umra_packages(update: Update):
    await update.message.reply_text(
        "🕋 *Umra paketlari — Armon emas, imkon!* 🌙\n\n"
        "✨ *Standard:* 1100$ dan\n"
        "✨ *VIP:* 2000$ dan\n\n"
        "Paketga quyidagilar kiradi:\n"
        "✅ Vizani rasmiylashtirish\n"
        "✅ Mehmonxona\n"
        "✅ Transport\n"
        "✅ Gid xizmatlari\n"
        "✅ Guruh uchun ovqat\n\n"
        "💳 *To‘lov:* Uzcard / Humo / Visa / Crypto\n"
        f"📞 *Bog‘lanish:* {MANAGER_ASSISTANT} yoki {MANAGER_RAVZA}",
        parse_mode="Markdown"
    )

async def hotels(update: Update):
    await update.message.reply_text(
        "🏨 *Mehmonxona va Hostel bron qilish* 🛏\n\n"
        "📍 Makka va Madina markazlarida joylashgan\n"
        "🕰 Har qanday muddatga\n"
        "🍴 Ovqatli yoki ovqatsiz\n\n"
        "💼 Ishonchli xizmat va xavfsizlik kafolati\n"
        f"📞 Aloqa: {MANAGER_ASSISTANT}",
        parse_mode="Markdown"
    )

async def train_tickets(update: Update):
    await update.message.reply_text(
        "🚄 *HHR Poezd chiptalari* 🚅\n\n"
        "📍 Yo‘nalishlar: Makka, Madina va boshqa shaharlar\n"
        "🕓 Buyurtma: Istalgan kunga\n"
        "💺 Joylar: Ekanom / Biznes\n\n"
        "🛂 Faqat viza bo‘lishi kifoya\n"
        f"📞 Bog‘lanish: {MANAGER_ASSISTANT}",
        parse_mode="Markdown"
    )

async def transport_service(update: Update):
    await update.message.reply_text(
        "🚐 *Shaxsiy va guruh transporti* 🚖\n\n"
        "🚍 Avtobus, Toyota, VIP mashinalar\n"
        "🏘 Mehmonxonadan masjidlargacha yetkazish\n"
        "👨‍✈️ Tajribali haydovchilar\n\n"
        f"📞 Buyurtma uchun: {MANAGER_ASSISTANT}",
        parse_mode="Markdown"
    )

async def group_food(update: Update):
    await update.message.reply_text(
        "🍽 *10+ kishilik guruh ovqatlari* 🍛\n\n"
        "🥘 O‘zbekcha taomlar\n"
        "🍱 1, 2 yoki 3 mahal\n"
        "🎉 Ziyofatlar uchun maxsus menyular\n\n"
        f"📞 Bog‘lanish: {MANAGER_ASSISTANT}",
        parse_mode="Markdown"
    )

async def plane_tickets(update: Update):
    await update.message.reply_text(
        "✈️ *Avia chiptalar — Istalgan manzilga* 🌍\n\n"
        "📆 Istalgan sana, istalgan davlat\n"
        "🛂 Vizali yoki vizasiz variantlar\n\n"
        f"📞 Buyurtma: {MANAGER_ASSISTANT} yoki {MANAGER_RAVZA}",
        parse_mode="Markdown"
    )

async def admin_contacts(update: Update):
    await update.message.reply_text(
        "📞 *Adminlar bilan to‘g‘ridan-to‘g‘ri bog‘laning:*\n\n"
        f"🍇 Ravza xizmatlari: {MANAGER_RAVZA}\n"
        f"🕋 Umra & boshqa xizmatlar: {MANAGER_ASSISTANT}",
        parse_mode="Markdown"
    )

async def official_channels(update: Update):
    await update.message.reply_text(
        "📢 *Rasmiy axborot manbalarimiz:*\n\n"
        f"✅ UmraJet yangiliklari: {CHANNEL_UMRAJET}\n"
        f"✅ Ravza tashriflari: {CHANNEL_RAVZA}",
        parse_mode="Markdown"
    )

async def ai_helper_intro(update: Update):
    await update.message.reply_text(
        "🧠 *AI yordamchi* faollashtirildi. Endi oddiy savollarni yozing, va javob olasiz.\n"
        "(Masalan: \"Umra necha kun davom etadi?\" yoki \"Vizasiz Ravzaga bora olamanmi?\")",
        parse_mode="Markdown"
    )

# --- AI yordamchi (oddiy, to‘liq emas) --- #
async def ai_helper(update: Update, text: str):
    lower = text.lower()
    if "ravza" in lower:
        await update.message.reply_text("✅ Ha, vizasiz ham Ravzaga olib kiramiz.")
    elif "umra" in lower:
        await update.message.reply_text("🕋 Umra xizmatimiz to‘liq paketdan iborat — sizga faqat pasport yetarli.")
    elif "to‘lov" in lower or "tolov" in lower:
        await update.message.reply_text("💳 To‘lov: Uzcard, Humo, Visa, yoki Crypto orqali amalga oshiriladi.")
    else:
        await update.message.reply_text("🤖 Savolingizni tushunmadim. Iltimos, aniqroq yozing yoki menyudan xizmat tanlang.")

# --- Xabarlarni qayta ishlovchi funksiya --- #
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "🍇 Ravzaga tashrif":
        await ravza_service(update)
    elif text == "🕋 Umra paketlari":
        await umra_packages(update)
    elif text == "🏨 Mehmonxona/Hostel":
        await hotels(update)
    elif text == "🚄 Poezd chiptalari":
        await train_tickets(update)
    elif text == "🚐 Transport xizmati":
        await transport_service(update)
    elif text == "🍽 Guruh ovqatlari":
        await group_food(update)
    elif text == "✈️ Avia chiptalar":
        await plane_tickets(update)
    elif text == "📞 Admin bilan bog‘lanish":
        await admin_contacts(update)
    elif text == "📢 Rasmiy kanallar":
        await official_channels(update)
    elif text == "💬 Yordamchi AI":
        await ai_helper_intro(update)
    else:
        # AI yordamchi oddiy savollarga javob beradi
        await ai_helper(update, text)

# --- Bot komandalarini sozlash ---
async def set_menu_commands(application: Application):
    await application.bot.set_my_commands([
        BotCommand("start", "🔄 Botni qayta ishga tushirish"),
    ])

def main():
    application = Application.builder().token(TOKEN).post_init(set_menu_commands).build()

    # Handlerlarni qo‘shish
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Botni ishga tushirish
    application.run_polling()
