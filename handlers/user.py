from aiogram import Router, F
from aiogram.filters import Command, Text
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from utils.helpers import notify_managers

user_router = Router()

class OrderStates(StatesGroup):
    ChoosingService = State()
    TasrehCount = State()
    TasrehVisa = State()
    PoezdDate = State()
    PoezdVisa = State()
    CollectingDetails = State()

@user_router.message(Command("start"))
async def start_handler(message: Message, state: FSMContext):
    await state.clear()
    text = (
        "🕌 <b>UmraJetBot</b> ga xush kelibsiz!\n\n"
        "Quyidagi xizmatlarimizdan birini tanlang:\n"
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛂 Viza xizmatlari (Turist & Umra)", callback_data="service_visa")],
        [InlineKeyboardButton(text="🕌 Ravzaga kirish uchun Tasreh", callback_data="service_tasreh")],
        [InlineKeyboardButton(text="🚄 Poezd chiptalari", callback_data="service_poezd")],
        [InlineKeyboardButton(text="🏨 Hotel & Hostel", callback_data="service_hotel")],
        [InlineKeyboardButton(text="🚗 Transport xizmatlari", callback_data="service_transport")],
        [InlineKeyboardButton(text="🍽️ Guruhlar uchun ovqat xizmatlari", callback_data="service_food")],
        [InlineKeyboardButton(text="📞 Managerlar bilan bog‘lanish", callback_data="contact_managers")],
    ])
    await message.answer(text, reply_markup=kb)
    await OrderStates.ChoosingService.set()

@user_router.callback_query(Text(startswith="service_"), state=OrderStates.ChoosingService)
async def service_selected(call: CallbackQuery, state: FSMContext):
    service = call.data.split("_")[1]
    await state.update_data(service=service)
    
    if service == "visa":
        text = (
            "🛂 <b>Viza xizmatlari</b>\n"
            "Biz Turist va Umra vizalarini chiqarib beramiz.\n"
            "Siz uchun qulay variantni tanlang."
        )
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🛂 Turist Viza", callback_data="visa_tourist")],
            [InlineKeyboardButton(text="🕌 Umra Viza", callback_data="visa_umra")],
            [InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back_to_menu")],
        ])
        await call.message.edit_text(text, reply_markup=kb)
        
    elif service == "tasreh":
        text = "🕌 Ravzaga kirish uchun Tasreh xizmatimiz.\n\nNechta Tasreh kerakligini kiriting (raqam bilan):"
        await call.message.edit_text(text)
        await OrderStates.TasrehCount.set()
        
    elif service == "poezd":
        text = (
            "🚄 Poezd chiptalari xizmati.\n"
            "Iltimos, poezd safar sanasini kiriting (YYYY-MM-DD formatda):"
        )
        await call.message.edit_text(text)
        await OrderStates.PoezdDate.set()
        
    elif service == "hotel":
        text = (
            "🏨 Hotel va Hostel xizmatlari.\n"
            "Iltimos, xohlagan joyingizni va sanani yozing:"
        )
        await call.message.edit_text(text)
        await OrderStates.CollectingDetails.set()
        
    elif service == "transport":
        text = (
            "🚗 Transport xizmatlari.\n"
            "Iltimos, kerakli transport turi va sanani yozing:"
        )
        await call.message.edit_text(text)
        await OrderStates.CollectingDetails.set()
        
    elif service == "food":
        text = (
            "🍽️ Guruhlar uchun ovqat xizmatlari.\n"
            "Iltimos, guruh hajmi va taomlar haqida ma'lumot bering:"
        )
        await call.message.edit_text(text)
        await OrderStates.CollectingDetails.set()
        
    elif service == "contact":
        text = (
            "📞 Managerlar bilan bog‘lanish:\n"
            "Asosiy manager: @vip_arabiy\n"
            "Manager 1: @V001VB\n"
            "Manager 2: @V001XX\n\n"
            "Rasmiy botimiz: @umrajet_bot\n"
            "Rasmiy kanallar: @umrajet, @the_ravza"
        )
        await call.message.edit_text(text)
        await state.clear()
        
    else:
        await call.answer("Noto‘g‘ri tanlov, boshqattan urinib ko‘ring.", show_alert=True)
        return

    await call.answer()

@user_router.callback_query(Text("back_to_menu"))
async def back_to_menu(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await start_handler(call.message, state)

@user_router.message(OrderStates.TasrehCount)
async def tasreh_count_received(message: Message, state: FSMContext):
    if not message.text.isdigit() or int(message.text) <= 0:
        await message.answer("Iltimos, 1 yoki undan katta butun son kiriting.")
        return
    count = int(message.text)
    await state.update_data(tasreh_count=count)
    
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Viza kerak", callback_data="tasreh_visa_yes")],
        [InlineKeyboardButton(text="Viza kerak emas", callback_data="tasreh_visa_no")],
    ])
    await message.answer("Tasreh uchun viza beriladimi?", reply_markup=kb)
    await OrderStates.TasrehVisa.set()

@user_router.callback_query(Text(startswith="tasreh_visa_"), state=OrderStates.TasrehVisa)
async def tasreh_visa_selected(call: CallbackQuery, state: FSMContext):
    visa_needed = call.data.split("_")[-1] == "yes"
    await state.update_data(tasreh_visa=visa_needed)
    
    data = await state.get_data()
    count = data.get("tasreh_count")
    visa_text = "viza beriladi" if visa_needed else "viza berilmaydi"
    
    price_per_unit = 20 if visa_needed else 15
    if count >= 10:
        price_per_unit = 15 if visa_needed else 12
    
    total_price = price_per_unit * count
    
    text = (
        f"📋 Siz tanladingiz:\n"
        f"Tasreh soni: {count}\n"
        f"Viza: {visa_text}\n"
        f"Narx (SAR): {total_price}\n\n"
        f"Iltimos, buyurtma uchun qo‘shimcha ma'lumot kiriting yoki 'tayyor' deb yozing."
    )
    await call.message.edit_text(text)
    await OrderStates.CollectingDetails.set()
    await call.answer()

@user_router.message(OrderStates.PoezdDate)
async def poezd_date_received(message: Message, state: FSMContext):
    if len(message.text) != 10 or message.text[4] != "-" or message.text[7] != "-":
        await message.answer("Sana noto‘g‘ri formatda. Iltimos YYYY-MM-DD ko‘rinishida kiriting.")
        return
    await state.update_data(poezd_date=message.text)
    
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Viza kerak", callback_data="poezd_visa_yes")],
        [InlineKeyboardButton(text="Viza kerak emas", callback_data="poezd_visa_no")],
    ])
    await message.answer("Poezd uchun viza kerakmi?", reply_markup=kb)
    await OrderStates.PoezdVisa.set()

@user_router.callback_query(Text(startswith="poezd_visa_"), state=OrderStates.PoezdVisa)
async def poezd_visa_selected(call: CallbackQuery, state: FSMContext):
    visa_needed = call.data.split("_")[-1] == "yes"
    await state.update_data(poezd_visa=visa_needed)
    
    data = await state.get_data()
    date = data.get("poezd_date")
    visa_text = "viza kerak" if visa_needed else "viza kerak emas"
    
    text = (
        f"🚄 Poezd safar sanasi: {date}\n"
        f"Viza holati: {visa_text}\n\n"
        f"Iltimos, qo‘shimcha ma'lumot kiriting yoki 'tayyor' deb yozing."
    )
    await call.message.edit_text(text)
    await OrderStates.CollectingDetails.set()
    await call.answer()

@user_router.message(OrderStates.CollectingDetails)
async def collecting_details(message: Message, state: FSMContext):
    details = message.text
    data = await state.get_data()
    
    order = {
        "user_id": message.from_user.id,
        "user_name": message.from_user.full_name,
        "user_username": message.from_user.username or "",
        "service": data.get("service"),
        "details": details,
        "extra": data,
    }
    
    await notify_managers(order)
    
    await message.answer(
        "✅ Buyurtmangiz qabul qilindi! Tez orada managerlar siz bilan bog‘lanishadi.\n"
        "Qo‘shimcha xizmatlar uchun /start ni bosing."
    )
    await state.clear()

@user_router.callback_query(Text("contact_managers"))
async def contact_managers(call: CallbackQuery):
    text = (
        "📞 Managerlar bilan bog‘lanish:\n"
        "Asosiy manager: @vip_arabiy\n"
        "Manager 1: @V001VB\n"
        "Manager 2: @V001XX\n\n"
        "Rasmiy botimiz: @umrajet_bot\n"
        "Rasmiy kanallar: @umrajet, @the_ravza"
    )
    await call.message.edit_text(text)
    await call.answer()
