from aiogram.dispatcher.filters.state import State, StatesGroup


class CurrencyConverter(StatesGroup):
    currency_from = State()
    currency_to = State()
    amount = State()

