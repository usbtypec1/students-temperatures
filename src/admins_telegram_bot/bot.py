from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode, BotCommand

import config
from admins_telegram_bot.middlewares import OnlyAdminsMiddleware
from common.middlewares import ProcessResponseMiddleware

bot = Bot(config.ADMINS_TELEGRAM_BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())


def setup_middlewares(dispatcher: Dispatcher) -> None:
    middlewares_for_setup = (
        ProcessResponseMiddleware(dispatcher.bot),
        OnlyAdminsMiddleware(dispatcher.bot),
    )
    for middleware in middlewares_for_setup:
        dispatcher.setup_middleware(middleware)


async def setup_bot_commands(dispatcher: Dispatcher):
    await dispatcher.bot.set_my_commands([
        BotCommand('start', 'Открыть меню'),
        BotCommand('temperatures_report', 'Сегодняшние температуры'),
    ])


async def on_startup(dispatcher: Dispatcher) -> None:
    setup_middlewares(dispatcher)
