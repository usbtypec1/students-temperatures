from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config
from admins_telegram_bot.middlewares import OnlyAdminsMiddleware
from common.middlewares import ProcessResponseMiddleware

bot = Bot(config.ADMINS_TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


def setup_middlewares(dispatcher: Dispatcher) -> None:
    middlewares_for_setup = (
        ProcessResponseMiddleware(dispatcher.bot),
        OnlyAdminsMiddleware(),
    )
    for middleware in middlewares_for_setup:
        dispatcher.setup_middleware(middleware)


async def on_startup(dispatcher: Dispatcher) -> None:
    setup_middlewares(dispatcher)
