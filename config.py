import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROUP_ID = int(os.getenv("GROUP_ID"))

# Adminlar ID ro'yxati (foydalanuvchi ID lari)
ADMINS = ["6185643481", "7671988237", "7376002803"]  # @V001XX, @V001VB, @vip_arabiy
