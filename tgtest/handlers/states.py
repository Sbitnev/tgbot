from aiogram.dispatcher.filters.state import State, StatesGroup

class ChooseGroup(StatesGroup):
    group = State()