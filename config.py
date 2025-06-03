import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ORDER_GROUP_ID = int(os.getenv("ORDER_GROUP_ID"))

# Adminlar ro'yxati
ADMINS = [
    7376002803,  # @vip_arabiy
    7671988237,  # @V001VB
    6185643481   # @V001XX
]
