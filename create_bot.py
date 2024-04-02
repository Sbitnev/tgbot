import config as cfg
from aiogram import Bot
from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()

bot = Bot(token=cfg.TOKEN)

dp = Dispatcher(bot, storage=storage)
