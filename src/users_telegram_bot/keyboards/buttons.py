from aiogram.types import KeyboardButton

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
