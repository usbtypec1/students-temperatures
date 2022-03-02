from typing import Optional, Iterable

import db
from admins_telegram_bot import keyboards
from common.responses import Response, KeyboardMarkup

__all__ = (
    'MainMenuResponse',
    'StudentsWithoutTemperatureRecordsResponse',
    'MarkedTemperaturesReportResponse',
    'MarkTemperatureNotificationResponse',
    'NotificationsSentResponse',
)


class MarkedTemperaturesReportResponse(Response):
    __slots__ = ('__records',)

    def __init__(self, records: Iterable[db.TemperatureRecord]):
        self.__records = records

    def get_text(self) -> Optional[str]:
        if not self.__records:
            return 'Пока никто не отметил свою температуру 😕'
        lines = ['<b>Температуры учеников:</b>']
        lines += [f'{report.student.first_name.title()}: {report.temperature_value:.1f}'
                  for report in self.__records]
        return '\n'.join(lines)


class StudentsWithoutTemperatureRecordsResponse(Response):
    __slots__ = ('__users_without_records',)

    def __init__(self, users_without_records: Iterable[db.User]):
        self.__users_without_records = users_without_records

    def get_text(self) -> Optional[str]:
        if not self.__users_without_records:
            return 'Все отметили температуру 🥳'
        lines = ['<b>Ещё не отметили температуру:</b>']
        lines += [f'{user.first_name.title()}' for user in self.__users_without_records]
        return '\n'.join(lines)

    def get_reply_markup(self) -> Optional[KeyboardMarkup]:
        if self.__users_without_records:
            return keyboards.NotMarkedTemperaturesMenuMarkup()


class MainMenuResponse(Response):

    def get_text(self) -> Optional[str]:
        return 'Главное меню 👨‍💻'

    def get_reply_markup(self) -> Optional[KeyboardMarkup]:
        return keyboards.MainMenuMarkup()


class MarkTemperatureNotificationResponse(Response):
    __slots__ = ('__chat_id',)

    def __init__(self, chat_id: int):
        self.__chat_id = chat_id

    def get_chat_id(self) -> Optional[int]:
        return self.__chat_id

    def get_text(self) -> Optional[str]:
        return 'Пожалуйста, отметьте вашу температуру ❗️'


class NotificationsSentResponse(Response):

    def get_text(self) -> Optional[str]:
        return 'Напоминания отправлены 👌'
