import contextlib
from typing import Union, Iterable

from aiogram import Bot
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from aiogram.utils.exceptions import TelegramAPIError

from telegram_bot.responses import Response


class ProcessResponseMiddleware(BaseMiddleware):
    """
    This middleware processes all response objects that returned from any handler.
    """

    def __init__(self, bot: Bot):
        super().__init__()
        self._bot = bot

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
                await self._bot.send_message(chat_id, text, reply_markup=reply_markup)

    async def on_post_process_callback_query(self, callback_query: CallbackQuery,
                                             data_from_handler: list, data: dict):
        if not data_from_handler:
            return
        responses: Union[Response, Iterable[Response]] = data_from_handler[0]
        if isinstance(responses, Response):
            responses = [responses]
        for response in responses:
            text, reply_markup = response.get_text(), response.get_reply_markup()
            chat_id = response.get_chat_id() or callback_query.message.chat.id
            with contextlib.suppress(TelegramAPIError):
                await self._bot.send_message(chat_id, text, reply_markup=reply_markup)
