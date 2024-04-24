# import asyncio
# import datetime
# from aiogram import Bot, Dispatcher
# from aiogram.types import ChatType
# from database import sqldb
# import json
# from handlers import userside

# # Инициализация бота
# bot = Bot(token='6839706247:AAHnMPOdwbkWeamBgh-3vorJF9Ht2VnvqjQ')
# dp = Dispatcher(bot)

# # Список пользователей (их ID)
# #user_ids = [350509350]  # пример ID пользователей

# # Функция для отправки сообщения
# async def send_message_to_users():
#     user_ids = [id_[0] for id_ in await sqldb.get_notif_users()]
#     print(user_ids)
#     #user_ids = [350509350]
#     days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#     for user_id in user_ids:
#         try:
#             group_num = str(sqldb.get_group_name(user_id))
#             week, day = userside.get_day_and_week()
#             schedule_text = userside.day_sch(user_id, week, day+1)
#             if not ('Нет занятий' in schedule_text):
#                 await bot.send_message(user_id, "Занятия завтра: \n"+schedule_text, parse_mode="Markdown")
#         except Exception as e:
#             print(f"Ошибка при отправке сообщения пользователю {user_id}: {e}")

# # Функция для планирования отправки сообщения
# async def schedule_message():
#     while True:
#         now = datetime.datetime.now()
#         if now.hour == 22 and now.minute == 31:
#             await send_message_to_users()
#             print('Time')
#         await asyncio.sleep(60)  # проверяем каждую минуту

# # Запуск бота
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.create_task(schedule_message())
#     loop.run_forever()