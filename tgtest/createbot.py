from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

bottoken = '6839706247:AAHnMPOdwbkWeamBgh-3vorJF9Ht2VnvqjQ'

storage = MemoryStorage()

bot = Bot(token=bottoken)
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())