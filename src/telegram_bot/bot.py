import contextlib

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode, BotCommand, BotCommandScopeChat, BotCommandScopeDefault
from aiogram.utils.exceptions import ChatNotFound

import config
import db
from telegram_bot.middlewares import ProcessResponseMiddleware

__all__ = (
    'bot',
    'dp',
    'setup_bot_commands',
    'on_bot_startup',
    'setup_middlewares',
)

bot = Bot(config.TELEGRAM_BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())


async def setup_student_commands(dispatcher: Dispatcher):
    await dispatcher.bot.set_my_commands([
            BotCommand('start', 'Стартуем 🚀'),
            BotCommand('mark_temperature', 'Отметить температуру 🔥'),
            BotCommand('classmates', 'Список любимых одноклассников 👦🏿'),
            BotCommand('history', 'Моя история отметок температур 📆'),
        ], scope=BotCommandScopeDefault())


async def setup_admin_commands(dispatcher: Dispatcher, student_telegram_id: int):
    await dispatcher.bot.set_my_commands([
        BotCommand('start', 'Стартуем 🚀'),
        BotCommand('temperatures_report', 'Сегодняшние температуры'),
        BotCommand('download_as_excel', 'Скачать в формате excel'),
    ], scope=BotCommandScopeChat(student_telegram_id))


async def setup_bot_commands(dispatcher: Dispatcher):
    await setup_student_commands(dispatcher)
    for telegram_id in config.ADMIN_CHAT_IDS:
        with contextlib.suppress(ChatNotFound):
            await setup_admin_commands(dispatcher, telegram_id)


def setup_middlewares(dispatcher: Dispatcher) -> None:
    middlewares_for_setup = (ProcessResponseMiddleware(dispatcher.bot),)
    for middleware in middlewares_for_setup:
        dispatcher.setup_middleware(middleware)


async def on_bot_startup(dispatcher: Dispatcher):
    setup_middlewares(dispatcher)
    await setup_bot_commands(dispatcher)
