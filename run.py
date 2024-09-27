import asyncio
from aiogram import Bot, Dispatcher
import os
from python.heandlers import router
from config import TOKEN



bot = Bot(token=TOKEN)
dp = Dispatcher()
 

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)



if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')