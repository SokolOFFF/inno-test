# import logging
# import os

# from aiogram import Bot, types
# from aiogram.contrib.middlewares.logging import LoggingMiddleware
# from aiogram.dispatcher import Dispatcher
# from aiogram.dispatcher.webhook import SendMessage
# from aiogram.utils.executor import start_webhook


# API_TOKEN = os.environ.get('TOKEN')


# WEBHOOK_HOST = 'https://your.domain'
# WEBHOOK_PATH = '/path/to/api'
# WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"


# WEBAPP_HOST = 'localhost'  # or ip
# WEBAPP_PORT = 3001

# logging.basicConfig(level=logging.INFO)

# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)
# dp.middleware.setup(LoggingMiddleware())


# @dp.message_handler()
# async def echo(message: types.Message):
#     return SendMessage(message.chat.id, message.text)


# async def on_startup(dp):
#     await bot.set_webhook(WEBHOOK_URL)


# async def on_shutdown(dp):
#     logging.warning('Shutting down..')
#     await bot.delete_webhook()
#     logging.warning('Bye!')


# if __name__ == '__main__':
#     start_webhook(
#         dispatcher=dp,
#         webhook_path=WEBHOOK_PATH,
#         on_startup=on_startup,
#         on_shutdown=on_shutdown,
#         skip_updates=True,
#         host=WEBAPP_HOST,
#         port=WEBAPP_PORT,
#     )





import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

API_TOKEN = '7034753304:AAFK0ASRHwXyVq6WZnlDNU5DNE3IAOpsh7k'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_func(message: types.Message):
    await message.answer('Вы ввели команду /start')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())