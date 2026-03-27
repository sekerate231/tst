from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from states.register import RegisterState
from aiogram.types import Message,ReplyKeyboardRemove

router=Router()

@router.message(F.text=='Register')
async def register_hendler(msg:Message,state:FSMContext,db):
    if await db.is_user_exists(msg.from_user.id):
        await msg.answer('Siz royhatan otbolgansiz!')
    else:
      await msg.answer('Ismingizni kiriting:')
      await state.set_state(RegisterState.name)

@router.message(RegisterState.name)
async def register_hendler(msg:Message,state:FSMContext):
    await state.update_data(name=msg.text)
    await msg.answer('Familiyangizni kiritng:')
    await state.set_state(RegisterState.full_name)

@router.message(RegisterState.full_name)
async def register_hendler(msg:Message,state:FSMContext):
    await state.update_data(full_name=msg.text)
    await msg.answer('Yoshingizni kiritng:')
    await state.set_state(RegisterState.age)

@router.message(RegisterState.age)
async def register_hendler(msg:Message,state:FSMContext):
    await state.update_data(age=msg.text)
    await msg.answer('Telefon raqamingizni kiritng:')
    await state.set_state(RegisterState.phone)

@router.message(RegisterState.phone)
async def register_hendler(msg:Message,state:FSMContext,db):
    await state.update_data(phone=msg.text)

    
    data= await state.get_data()
    await msg.answer(f'Ismingiz:{data['name']}\nFamiliyangiz:{data['full_name']}\n Yoshingiz:{data['age']}\n Telefon raqamingiz:{data['phone']}')
    await db.add_user(f'{msg.from_user.id},{data['name']},{data['full_name']},{data['age']},{data['phone']}')
    await msg.answer('Siz mufoqyatli royxatan otingiz!', reply_markup=ReplyKeyboardRemove())

    await state.clear()
