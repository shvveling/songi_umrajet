from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import ADMINS
from keyboards.admin_keyboards import admin_menu_kb

# Admin menu start
async def admin_panel(message: types.Message):
    if str(message.from_user.id) in ADMINS:
        await message.answer("🔐 *Admin panelga xush kelibsiz!*", reply_markup=admin_menu_kb, parse_mode='Markdown')
    else:
        await message.reply("❌ Sizda admin panelga kirish ruxsati yo‘q.")

# Statistika (mock)
async def show_stats(call: types.CallbackQuery):
    if str(call.from_user.id) in ADMINS:
        await call.message.edit_text("📊 Umumiy foydalanuvchilar: *2145 ta*\n🔄 Faol foydalanuvchilar: *712 ta*", parse_mode="Markdown", reply_markup=admin_menu_kb)

# Push yuborish
async def push_menu(call: types.CallbackQuery):
    if str(call.from_user.id) in ADMINS:
        await call.message.answer("📢 Yubormoqchi bo‘lgan xabaringizni yozing:")
        await call.answer()
        # Shu yerda FSM bilan push_xabar qabul qilish yoziladi (alohida qo‘shamiz)

# Qo‘shimcha funktsiyalar (bo‘limlar)
async def manage_orders(call: types.CallbackQuery):
    await call.message.edit_text("📦 Buyurtmalarni ko‘rish bo‘limi hozirda tayyorlanmoqda.", reply_markup=admin_menu_kb)

# Register
def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(admin_panel, Command("admin"))
    dp.register_callback_query_handler(show_stats, lambda c: c.data == "stats")
    dp.register_callback_query_handler(push_menu, lambda c: c.data == "push")
    dp.register_callback_query_handler(manage_orders, lambda c: c.data == "orders")
