from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove

def start_reply():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Mahsulotlar'), KeyboardButton(text='Mening Buyrtmalarim')],
            [KeyboardButton(text='Profile')]
        ],
        resize_keyboard=True
    )

def register_reply():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Register')]
        ],
        resize_keyboard=True
    )