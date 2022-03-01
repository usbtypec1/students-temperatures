from aiogram.types import KeyboardButton

__all__ = (
    'MarkedTemperaturesReportButton',
)


class MarkedTemperaturesReportButton(KeyboardButton):

    def __init__(self):
        super().__init__('📄 Отчёт о температурах учеников')
