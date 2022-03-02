from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message

import db


class OnlyStudentsMiddleware(BaseMiddleware):
    """
    Ensure user is existing in database.
    If so, that user object passes in middleware state as 'current_user'.
    If you want to use that 'current_user' object,
    you should define it as kwarg in your handler.
    """

    async def on_pre_process_message(self, message: Message, data: dict):
        current_user = db.get_user_or_none_by_telegram_id(message.from_user.id)
        if current_user is None:
            await message.answer('Я вас не знаю 😁')
            raise CancelHandler
        data['current_user'] = current_user
