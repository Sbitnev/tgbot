import asyncio
import datetime
from aiogram import Bot, Dispatcher
from aiogram.types import ChatType

# Инициализация бота
bot = Bot(token='6839706247:AAHnMPOdwbkWeamBgh-3vorJF9Ht2VnvqjQ')
dp = Dispatcher(bot)

# Список пользователей (их ID)
user_ids = [350509350]  # пример ID пользователей

# Функция для отправки сообщения
async def send_message_to_users():
    for user_id in user_ids:
        try:
            await bot.send_message(user_id, "Привет")
        except Exception as e:
            print(f"Ошибка при отправке сообщения пользователю {user_id}: {e}")

# Функция для планирования отправки сообщения
async def schedule_message():
    while True:
        now = datetime.datetime.now()
        if now.hour == 22 and now.minute == 31:
            await send_message_to_users()
            print('Time')
        await asyncio.sleep(60)  # проверяем каждую минуту

# Запуск бота
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(schedule_message())
    loop.run_forever()