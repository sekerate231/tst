from aiogram.types import Message
from aiogram import F,Router

router=Router()

@router.message(F.text=='Profile')
async def profile(msg:Message,db):
    data= await db.user_profile(msg.from_user.id)
    await msg.answer(f'Your information: \n ismingiz: {data['name']}\nYoshingiz: {data['age']}\nTelefon raqamingiz: {data['phone']}\nRolingiz: {data['role']}')