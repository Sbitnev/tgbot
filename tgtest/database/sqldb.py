import sqlite3
from datetime import datetime


base = sqlite3.connect('database/bot.db')
cursor = base.cursor()

allg =['K3120', 'K3121', 'K3122', 'K3123', 'K3139', 'K3140', 'K3141', 'MC1 1', 'MC1 1.1', 'P3106', 'P3107', 'P3108', 'P3109', 'P3110', 'P3111', 'P3112', 'P3113', 'P3114', 'P3115', 'P3116', 'P3117', 'P3118', 'P3119', 'P3120', 'P3121', 'P3122', 'P3123', 'P3124', 'P3125', 'P3130', 'P3131', 'P3132', 'L3216', 'L3217', 'M3200', 'M3201', 'M3202', 'M3203', 'M3204', 'M3205', 'M3206', 'M3207', 'M3208', 'M3209', 'M3210', 'M3211', 'M3212', 'M3213', 'M3214', 'M3215', 'M3216', 'M3217', 'M3218', 'M3219', 'M3220d', 'M3221d', 'M3231', 'M3232', 'M3233', 'M3234', 'M3235', 'M3236', 'M3237', 'M3238', 'M3239', 'MC2 1', 'MC2 1.1', 'O3243', 'O3244', 'U3279d', 'U3280d', 'V3202', 'V3203', 'Z3243', 'Z3244', 'B33001', 'B33002', 'B33003', 'D33101', 'H33212', 'H33232', 'K33201', 'K33202', 'K33211', 'K33212', 'K33391', 'K33392', 'K33401', 'K33402', 'K33421', 'K33422', 'L33161', 'L33162', 'L33181', 'L33182', 'M33001', 'M33011', 'M33021', 'M33031', 'M33051', 'M33061', 'M33071', 'M33081', 'M33091', 'M33101', 'M33111', 'M33121', 'M33321', 'M33331', 'M33341', 'M33351', 'M33361', 'M33371', 'M33381', 'M33391', 'N33451', 'N33452', 'N33453', 'N33461', 'N33471', 'N33481', 'N33491', 'N33501', 'N33511', 'N33521', 'N33522', 'N33523', 'N33531', 'N33532', 'O33431', 'O33432', 'O33442', 'P3304c', 'P33081', 'P33082', 'P33091', 'P33092', 'P33101', 'P33102', 'P33111', 'P33121', 'P33131', 'P33141', 'P33151', 'P33201', 'P33202', 'P33211', 'P33212', 'P33222', 'P33232', 'P33301', 'P33302', 'P33311', 'P33312', 'P33661', 'P33662', 'P33663', 'P33664', 'P33691', 'P33692', 'P33693', 'P33694', 'R33351', 'R33352', 'R33353', 'R33362', 'R33372', 'R33401', 'R33402', 'R33403', 'R33412', 'R33413', 'R33423', 'R3342c', 'R33801', 'R33802', 'R33811', 'R33812', 'R3398c', 'T33301', 'T33302', 'T33303', 'T33304', 'T33305', 'T33311', 'T33321', 'U3310d', 'U3378d', 'V33021', 'V33022', 'V33023', 'V33031', 'W33051', 'W33052', 'W33602', 'Z33431', 'Z33432', 'Z33433', 'Z33434', 'B34001', 'B34002', 'B34003', 'B34222', 'B34223', 'B34232', 'B34233', 'D34101', 'K34201', 'K34202', 'K34211', 'K34212', 'K34401', 'K34402', 'K34412', 'K34421', 'K34422', 'L34161', 'L34162', 'L34181', 'L34182', 'M34001', 'M34011', 'M34021', 'M34031', 'M34041', 'M34051', 'M34061', 'M34071', 'M34081', 'M34091', 'M34112', 'M34341', 'M34351', 'M34361', 'M34371', 'M34381', 'M34391', 'N34461', 'N34462', 'N34463', 'N34471', 'N34481', 'N34491', 'N34501', 'N34511', 'N34521', 'N34523', 'N34531', 'N34532', 'P3404c', 'P34101', 'P34102', 'P34111', 'P34121', 'P34131', 'P34201', 'P34202', 'P34211', 'P34212', 'P34222', 'P34301', 'P34302', 'P34312', 'P34671', 'P34672', 'P34673', 'P34674', 'P34691', 'P34692', 'P34693', 'P34694', 'R34351', 'R34352', 'R34362', 'R34372', 'R3438', 'R34401', 'R34402', 'R34403', 'R34412', 'R34413', 'R34423', 'R3442c', 'R34801', 'R34802', 'R34811', 'R34812', 'T34301', 'T34302', 'T34303', 'T34304', 'T34305', 'T34306', 'U34751', 'U34752', 'U34761', 'U34762', 'V34021', 'V34022', 'V34023', 'W34051', 'W34052', 'W34601', 'Z34431', 'Z34433', 'Z34434']

def sql_start():
    if base:
        print('База данных подключена!')
    cursor.execute('CREATE TABLE IF NOT EXISTS users (tg_id INTEGER, name_group TEXT, notif INTEGER)')
    cursor.execute('CREATE TABLE IF NOT EXISTS groups (name_group TEXT, schedule TEXT, request INTEGER)')
    base.commit()


async def get_data_from_proxy(state):
    async with state.proxy() as data:
        return data

async def add_user(user_id):
    cursor.execute('INSERT INTO users VALUES (?, ?, ?)', (user_id, 'no_group', 0))
    base.commit()

async def add_group(group):
    all_groups = [id_[0] for id_ in await get_all_groups()]
    
    if group not in all_groups:
        cursor.execute('INSERT INTO groups VALUES (?, ?, ?)', (group, 'no_schedule', 0))
        base.commit()
    else:
        print('exists')
    

async def add_all():
    for i in allg:
        await add_group(i)

async def get_all_users():
    return [u for u in cursor.execute('SELECT * FROM users')]

async def get_all_groups():
    return [u for u in cursor.execute('SELECT * FROM groups')]

async def get_notif_users():
    return [u for u in cursor.execute('SELECT tg_id FROM users WHERE notif = 1')]

async def change_user_group(user_id, group_name):
    cursor.execute('UPDATE users SET name_group = ? WHERE tg_id = ?', (group_name, user_id))
    base.commit()

async def change_notif(user_id, notif):
    cursor.execute('UPDATE users SET notif = ? WHERE tg_id = ?', (notif, user_id))
    base.commit()

async def change_schedule(group, schedule):
    cursor.execute('UPDATE groups SET schedule = ? WHERE name_group = ?', (schedule, group))
    base.commit()

async def get_group_name(tg_id):
    cursor.execute('SELECT name_group FROM users WHERE tg_id = ?', (tg_id,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None
    
async def get_notif(tg_id):
    cursor.execute('SELECT notif FROM users WHERE tg_id = ?', (tg_id,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None

