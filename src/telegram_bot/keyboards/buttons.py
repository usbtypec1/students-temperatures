from aiogram.types import KeyboardButton, InlineKeyboardButton

__all__ = (
    'MarkTemperatureButton',
    'ClassmatesListButton',
    'MyTemperatureHistoryButton',
)


class MarkTemperatureButton(KeyboardButton):

    def __init__(self):
        super().__init__('🌡 Отметить температуру')


class ClassmatesListButton(KeyboardButton):

    def __init__(self):
        super().__init__('👦 Одноклассники')


class MyTemperatureHistoryButton(KeyboardButton):

    def __init__(self):
        super().__init__('📆 История')


class MarkedTemperaturesReportButton(KeyboardButton):

    def __init__(self):
        super().__init__('📄 Отчёт о температурах учеников')


class NotifyToMarkTemperatureButton(InlineKeyboardButton):

    def __init__(self):
        super().__init__('🔈 Напомнить отметить температуру',
                         callback_data='notify-to-mark-temperature')