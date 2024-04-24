from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
import os
import json
import emoji
from createbot import bot, dp, ADMINS_CHAT_ID
from aiogram import types
from handlers.states import GetGroup, DeleteGroup
from database import sqldb
import datetime
from keyb import menukb, inlinekb
from parsersch import parserjson

# Обработчик команды
@dp.message_handler(commands=['admin'])
async def command_handler(message: types.Message):
    if message.chat.id == ADMINS_CHAT_ID:
        # Ответ на команду только в чате с администратором
        await message.answer("Панель администратора", reply_markup=inlinekb.inline_kb)
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
    await bot.send_message(ADMINS_CHAT_ID, await parserjson.get_groupschedule(number))

@dp.callback_query_handler(text='delete_group')
async def add_group_handler(callback: types.CallbackQuery):
    await DeleteGroup.group.set()
    await bot.send_message(ADMINS_CHAT_ID, "Введите номер группы:", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(state=DeleteGroup.group)
async def process_name(message: types.Message, state: FSMContext):
    number = message.text  
    await state.finish()
    await bot.send_message(ADMINS_CHAT_ID, await parserjson.deletegroup(number))


# Обработчик команды
@dp.message_handler(commands=['addall'])
async def command_handler(message: types.Message):
    if message.chat.id == ADMINS_CHAT_ID:
        # Ответ на команду только в чате с администратором
        for i in sqldb.allg:
            await sqldb.add_group(i)
        await message.answer("Успешно")
    else:
        # Игнорировать команду в других чатах
        pass

@dp.message_handler(commands=['admin'])
async def command_handler(message: types.Message):
    if message.chat.id == ADMINS_CHAT_ID:
        # Ответ на команду только в чате с администратором
        await message.answer("Админ еее", reply_markup=inlinekb.inline_kb)
    else:
        # Игнорировать команду в других чатах
        pass

# async def add_proxy_data(state, data: dict):
#     async with state.proxy() as proxy:
#         for k,v in data.items():
#             proxy[k] = v