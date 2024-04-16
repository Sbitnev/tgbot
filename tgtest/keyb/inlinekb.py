from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

inline_kb = InlineKeyboardMarkup(row_width=2)
inline_kb.add(
    InlineKeyboardButton(text="Добавить группу", callback_data="add_group"),
    InlineKeyboardButton(text="Отмена", callback_data="cancel")
)