from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnSch = KeyboardButton('Узнать расписание')
btnGroup = KeyboardButton('Изменить группу')
btnGroupName = KeyboardButton('Узнать группу')
btnNotif = KeyboardButton('Уведомления')


mainMenu = ReplyKeyboardMarkup().add(btnSch, btnGroupName, btnGroup, btnNotif)

btnToday = KeyboardButton('Расписание на сегодня')
btnNextday = KeyboardButton('Расписание на завтра')
btnWeek = KeyboardButton('Расписание на эту неделю')
btnNextweek = KeyboardButton('Расписание на следующую неделю')
btnMain = KeyboardButton('Главное меню')

dayMenu = ReplyKeyboardMarkup().row(btnToday, btnNextday).row(btnWeek, btnNextweek).add(btnMain)