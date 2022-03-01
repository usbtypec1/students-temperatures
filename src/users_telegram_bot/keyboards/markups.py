from aiogram.types import ReplyKeyboardMarkup

from . import buttons

__all__ = (
    'MainMenuMarkup',
)


class MainMenuMarkup(ReplyKeyboardMarkup):

    def __init__(self):
        super().__init__(
            keyboard=[[buttons.MarkTemperatureButton()],
                      [buttons.ClassmatesListButton(), buttons.MyTemperatureHistoryButton()]],
            resize_keyboard=True,
        )
