from typing import Iterable

from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.middlewares import BaseMiddleware

import config

bot = Bot(config.ADMINS_TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


def setup_middlewares(dispatcher: Dispatcher,
                      middlewares_for_setup: Iterable[BaseMiddleware]) -> None:
    for middleware in middlewares_for_setup:
        dispatcher.setup_middleware(middleware)
