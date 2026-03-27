from aiogram.fsm.state import State,StatesGroup

class AddProductsState(StatesGroup):
    name=State()
    price=State()
    description=State()
