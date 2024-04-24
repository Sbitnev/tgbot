from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
import os
import json
from createbot import bot, dp, ADMINS_CHAT_ID
from aiogram import types
from handlers.states import ChooseGroup, ChooseNotif
from database import sqldb
import datetime
from keyb import menukb
from handlers import adminside
import pickle
from parsersch import parserjson

async def job():
    user_ids = [id_[0] for id_ in await sqldb.get_notif_users()]
    print(user_ids)
    # user_ids = [350509350]
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for user_id in user_ids:
        try:
            group_num = str(await sqldb.get_group_name(user_id))
            week, day = await get_day_and_week()
            schedule_text = await day_sch(user_id, week, day+1)
            if not ('Нет занятий' in schedule_text):
                await bot.send_message(user_id, "Занятия завтра: \n\n"+schedule_text, parse_mode="Markdown")
        except Exception as e:
            print(f"Ошибка при отправке сообщения пользователю {user_id}: {e}")

async def get_day_and_week():
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    today = datetime.date.today()
    day_of_week = today.weekday()  # Monday - 0, Sunday - 6
    even_week = "odd" if (today.isocalendar()[1] % 2 == 0) else "even"  # 0 for odd week, 1 for even
    return even_week, day_of_week

async def schedule_to_text(schedule):
    text = ""
    for week_type, days in schedule.items():
        text += f"{week_type.capitalize()} week:\n"
        for day, lessons in days.items():
            text += format_day({day : lessons})
    return text

async def format_day(schedule_dict):
    output = ""
    weekdays = {
    "Monday": "Понедельник",
    "Tuesday": "Вторник",
    "Wednesday": "Среда",
    "Thursday": "Четверг",
    "Friday": "Пятница",
    "Saturday": "Суббота",
    "Sunday": "Воскресенье"}
    for day, classes in schedule_dict.items():
        output += f"*{weekdays[day]}*:\n"
        if classes == "No lessons":
            output += "Нет занятий\n\n"
        else:
            for class_info in classes:
                arr = class_info['info'].split(", ")
                output += f"Время: {class_info['time']}\n"
                output += f"Место: {class_info['addr']}\n"
                output += f"Предмет: {arr[0]}\n"
                output += f"Преподаватель: {arr[1]}\n"
                output += f"Формат: {arr[2]}\n\n"
    return output

async def day_sch(id, week, day):
    schedule_text = ''
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    group_num = str(await sqldb.get_group_name(id))
    with open("groups/"+str(group_num)+".json") as file:
        SCHEDULE = json.load(file)
    if day == 7:
        week = "odd" if (week == "even") else "even"
        day = days_of_week[0]
    else:
        day = days_of_week[(day)%7]

    schedule_text = await format_day({day:SCHEDULE[week][day]})
    return schedule_text




@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    all_users_id = [id_[0] for id_ in await sqldb.get_all_users()]
    
    if message.from_user.id not in all_users_id:
        await sqldb.add_user(message.from_user.id)

    if sqldb.get_group_name == 'no_group':
        await message.reply('Здравствуй! Это бот, который отправляет расписание университета ИТМО. Для получения списка команд воспользуйтесь /help', reply=False)
        await ChooseGroup.group.set()
        await message.reply('Введите номер вашей группы латинскими буквами:', reply=False)
    else:
        await message.reply('Здравствуй! Это бот, который отправляет расписание университета ИТМО. Для получения списка команд воспользуйтесь /help', reply=False, reply_markup=menukb.mainMenu)


# Обработчик ввода номера группы
@dp.message_handler(state=ChooseGroup.group)
async def get_group(message: types.Message, state: FSMContext):
    group_num = message.text.upper()
    with open('groups/allgroups.pkl', 'rb') as file:
        allgroups = pickle.load(file)
    upperallgroups = [x.upper() for x in allgroups]
    if not group_num in upperallgroups:
        await message.reply('Неверный номер группы.', reply=False)
        return
    
    await state.finish()
    group_num = allgroups[upperallgroups.index(group_num)]
    await sqldb.change_user_group(message.from_user.id, group_num)
    if not os.path.exists('groups/'+str(group_num)+'.json'):
        await parserjson.get_groupschedule(group_num)

    await message.reply(f"Ваша группа: {group_num}\nДля получения расписания воспользуйтесь клавиатурой", reply=False, reply_markup=menukb.mainMenu)

@dp.message_handler()
async def echo(message: types.Message):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if message.text == 'Расписание на сегодня':
        result = await get_day_and_week()
        week = result[0]
        day = result[1]
        schedule_text = await day_sch(message.from_user.id, week, day)
        await message.answer(schedule_text, parse_mode="Markdown")
    
    elif message.text == 'Расписание на завтра':
        result = await get_day_and_week()
        week = result[0]
        day = result[1]
        schedule_text = await day_sch(message.from_user.id, week, day+1)
        await message.answer(schedule_text, parse_mode="Markdown")

    elif message.text == 'Расписание на эту неделю':
        schedule_text = ''
        group_num = str(await sqldb.get_group_name(message.from_user.id))
        with open("groups/"+str(group_num)+".json") as file:
            SCHEDULE = json.load(file)
        result = await get_day_and_week()
        week = result[0]
        day = result[1]
        SCHEDULE = SCHEDULE[week]
        for day, lessons in SCHEDULE.items():
            schedule_text += await format_day({day : lessons})
    
        await message.answer(schedule_text, parse_mode="Markdown")

    elif message.text == 'Расписание на следующую неделю':
        schedule_text = ''
        group_num = str(await sqldb.get_group_name(message.from_user.id))
        with open("groups/"+str(group_num)+".json") as file:
            SCHEDULE = json.load(file)
        result = await get_day_and_week()
        week = result[0]
        day = result[1]
        week = "odd" if (week == "even") else "even"
        SCHEDULE = SCHEDULE[week]
        for day, lessons in SCHEDULE.items():
            schedule_text += await format_day({day : lessons})
    
        await message.answer(schedule_text, parse_mode="Markdown")

    elif message.text == 'Изменить группу':
        await ChooseGroup.group.set()
        await message.reply('Введите номер вашей группы латинскими буквами:', reply=False)

    elif message.text == 'Узнать группу':
        group_num = str(await sqldb.get_group_name(message.from_user.id))
        await message.reply(f'Вы указали этот номер группы: {group_num}', reply=False)

    elif message.text == 'Узнать расписание':
        await message.reply('Вы на странице расписания', reply=False, reply_markup=menukb.dayMenu)

    elif message.text == 'Главное меню':
        await message.reply('Вы в главном меню', reply=False, reply_markup=menukb.mainMenu)

    elif message.text == 'Назад':
        await message.reply('Вы в главном меню', reply=False, reply_markup=menukb.mainMenu)

    elif message.text == 'Уведомления':
        if await sqldb.get_notif(message.from_user.id):
            await message.reply('Уведомления включены', reply=False, reply_markup=menukb.notifoff)
        else:
            await message.reply('Уведомления выключены', reply=False, reply_markup=menukb.notifon)
    
    elif message.text == 'Включить':
        await sqldb.change_notif(message.from_user.id, 1)
        await message.reply('Уведомления включены', reply=False, reply_markup=menukb.mainMenu)
    
    elif message.text == 'Выключить':
        await sqldb.change_notif(message.from_user.id, 0)
        await message.reply('Уведомления выключены', reply=False, reply_markup=menukb.mainMenu)
    


