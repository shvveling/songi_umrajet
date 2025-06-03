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

# --- Aksiya muddati ---
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
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "🤍 *UmraJet — Premium Umra xizmatlari markazi* 🤍\n\n"
        "Assalomu alaykum!\n"
        "Biz bilan safaringiz yanada qulay va muqaddas bo'ladi. Quyidagi xizmatlardan birini tanlang:",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

# --- Xizmatlar ---
async def ravza_service(update: Update):
    discount_active = is_discount_active()
    price_viza = "10 SAR (aksiyada!)" if discount_active else "15 SAR"
    price_no_viza = "15 SAR (aksiyada!)" if discount_active else "20 SAR"

    await update.message.reply_text(
        f"🍇 *Ravzaga tashrif — Ruhi tetiklik sari bir qadam*\n\n"
        f"🕌 Nabiy sollallohu alayhi vasallamning Ravzalariga tashrif buyurish imkoniyati.\n"
        f"📋 *Narxlar:*\n"
        f" - Viza bilan: {price_viza}\n"
        f" - Vizasiz: {price_no_viza}\n\n"
        f"🎁 7 kunlik ochilish aksiyasi davom etmoqda!\n"
        f"📌 Guruhli yoki yakka tartibdagi tashriflar\n"
        f"💳 To‘lov: Uzcard / Humo / Visa / Crypto\n\n"
        f"🗂 Hujjatlarni rasm yoki PDF ko‘rinishida yuboring.\n"
        f"📞 Bog‘lanish: {MANAGER_RAVZA} yoki {MANAGER_ASSISTANT}",
        parse_mode="Markdown"
    )

async def umra_packages(update: Update):
    await update.message.reply_text(
        "🕋 *Umra paketlari — Orzularingiz endi yanada yaqin*\n\n"
        "✨ *Standard:* 1100$ dan\n"
        "✨ *VIP:* 2000$ dan\n\n"
        "Paketga quyidagilar kiradi:\n"
        "✅ Viza rasmiylashtirish\n"
        "✅ Qulay mehmonxonalar\n"
        "✅ Zamonaviy transport\n"
        "✅ Gid xizmati\n"
        "✅ Guruh ovqatlari\n\n"
        f"📞 Batafsil: {MANAGER_ASSISTANT} yoki {MANAGER_RAVZA}",
        parse_mode="Markdown"
    )

async def hotels(update: Update):
    await update.message.reply_text(
        "🏨 *Mehmonxona va hostel bron qilish*\n\n"
        "📍 Makka va Madinaning markazida\n"
        "🕰 Istalgan muddatga joylashtirish\n"
        "🍽 Ovqatli yoki ovqatsiz variantlar\n"
        "🛏 Toza, xavfsiz va arzon joylar\n\n"
        f"📞 Band qilish: {MANAGER_ASSISTANT}",
        parse_mode="Markdown"
    )

async def train_tickets(update: Update):
    await update.message.reply_text(
        "🚄 *HHR Poezd chiptalari — Tez va xavfsiz safar*\n\n"
        "📍 Yo‘nalishlar: Makka ↔ Madina va boshqa shaharlarga\n"
        "🎟 Joylar: Ekanom / Biznes klass\n"
        "📅 Istalgan sana uchun buyurtma berish mumkin\n\n"
        f"📞 Buyurtma uchun: {MANAGER_ASSISTANT}",
        parse_mode="Markdown"
    )

async def transport_service(update: Update):
    await update.message.reply_text(
        "🚐 *Shaxsiy va guruh transport xizmati*\n\n"
        "🚘 Toyota, VIP avtomobillar, avtobuslar\n"
        "🕌 Mehmonxonadan masjidlargacha yetkazish\n"
        "👨‍✈️ Tajribali, xushmuomala haydovchilar\n\n"
        f"📞 Buyurtma: {MANAGER_ASSISTANT}",
        parse_mode="Markdown"
    )

async def group_food(update: Update):
    await update.message.reply_text(
        "🍽 *10+ kishilik guruh ovqatlari*\n\n"
        "🍛 Milliy taomlar: palov, manti, shashlik va boshqalar\n"
        "🍽 1 mahal, 2 mahal yoki to‘liq ta'minot\n"
        "🎉 Tadbirlar, ziyofatlar uchun xizmat\n\n"
        f"📞 Buyurtma uchun: {MANAGER_ASSISTANT}",
        parse_mode="Markdown"
    )

async def plane_tickets(update: Update):
    await update.message.reply_text(
        "✈️ *Avia chiptalar — Har qanday yo‘nalishda*\n\n"
        "🌍 Dunyoning istalgan nuqtasiga\n"
        "🗓 Mos sana va narxlar bilan\n"
        "📃 Viza bilan va vizasiz variantlar mavjud\n\n"
        f"📞 Batafsil: {MANAGER_ASSISTANT} yoki {MANAGER_RAVZA}",
        parse_mode="Markdown"
    )

async def admin_contacts(update: Update):
    await update.message.reply_text(
        f"📞 *Admin kontaktlari:*\n\n"
        f"🍇 Ravza xizmatlari: {MANAGER_RAVZA}\n"
        f"🕋 Umra & boshqa xizmatlar: {MANAGER_ASSISTANT}",
        parse_mode="Markdown"
    )

async def official_channels(update: Update):
    await update.message.reply_text(
        f"📢 *Rasmiy kanallar:*\n\n"
        f"🧭 UmraJet: {CHANNEL_UMRAJET}\n"
        f"🕌 Ravza tashriflari: {CHANNEL_RAVZA}",
        parse_mode="Markdown"
    )

async def ai_helper_intro(update: Update):
    await update.message.reply_text(
        "🤖 *AI yordamchi* ishga tushdi.\n"
        "Iltimos, oddiy savollaringizni yozing — biz sizga tez va aniq javob beramiz.",
        parse_mode="Markdown"
    )

async def ai_helper(update: Update, text: str):
    lower = text.lower()
    if "ravza" in lower:
        await update.message.reply_text("✅ Ha, vizasiz ham Ravzaga olib kiramiz.")
    elif "umra" in lower:
        await update.message.reply_text("🕋 Umra paketlarimiz to‘liq tayyorlangan — sizga faqat pasport yetarli.")
    elif "to‘lov" in lower or "tolov" in lower:
        await update.message.reply_text("💳 To‘lov Uzcard, Humo, Visa yoki Crypto orqali amalga oshiriladi.")
    else:
        await update.message.reply_text("🤖 Savolingizni to‘liqroq yozing yoki menyudan xizmat tanlang.")

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
        await ai_helper(update, text)

async def set_menu_commands(application: Application):
    await application.bot.set_my_commands([
        BotCommand("start", "🔄 Botni qayta ishga tushirish"),
    ])

def main():
    application = Application.builder().token(TOKEN).post_init(set_menu_commands).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()

if __name__ == "__main__":
    main()
