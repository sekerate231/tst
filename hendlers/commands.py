from aiogram.filters import Command,CommandStart
from aiogram import Router
from aiogram.types import Message
from keyboards.replies import register_reply,start_reply

router=Router()

@router.message(CommandStart())
async def start(msg:Message,db):
 if await db.is_user_exists():
    await msg.answer(f'Assalomu Aleykum {msg.from_user.full_name}botga hush kelibsiz',reply_markup=start_reply())
 else:
   await msg.answer(f'Assalomu Aleykum {msg.from_user.full_name}botga hush kelibsiz',reply_markup=register_reply())