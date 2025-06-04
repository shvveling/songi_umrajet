from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import ADMINS, GROUP_ID
from loader import dp, bot
from database import get_all_users_count

# Admin Panelga kirish
@dp.message_handler(Command("admin"))
async def admin_panel(message: types.Message):
    if str(message.from_user.id) not in ADMINS:
        return

    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("📊 Statistika", callback_data="stats"),
        InlineKeyboardButton("📢 E'lon yuborish", callback_data="send_announcement"),
        InlineKeyboardButton("📥 Buyurtmalar", url=f"https://t.me/c/{str(GROUP_ID)[4:]}")
    )

    await message.answer("🔐 <b>Admin Panelga xush kelibsiz!</b>", reply_markup=keyboard, parse_mode="HTML")

# Statistika ko‘rsatish
@dp.callback_query_handler(lambda c: c.data == "stats")
async def show_stats(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) not in ADMINS:
        return

    user_count = get_all_users_count()
    await callback_query.message.edit_text(f"📊 <b>Statistika</b>\n\n👥 Foydalanuvchilar soni: <b>{user_count}</b>", parse_mode="HTML")

# E'lon yuborish
@dp.callback_query_handler(lambda c: c.data == "send_announcement")
async def ask_announcement(callback_query: types.CallbackQuery):
    if str(callback_query.from_user.id) not in ADMINS:
        return
    await callback_query.message.answer("📢 E'lon matnini kiriting:")
    dp.register_message_handler(process_announcement, state=None)

async def process_announcement(message: types.Message):
    if str(message.from_user.id) not in ADMINS:
        return

    announcement_text = message.text
    user_count = get_all_users_count()
    success, failed = 0, 0

    from database import get_all_users
    for user_id in get_all_users():
        try:
            await bot.send_message(user_id, announcement_text)
            success += 1
        except:
            failed += 1

    await message.answer(f"✅ Yuborildi: {success} ta\n❌ Yuborilmadi: {failed} ta")
    dp.unregister_message_handler(process_announcement, state=None)

def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(admin_panel, Command("admin"))
