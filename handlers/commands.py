from aiogram import Dispatcher, types
from keyboards import inline
from config import states


async def bot_start(msg: types.Message):
    await msg.delete()
    name = msg.from_user.first_name
    await msg.answer(f"Hello, {name}! Please, choose a currency", reply_markup=inline.currency())
    await states.CurrencyConverter.currency_from.set()


def register(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands='start', state='*')
