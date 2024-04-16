from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
import os
import json
import emoji
from createbot import bot, dp, ADMINS_CHAT_ID
from aiogram import types
from handlers.states import GetGroup
from database import sqldb
import datetime
from keyb import menukb, inlinekb
from parsersch import parserjson

# Обработчик команды
@dp.message_handler(commands=['admin'])
async def command_handler(message: types.Message):
    if message.chat.id == ADMINS_CHAT_ID:
        # Ответ на команду только в чате с администратором
        await message.answer("Админ еее", reply_markup=inlinekb.inline_kb)
    else:
        # Игнорировать команду в других чатах
        pass

@dp.callback_query_handler(text='add_group')
async def add_group_handler(callback: types.CallbackQuery):
    await GetGroup.group.set()
    await bot.send_message(ADMINS_CHAT_ID, "Введите номер группы:", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(state=GetGroup.group)
async def process_name(message: types.Message, state: FSMContext):
    number = message.text  
    await state.finish()
    if parserjson.get_groupschedule(number):
        await bot.send_message(ADMINS_CHAT_ID, "Успешно")
    else:
        await bot.send_message(ADMINS_CHAT_ID, "неУспешно")



# async def add_proxy_data(state, data: dict):
#     async with state.proxy() as proxy:
#         for k,v in data.items():
#             proxy[k] = v