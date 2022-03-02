from aiogram.types import KeyboardButton, InlineKeyboardButton

__all__ = (
    'MarkedTemperaturesReportButton',
    'NotifyToMarkTemperatureButton',
)


class MarkedTemperaturesReportButton(KeyboardButton):

    def __init__(self):
        super().__init__('📄 Отчёт о температурах учеников')


class NotifyToMarkTemperatureButton(InlineKeyboardButton):

    def __init__(self):
        super().__init__('🔈 Напомнить отметить температуру',
                         callback_data='notify-to-mark-temperature')
