from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def currency() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('US dollar', callback_data='usd')],
        [InlineKeyboardButton('Euro', callback_data='eur')],
        [InlineKeyboardButton('Pound sterling', callback_data='gbp')],
        [InlineKeyboardButton('Chinese renminbi', callback_data='cny')],
        [InlineKeyboardButton('Japanese yen', callback_data='jpy')],
        [InlineKeyboardButton('Swiss franc', callback_data='chf')]
    ])
    return kb
