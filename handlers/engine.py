import requests
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from keyboards import inline
from config import config, states


async def first_step(call: types.CallbackQuery, state: FSMContext):
    currency_from = call.data
    await state.update_data(currency_from=currency_from)
    await call.answer()
    await call.message.edit_reply_markup()
    await call.message.answer(f'Ok, {currency_from.upper()}. Now please, select the second currency',
                              reply_markup=inline.currency())

    await states.CurrencyConverter.next()


async def second_step(call: types.CallbackQuery, state: FSMContext):
    currency_to = call.data
    await state.update_data(currency_to=currency_to)
    data = await state.get_data()
    currency_from = data['currency_from']
    if currency_from == currency_to:
        await call.message.answer("You pick similar currencies, please, try again - /start")
        await call.message.edit_reply_markup()
        await state.finish()
        return

    await call.answer()
    await call.message.edit_reply_markup()
    await call.message.answer(f'Ok, {currency_from.upper()} to {currency_to.upper()}. '
                              f'Please enter the amount of {currency_from.upper()} to convert:')

    await states.CurrencyConverter.next()


async def final(msg: types.Message, state: FSMContext):
    try:
        amount = msg.text
        await state.update_data(amount=amount)
        data = await state.get_data()
        currency_from = data['currency_from'].upper()
        currency_to = data['currency_to'].upper()
        url = f'https://openexchangerates.org/api/latest.json?app_id={config.access_key}'
        response = requests.get(url)
        data = response.json()
        exchange_rate = data['rates'][currency_to] / data['rates'][currency_from]
        converted_amount = float(amount) * exchange_rate
        await msg.answer(f'{int(amount)} {currency_from} is {round(converted_amount, 2)} {currency_to}'
                         f'\nPress /start to do another converting.')
        await state.finish()
    except ValueError:
        await msg.answer("Please, send me only digits. Try again")


def register(dp: Dispatcher):
    dp.register_callback_query_handler(first_step, lambda c: c.data in config.cur_list,
                                       state=states.CurrencyConverter.currency_from)
    dp.register_callback_query_handler(second_step, lambda c: c.data in config.cur_list,
                                       state=states.CurrencyConverter.currency_to)
    dp.register_message_handler(final, state=states.CurrencyConverter.amount)
