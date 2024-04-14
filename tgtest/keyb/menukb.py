from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnToday = KeyboardButton('Расписание на сегодня')
btnNextday = KeyboardButton('Расписание на завтра')
btnWeek = KeyboardButton('Расписание на эту неделю')
btnNextweek = KeyboardButton('Расписание на следующую неделю')

dayMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnToday, btnNextday, btnWeek, btnNextweek)