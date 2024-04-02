from create_bot import bot, dp
from aiogram.utils import executor
from db import sql

async def on_startup(_):
    sql.sql_start()
    print('Bot online')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
