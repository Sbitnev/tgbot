import sqlite3
from datetime import datetime

base = sqlite3.connect('database/bot.db')
cursor = base.cursor()


def sql_start():
    if base:
        print('База данных подключена!')
    cursor.execute('CREATE TABLE IF NOT EXISTS users (tg_id INTEGER, name_group TEXT)')
    base.commit()


async def get_data_from_proxy(state):
    async with state.proxy() as data:
        return data
