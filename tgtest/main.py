from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage  # Consider persistent storage later
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters.state import State, StatesGroup

storage = MemoryStorage()

bot = Bot(token='6839706247:AAHnMPOdwbkWeamBgh-3vorJF9Ht2VnvqjQ')

dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

# Таблица с расписанием
SCHEDULE = {
    '101': {
        'Понедельник': '10:00 - Математика',
        'Вторник': '12:00 - Русский язык',
        'Среда': '14:00 - Физика'
    },
    '102': {
        'Понедельник': '11:00 - История',
        'Вторник': '13:00 - Биология',
        'Среда': '15:00 - Химия'
    }
}



class ChooseGroup(StatesGroup):
    group = State()


# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.chat.id, 'Здарова! Бот твоей шараги. Помощь по командам /help')


# Обработчик ввода номера группы
@dp.message_handler(state=ChooseGroup.group)
async def get_group(message: types.Message, state: FSMContext):
    group_num = message.text
    if group_num not in SCHEDULE:
        await message.reply('Неверный номер группы.', reply=False)
        return
    
    await state.finish()
    
    schedule_text = ''
    for day, lesson in SCHEDULE[group_num].items():
        schedule_text += f'{day}: {lesson}\n'
    
    await message.answer(f'**Расписание для группы {group_num}:**\n\n{schedule_text}', reply_markup=ReplyKeyboardRemove())
