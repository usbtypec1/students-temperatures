import contextlib
from typing import Union, Iterable

from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Update, Message
from aiogram.utils.exceptions import TelegramAPIError

import config
from admins_telegram_bot.bot import bot
from admins_telegram_bot.responses import Response


class OnlyAdminsMiddleware(BaseMiddleware):

    async def on_pre_process_update(self, update: Update, data: dict):
        query = update.message or update.callback_query
        if query.from_user.id not in config.ADMINS_TELEGRAM_IDS:
            await query.answer('Вы не админ')
            raise CancelHandler


class ProcessResponseMiddleware(BaseMiddleware):
    """
    This middleware processes all response objects that returned from any handler.
    """

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
