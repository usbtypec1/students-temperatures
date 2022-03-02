from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Update

import config


class OnlyAdminsMiddleware(BaseMiddleware):

    async def on_pre_process_update(self, update: Update, data: dict):
        query = update.message or update.callback_query
        if query.from_user.id not in config.ADMINS_TELEGRAM_IDS:
            await query.answer('Вы не админ')
            raise CancelHandler
