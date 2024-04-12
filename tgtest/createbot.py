from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

bottoken = '6839706247:AAHnMPOdwbkWeamBgh-3vorJF9Ht2VnvqjQ'
ADMINS_CHAT_ID = -4195314706

storage = MemoryStorage()

bot = Bot(token=bottoken)
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())