from aiogram import executor
from createbot import bot, dp
from handlers import userside
from database import sqldb

async def on_startup(_):
    sqldb.sql_start()
    await sqldb.add_all()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

