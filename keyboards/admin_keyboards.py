from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_menu_kb = InlineKeyboardMarkup(row_width=2)
admin_menu_kb.add(
    InlineKeyboardButton("📦 Buyurtmalar", callback_data="orders"),
    InlineKeyboardButton("📊 Statistika", callback_data="stats"),
    InlineKeyboardButton("📢 Push xabar", callback_data="push")
)
