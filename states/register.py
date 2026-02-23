from aiogram.fsm.state import State,StatesGroup

class RegisterState(StatesGroup):
    name=State()
    full_name=State()
    age=State()
    number=State()