from aiogram import types
from aiogram.dispatcher.filters import Text



async def add_proxy_data(state, data: dict):
    async with state.proxy() as proxy:
        for k,v in data.items():
            proxy[k] = v