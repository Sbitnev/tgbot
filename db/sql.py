import sqlite3
from create_bot import bot

base = sqlite3.connect('info.db')
cursor = base.cursor()

def sql_start():
    if base:
        print('Db connected!')
    cursor.execute('CREATE TABLE IF NOT EXISTS users (tg_id, name_group)')
    base.commit()