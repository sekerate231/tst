from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,ReplyKeyboardRemove

def start_reply():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Mahsulotlar'), KeyboardButton(text='Mening Buyrtmalarim')],
            [KeyboardButton(text='Profile'),KeyboardButton(text='🛒 Savatcha')]
        ],
        resize_keyboard=True
    )

def start_reply_admin():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Mahsulotlar'), KeyboardButton(text='Mening Buyrtmalarim')],
            [KeyboardButton(text='Profile'), KeyboardButton(text='Panel')]
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

def admin_panel_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🆕 Mahsulot q'oshish")],
            [KeyboardButton(text="📋 Admin mahsulotlar")],
            [KeyboardButton(text="👥 Foydalanuvchilar")],
            [KeyboardButton(text="📢Reklama")],
            [KeyboardButton(text="🔙 Orqaga")]
        ],
        resize_keyboard=True
    )