from aiogram import types, Dispatcher

# HHR train poezd yo'nalishlari va ma'lumotlari
HHR_TRAIN_INFO = """
🚆 *HHR Train Yo‘nalishlari va Narxlari*:

1. Riyadh — Makkah
2. Riyadh — Madina
3. Makkah — Madina
4. Jeddah — Madina
5. Dammam — Makkah

🕒 Har bir yo'nalish uchun qatnov vaqtlari va chipta narxlari doimiy ravishda o‘zgarib turadi.
Sizga aniq ma’lumotni sotuvchilarimiz taqdim etadi.

📌 Chipta xarid qilishda viza holatini, yo‘nalishni va sana tanlashni unutmang.
"""

async def service_handler(message: types.Message):
    text = ""
    if message.text == "🛂 Viza xizmati":
        text = (
            "🌍 *Viza xizmatlari*\n\n"
            "Turist va Umra vizalarini rasmiy ravishda taqdim etamiz.\n\n"
            "💰 Narxlar:\n"
            "• Turist vizasi: 120 USD / dona\n"
            "• Umra vizasi: 160 USD / dona\n\n"
            "Viza olish jarayoni tez va ishonchli, hujjatlar bilan yordam beramiz."
        )
    elif message.text == "🕌 Ravza tasreh xizmati":
        text = (
            "🕋 *Ravza tasreh xizmati*\n\n"
            "Ravzaga kirish uchun tasreh xizmatlari 24/7:\n"
            "- Agar sizda oldin ro‘yxatdan o‘tmagan va ruhsatnoma (viza) bo‘lsa, narx: 15 SAR / dona\n"
            "- Agar viza berilmasa, narx: 20 SAR / dona\n\n"
            "Guruhlarga 10+ tasrehlarga chegirma mavjud, narxlar alohida kelishiladi.\n\n"
            "Eslatma: Tasreh uchun viza berilsa narx arzonroq bo'ladi oldin ro'yhatdan o'tmagan bo'lishi sharti bilan."
        )
    elif message.text == "🏨 Mehmonxona":
        text = (
            "🏨 *Mehmonxona va Hostel*\n\n"
            "Qulay va arzon narxlarda mehmonxona va hostel xizmatlarini taqdim etamiz.\n"
            "Joylashuv: Makkah va Madinada markaziy hududlarda.\n\n"
            "Narxlar va mavjudlik haqida batafsil ma'lumotni menejerlarimizdan so‘rashingiz mumkin."
        )
    elif message.text == "🚆 Po'ezd biletlar":
        text = HHR_TRAIN_INFO
    elif message.text == "🚗 Transport":
        text = (
            "🚗 *Transport xizmati*\n\n"
            "Airport transfer, shahardagi sayohatlar va guruh transportlari uchun xizmatlar.\n"
            "Yuqori sifatli va qulay transportlar taqdim etiladi."
        )
    elif message.text == "🍽️ Guruhlar uchun ovqat":
        text = (
            "🍽️ *Guruhlar uchun ovqat xizmati*\n\n"
            "Katta guruhlar uchun maxsus taom va menyular.\n"
            "Sifatli va mazali taomlarni taqdim etamiz."
        )
    else:
        text = "Iltimos, menyudan xizmatni tanlang."
        
    await message.answer(text, parse_mode="Markdown")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(service_handler, lambda m: m.text in [
        "🛂 Viza xizmati",
        "🕌 Ravza tasreh xizmati",
        "🏨 Mehmonxona",
        "🚆 Po'ezd biletlar",
        "🚗 Transport",
        "🍽️ Guruhlar uchun ovqat",
    ])
