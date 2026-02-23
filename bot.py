import asyncio
from aiogram import Bot,Dispatcher
from config import config 
from aiogram.fsm.storage.memory import MemoryStorage
from hendlers.commands import router as start_router
from hendlers.register import router as Register_router
from database.database import Database
async def main():
    bot=Bot(token=config.BOT_TOKEN)
    dp=Dispatcher(storage=MemoryStorage())

    db=Database()
    await db.connect()
    dp['db']=db

    dp.include_router(start_router)
    dp.include_router(Register_router)


    await dp.start_polling(bot)

if __name__=='__main__':
     asyncio.run(main())