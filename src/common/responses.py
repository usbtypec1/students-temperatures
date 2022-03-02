from typing import Optional, Union

from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup

__all__ = (
    'KeyboardMarkup',
    'Response',
)

KeyboardMarkup = Union[ReplyKeyboardMarkup, InlineKeyboardMarkup]


class Response:

    def get_chat_id(self) -> Optional[int]:
        """Override if you want to send response to certain chat."""

    def get_text(self) -> Optional[str]:
        """Override if you want to return any text."""

    def get_reply_markup(self) -> Optional[KeyboardMarkup]:
        """Override if you want to return any type of keyboard markup."""
