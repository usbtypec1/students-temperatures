from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup

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


class AdminMenuMarkup(ReplyKeyboardMarkup):

    def __init__(self):
        super().__init__(
            keyboard=[[buttons.MarkedTemperaturesReportButton()],
                      [buttons.DownloadExcelReportFileButton()]],
            resize_keyboard=True,
        )


class NotMarkedTemperaturesMenuMarkup(InlineKeyboardMarkup):

    def __init__(self):
        super().__init__()
        self.add(buttons.NotifyToMarkTemperatureButton())
