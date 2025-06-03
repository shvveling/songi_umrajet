import os
from aiogram import Bot
from aiogram.types import ParseMode
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")
bot = Bot(token=bot_token)

manager_ids = [6185643481, 7376002803, 7671988237]

async def notify_managers(order: dict):
    text = (
        f"📥 <b>Yangi buyurtma</b>\n\n"
        f"👤 Foydalanuvchi: {order['user_name']} (@{order['user_username']})\n"
        f"🛎 Xizmat: {order['service'].capitalize()}\n"
        f"📝 Ma'lumotlar: {order['details']}\n"
    )
    for admin_id in manager_ids:
        await bot.send_message(admin_id, text, parse_mode=ParseMode.HTML)
