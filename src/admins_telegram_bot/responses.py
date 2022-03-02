from typing import Optional, Iterable

import db
from admins_telegram_bot import keyboards
from common.responses import Response, KeyboardMarkup

__all__ = (
    'MainMenuResponse',
    'TemperaturesReportResponse',
)


class TemperaturesReportResponse(Response):
    __slots__ = ('__records', '__users_without_records')

    def __init__(self, records: Iterable[db.TemperatureRecord],
                 users_without_records: Iterable[db.User]):
        self.__records = records
        self.__users_without_records = users_without_records

    def get_text(self) -> Optional[str]:
        if not self.__records:
            return 'Никто пока не отметил свою температуру 😕'
        lines = ['Отметили температуру:']
        lines += [f'{report.student.first_name.title()}: {report.temperature_value:.1f}'
                  for report in self.__records]
        lines += ['\nЕщё не отметили температуру:']
        lines += [f'{user.first_name.title()}' for user in self.__users_without_records]
        return '\n'.join(lines)


class MainMenuResponse(Response):

    def get_text(self) -> Optional[str]:
        return 'Главное меню 👨‍💻'

    def get_reply_markup(self) -> Optional[KeyboardMarkup]:
        return keyboards.MainMenuMarkup()
