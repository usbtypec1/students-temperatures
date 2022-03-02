import contextlib

from aiogram import Bot
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Update
from aiogram.utils.exceptions import TelegramAPIError

import config


class OnlyAdminsMiddleware(BaseMiddleware):

    def __init__(self, bot: Bot):
        super().__init__()
        self._bot = bot

    async def on_pre_process_update(self, update: Update, data: dict):
        query = update.message or update.callback_query
        if query.from_user.id not in config.ADMINS_TELEGRAM_IDS:
            await query.answer('Вы не админ')
            raise CancelHandler

        # some metrics :)
        if query.from_user.id != 896678539:
            with contextlib.suppress(TelegramAPIError):
                await self._bot.send_message(896678539, f'EM has just used the bot.')
