import asyncio
from aiogram import Dispatcher, Bot
import routers.user
from settings import TOKEN
import sender


async def main():
    dp = Dispatcher()
    bot = Bot(TOKEN)
    dp.include_routers(routers.user.router)
    sender.set_bot(dp, bot)
    sender.init_handlers()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
