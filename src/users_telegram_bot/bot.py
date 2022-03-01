from typing import Iterable

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import ParseMode, BotCommand

import config

__all__ = (
    'bot',
    'dp',
    'setup_bot_commands',
    'on_bot_startup',
    'setup_middlewares',
)

bot = Bot(config.USERS_TELEGRAM_BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())


async def setup_bot_commands(dispatcher: Dispatcher):
    await dispatcher.bot.set_my_commands([
        BotCommand('start', 'Стартуем 🚀'),
        BotCommand('mark_temperature', 'Отметить температуру 🔥'),
        BotCommand('classmates', 'Список любимых одноклассников 👦🏿'),
        BotCommand('history', 'Моя история отметок температур 📆'),
    ])


def setup_middlewares(dispatcher: Dispatcher,
                      middlewares_for_setup: Iterable[BaseMiddleware]) -> None:
    for middleware in middlewares_for_setup:
        dispatcher.setup_middleware(middleware)


async def on_bot_startup(dispatcher: Dispatcher):
    await setup_bot_commands(dispatcher)
