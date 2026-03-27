from aiogram.filters import Command,CommandStart
from aiogram import Router
from aiogram.types import Message
from filters.filter import Rolefilter
from keyboards.replies import register_reply,start_reply,start_reply_admin

router=Router()
@router.message(CommandStart(),Rolefilter('Admin'))
async def start(msg:Message):
  await msg.answer('Assalomu Aleykum admin, botga hush kelibsiz!\n Admin panel',reply_markup=start_reply_admin())
@router.message(CommandStart())
async def start(msg:Message,db):
 telegram_id=msg.from_user.id
 if await db.is_user_exists(telegram_id):
    await msg.answer(f'Assalomu Aleykum {msg.from_user.full_name}botga hush kelibsiz',reply_markup=start_reply())
 else:
   await msg.answer(f'Assalomu Aleykum {msg.from_user.full_name}botga hush kelibsiz',reply_markup=register_reply())