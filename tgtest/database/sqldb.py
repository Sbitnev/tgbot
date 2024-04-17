import sqlite3
from datetime import datetime


base = sqlite3.connect('database/bot.db')
cursor = base.cursor()


def sql_start():
    if base:
        print('База данных подключена!')
    cursor.execute('CREATE TABLE IF NOT EXISTS users (tg_id INTEGER, name_group TEXT, notif INTEGER)')
    base.commit()


async def get_data_from_proxy(state):
    async with state.proxy() as data:
        return data

async def add_user(user_id):
    cursor.execute('INSERT INTO users VALUES (?, ?, ?)', (user_id, 'no_group', 0))
    base.commit()

async def get_all_users():
    return [u for u in cursor.execute('SELECT * FROM users')]

async def get_notif_users():
    return [u for u in cursor.execute('SELECT tg_id FROM users WHERE notif = 1')]

async def change_user_group(user_id, group_name):
    cursor.execute('UPDATE users SET name_group = ? WHERE tg_id = ?', (group_name, user_id))
    base.commit()

async def change_notif(user_id, notif=1):
    cursor.execute('UPDATE users SET notif = ? WHERE tg_id = ?', (notif, user_id))
    base.commit()

def get_group_name(tg_id):
    cursor.execute('SELECT name_group FROM users WHERE tg_id = ?', (tg_id,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None
    
def get_notif(tg_id):
    cursor.execute('SELECT notif FROM users WHERE tg_id = ?', (tg_id,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None

