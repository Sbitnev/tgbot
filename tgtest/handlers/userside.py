from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
import os
import json
import emoji
from createbot import bot, dp
from aiogram import types
from handlers.states import ChooseGroup
from database import sqldb

def schedule_to_text(schedule):
    text = ""
    for week_type, days in schedule.items():
        text += f"{week_type.capitalize()} week:\n"
        for day, lessons in days.items():
            text += f"*{day}:*\n"
            if isinstance(lessons, str):
                text += f"{lessons}\n"
            else:
                for lesson in lessons:
                    text += emoji.emojize(f":alarm_clock: {lesson['time']}:\n🍘{lesson['info']}\n")
                    if lesson['addr']:
                        text += (emoji.emojize(':round_pushpin: Location:')) + f"{lesson['addr']}\n"
    return text

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply('Здравствуй! Это бот, который отправляет расписание университета ИТМО. Для получения списка команд воспользуйтесь /help', reply=False)
    
    all_users_id = [id_[0] for id_ in await sqldb.get_all_users()]
    
    if message.from_user.id not in all_users_id:
        await sqldb.add_user(message.from_user.id)

    await ChooseGroup.group.set()
    await message.reply('Введите номер вашей группы латинскими буквами:', reply=False)

# Обработчик ввода номера группы
@dp.message_handler(state=ChooseGroup.group)
async def get_group(message: types.Message, state: FSMContext):
    group_num = message.text
    group_num = group_num.upper()
    if not os.path.exists('groups/'+str(group_num)+'.json'):
        await message.reply('Неверный номер группы.', reply=False)
        return
    
    await state.finish()
    
    await sqldb.change_user_group(message.from_user.id, group_num)

    await message.reply(f"Ваша группа: {group_num}\nДля получения расписания воспользуйтесь /schedule", reply=False)

@dp.message_handler(commands=['schedule'])
async def schedule(message: types.Message):

    schedule_text = ''
    group_num = str(sqldb.get_group_name(message.from_user.id))
    with open("groups/"+str(group_num)+".json") as file:
        SCHEDULE = json.load(file)
    
    schedule_text = schedule_to_text(SCHEDULE)
    
    await bot.send_message(message.from_user.id, text= f'**Расписание для группы {group_num}:**\n\n{schedule_text}', reply_markup=ReplyKeyboardRemove(), parse_mode="Markdown")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
