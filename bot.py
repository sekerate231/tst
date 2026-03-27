import asyncio
from aiogram import Bot,Dispatcher
from config import config 
from aiogram.fsm.storage.memory import MemoryStorage
from hendlers.commands import router as start_router
from hendlers.register import router as Register_router
from hendlers.user.user_profile import router as profile_router
from hendlers.admin.admin import router as admin_panel_router
from database.database import Database
from hendlers.user.products import router as products_router
from hendlers.admin.add_products import router as add_products_admin_router
async def main():
    bot=Bot(token=config.BOT_TOKEN)
    dp=Dispatcher(storage=MemoryStorage())

    db=Database()
    await db.connect()
    dp['db']=db

    dp.include_router(start_router)
    dp.include_router(Register_router)
    dp.include_router(profile_router)
    dp.include_router(admin_panel_router)
    dp.include_router(products_router)
    dp.include_router(add_products_admin_router)


    await dp.start_polling(bot)

if __name__=='__main__':
     asyncio.run(main())