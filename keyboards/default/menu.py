from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📋 Xizmatlar"),
            KeyboardButton(text="📞 Aloqa"),
        ],
        [
            KeyboardButton(text="🛒 Buyurtmalarim"),
            KeyboardButton(text="ℹ️ Ma'lumot"),
        ]
    ],
    resize_keyboard=True
)
