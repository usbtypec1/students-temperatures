import random
from typing import Optional, Union, Iterable

from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup

__all__ = (
    'KeyboardMarkup',
    'Response',
)

import db
from telegram_bot.keyboards import markups

KeyboardMarkup = Union[ReplyKeyboardMarkup, InlineKeyboardMarkup]


class Response:

    def get_chat_id(self) -> Optional[int]:
        """Override if you want to send response to certain chat."""

    def get_text(self) -> Optional[str]:
        """Override if you want to return any text."""

    def get_reply_markup(self) -> Optional[KeyboardMarkup]:
        """Override if you want to return any type of keyboard markup."""


class AdminMenuResponse(Response):

    def get_text(self) -> Optional[str]:
        return 'Главное меню 👨‍💻'

    def get_reply_markup(self) -> Optional[KeyboardMarkup]:
        return markups.AdminMenuMarkup()


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


class ClassmatesListResponse(Response):
    __slots__ = ('__users',)

    __emojis = ('❤️', '🌈', '💩', '⚡️', '☠️', '🧡', '💗', '👑', '🐺',
                '💛', '💚', '💙', '💜', '🖤', '☢', '🐱', '🐽', '🍆', '🍑')

    def __init__(self, users: Iterable[db.User]):
        self.__users = users

    def get_text(self) -> str:
        if not self.__users:
            return 'У вас нет одноклассников 😕'
        lines = ['<b>Ваши любимые одноклассники:</b>']
        lines += [f'{random.choice(self.__emojis)} {user.first_name.title()}'
                  for user in self.__users]
        return '\n'.join(lines)


class TemperaturesHistoryResponse(Response):
    __slots__ = ('__temperature_records',)

    def __init__(self, temperature_records: Iterable[db.TemperatureRecord]):
        self.__temperature_records = temperature_records

    def get_text(self) -> Optional[str]:
        if not self.__temperature_records:
            return 'Вы пока ни разу не отмечали свою температуру 😢'
        lines = ['<b>История моих отметок температур:</b>']
        for record in self.__temperature_records:
            line = (f'{record.recorded_at_date:%d.%m.%Y} {record.edited_at_time:%H:%M}'
                    f' - <b>{record.temperature_value} °C</b>')
            if record.recorded_by is not None:
                line += f' ({record.recorded_by.first_name.title()})'
            lines.append(line)
        return '\n'.join(lines)


class MarkTemperatureFAQResponse(Response):

    def get_text(self) -> Optional[str]:
        lines = (
            'Чтобы отметить температуру, просто напишите её сюда',
            '👉 Например: <i>36.9</i>\n',
            'Также вы можете отметить температуру за своего одноклассника,'
            ' отправив температуру в таком виде: \n<i>42.6 Асхат</i> или <i>36.9 Мин джу</i>\n',
            'Чтобы посмотреть имена одноклассников (если ты вдруг забыл),'
            ' нажмите на кнопку <b>"👦 Одноклассники"</b> в главном меню или введите /classmates')
        return '\n'.join(lines)


class ClassmateTemperatureAlreadyMarkedResponse(Response):

    def get_text(self) -> Optional[str]:
        return 'Этот ученик уже отметил себе температуру 👌'


class ClassmateTemperatureSuccessfullyMarkedResponse(Response):
    __slots__ = ('__classmate_user', '__temperature')

    def __init__(self, classmate_user: db.User, temperature: float):
        self.__classmate_user = classmate_user
        self.__temperature = temperature

    def get_text(self) -> Optional[str]:
        return (f'Вы отметили температуру ученику {self.__classmate_user.first_name.title()}'
                f' как {self.__temperature:.1f} 🌟')


class OwnTemperatureMarkedByClassmateResponse(Response):
    __slots__ = ('__chat_id', '__current_user', '__temperature')

    def __init__(self, chat_id: int, current_user: db.User, temperature: float):
        self.__chat_id = chat_id
        self.__current_user = current_user
        self.__temperature = temperature

    def get_chat_id(self) -> Optional[int]:
        return self.__chat_id

    def get_text(self) -> Optional[str]:
        return (f'{self.__current_user.first_name.title()} отметил'
                f' вам температуру {self.__temperature:.1f} 🌟')


class MyTemperatureMarkedResponse(Response):

    def get_text(self) -> Optional[str]:
        return 'Ваша сегодняшняя температура обновлена 😍'


class MainMenuResponse(Response):

    def get_text(self) -> Optional[str]:
        return 'Главное меню 🧑‍💻'

    def get_reply_markup(self) -> Optional[KeyboardMarkup]:
        return markups.MainMenuMarkup()


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
            return markups.NotMarkedTemperaturesMenuMarkup()
