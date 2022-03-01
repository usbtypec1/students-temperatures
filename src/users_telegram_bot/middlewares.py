import contextlib
from typing import Iterable, Union

from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message
from aiogram.utils.exceptions import TelegramAPIError

import db
from users_telegram_bot.bot import bot
from users_telegram_bot.responses import Response


class OnlyStudentsMiddleware(BaseMiddleware):

    async def on_pre_process_message(self, message: Message, data: dict):
        current_user = db.get_user_or_none_by_telegram_id(message.from_user.id)
        if current_user is None:
            await message.answer('Я вас не знаю 😁')
            raise CancelHandler
        data['current_user'] = current_user


class ProcessResponseMiddleware(BaseMiddleware):

    async def on_post_process_message(self, message: Message, data_from_handler: list, data: dict):
        if not data_from_handler:
            return
        responses: Union[Response, Iterable[Response]] = data_from_handler[0]
        if isinstance(responses, Response):
            responses = [responses]
        for response in responses:
            text, reply_markup = response.get_text(), response.get_reply_markup()
            chat_id = response.get_chat_id() or message.chat.id
            with contextlib.suppress(TelegramAPIError):
                await bot.send_message(chat_id, text, reply_markup=reply_markup)
