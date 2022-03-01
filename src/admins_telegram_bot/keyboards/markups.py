from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup

from admins_telegram_bot.keyboards import buttons

__all__ = (
    'MainMenuMarkup',
)


class MainMenuMarkup(ReplyKeyboardMarkup):

    def __init__(self):
        super().__init__(
            keyboard=[[buttons.MarkedTemperaturesReportButton()]],
            resize_keyboard=True,
        )
