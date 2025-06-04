from aiogram.dispatcher.filters.state import State, StatesGroup

class OrderState(StatesGroup):
    service_type = State()
    full_name = State()
    phone_number = State()
    extra_info = State()
