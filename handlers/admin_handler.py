from aiogram import types, Dispatcher

ADMIN_IDS = [6185643481, 7376002803, 7671988237]

async def forward_orders_to_admins(message: types.Message):
    if message.chat.type == "private" and message.from_user.id not in ADMIN_IDS:
        for admin_id in ADMIN_IDS:
            try:
                await message.forward(admin_id)
            except Exception as e:
                print(f"Adminga xabar yuborishda xatolik: {e}")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(forward_orders_to_admins)
