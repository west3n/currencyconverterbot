import logging

from aiogram import types
from decouple import config

from handlers.commands import register as reg_commands
from handlers.engine import register as reg_engine


bot_token = config("BOT_TOKEN")
access_key = config("OER_API_KEY")
logger = logging.getLogger(__name__)
cur_list = ['usd', 'eur', 'gbp', 'cny', 'jpy', 'chf']


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Start bot")
    ])


def register_handlers(dp):
    reg_commands(dp)
    reg_engine(dp)
