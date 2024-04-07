from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

storage = MemoryStorage()

bot = Bot(token='6839706247:AAHnMPOdwbkWeamBgh-3vorJF9Ht2VnvqjQ')
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())

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


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await ChooseGroup.group.set()
    await message.reply('Введите номер вашей группы:', reply=False)

# Обработчик ввода номера группы
@dp.message_handler(state=ChooseGroup.group)
async def get_group(message: types.Message, state: FSMContext):
    group_num = message.text
    if group_num not in SCHEDULE:
        await message.answer('Неверный номер группы.')
        return
    
    await state.finish()
    
    schedule_text = ''
    for day, lesson in SCHEDULE[group_num].items():
        schedule_text += f'{day}: {lesson}\n'
    
    await message.answer(f'**Расписание для группы {group_num}:**\n\n{schedule_text}', reply_markup=ReplyKeyboardRemove())

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)