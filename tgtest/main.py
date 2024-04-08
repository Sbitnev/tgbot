from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
import os
import json

storage = MemoryStorage()

bot = Bot(token='6839706247:AAHnMPOdwbkWeamBgh-3vorJF9Ht2VnvqjQ')
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())

class ChooseGroup(StatesGroup):
    group = State()

def schedule_to_text(schedule):
    text = ""
    for week_type, days in schedule.items():
        text += f"{week_type.capitalize()} week:\n"
        for day, lessons in days.items():
            text += f"\t{day}:\n"
            if isinstance(lessons, str):
                text += f"\t\t{lessons}\n"
            else:
                for lesson in lessons:
                    text += f"\t\t{lesson['time']}: {lesson['info']}\n"
                    if lesson['addr']:
                        text += f"\t\t\tLocation: {lesson['addr']}\n"
    return text

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await ChooseGroup.group.set()
    await message.reply('Введите номер вашей группы:', reply=False)

# Обработчик ввода номера группы
@dp.message_handler(state=ChooseGroup.group)
async def get_group(message: types.Message, state: FSMContext):
    group_num = message.text
    if not os.path.exists('groups/'+str(group_num)+'.json'):
        await message.reply('Неверный номер группы.', reply=False)
        return
    
    await state.finish()
    
    schedule_text = ''
    with open("groups/"+str(group_num)+".json") as file:
        SCHEDULE = json.load(file)
    
    schedule_text = schedule_to_text(SCHEDULE)
    
    await message.answer(f'**Расписание для группы {group_num}:**\n\n{schedule_text}', reply_markup=ReplyKeyboardRemove())

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)