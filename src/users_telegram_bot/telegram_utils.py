from aiogram.utils.exceptions import TelegramAPIError

import db
from users_telegram_bot.bot import dp


async def send_message(chat_id: int, text: str) -> bool:
    """
    Try to send message to specific chat_id without any errors.
    On success returns True.
    """
    try:
        await dp.bot.send_message(chat_id, text)
    except TelegramAPIError:
        return False
    else:
        return True
