from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from filters.filter import Rolefilter
from aiogram import Router,F
from aiogram.types import CallbackQuery
from keyboards.inlines import inline_action
from states.add_products import AddProductsState
from states.update_products import UpdateProductState

router=Router()

@router.message(F.text=="🆕 Mahsulot q'oshish", Rolefilter('Admin'))
async def add_products(msg:Message, state:FSMContext):
    await msg.answer('Mahusulotni nomini kiriting:')
    await state.set_state(AddProductsState.name)

@router.message(AddProductsState.name)
async def add_products(msg:Message, state:FSMContext):
    await state.update_data(name=msg.text)
    await msg.answer('Mahsulotni narxini kiriting:')
    await state.set_state(AddProductsState.price)

@router.message(AddProductsState.price)
async def add_products(msg:Message, state:FSMContext):
    await state.update_data(price=msg.text)
    await msg.answer('Mahsulotni opisaniyasini kiriting:')
    await state.set_state(AddProductsState.description)

@router.message(AddProductsState.description)
async def add_products(msg:Message, state:FSMContext,db):
    await state.update_data(description=msg.text)

    data= await state.get_data()
    await db.app_products(data['name',data['price'],data['description']])
    await msg.answer('Mahsulot saqlandi!')
# ----------------------------------------------------------------------------------------------
@router.callback_query(F.data.startwith("adminproduct_"), Rolefilter("Admin"))
async def product(call:CallbackQuery):
    product_id = call.data.split("_")[1]
    await call.message.answer("Mahsulotni ozgartirish yoki ochirib tashlash ", reply_markup=inline_action(int(product_id)))
    await call.answer()

    @router.callback_query(F.data.startwith('delete_product_'), Rolefilter('Admin'))
    async def product(call:CallbackQuery, db):
        product_id=call.data.split("_")[2]
        await  db.delete_product(int(product_id))
        await call.message.answer('Mahsulot ochirildi')
        await call.answer()

    @router.callback_query(F.data.startwith('edit_product_'), Rolefilter('Admin'))
    async def product(call:CallbackQuery, state:FSMContext):
        product_id= call.data.split("_")[2]
        await state.set_state(UpdateProductState.product_id)
        await state.update_data(product_id=product_id)
        await call.message.answer('Mahsulotni nomini kiriting:')
        await state.set_state(UpdateProductState.name)

    @router.message(UpdateProductState.name)
    async def product(msg:Message, state:FSMContext):
        await state.update_data(name=msg.text)
        await msg.answer('Mahuslot narxini kiriting:' )
        await state.set_state(UpdateProductState.price)
    
    @router.message(UpdateProductState.price)
    async def product(msg:Message, state:FSMContext):
        await state.update_data(price=msg.text)
        await msg.answer('Mahuslot opisaniyasini kiriting:' )
        await state.set_state(UpdateProductState.description)
    
    @router.message(UpdateProductState.description)
    async def product(msg:Message, state:FSMContext, db):
        await state.update_data(description=msg.text)
        data= await state.get_data()
        await db.update_product(
            data["name"],
            data['price'],
            data['description'],
            data['product_id']
            )
        await msg.answer("Mahsulot ozgartirildi")
        await state.clear()
    
    