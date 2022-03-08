from typing import Union

from aiogram.dispatcher.filters import BoundFilter
from aiogram.dispatcher.handler import CancelHandler, SkipHandler
from aiogram.types import Message

import config
import db
from telegram_bot import parsers

__all__ = (
    'ClassmateTemperatureFilter',
    'NameMatchRatioThresholdFilter',
    'ValidTemperatureFilter',
    'StudentOwnTemperatureFilter',
    'OnlyAdminsFilter',
    'OnlyStudentsFilter',
)


class ClassmateTemperatureFilter(BoundFilter):
    """
    This filter ensures that user is going to mark classmate's temperature.
    Also filter passes out temperature that user entered.
    To handle it, define 'temperature'(float) as argument in your handler.
    """
    key = 'classmate_temperature'

    async def check(self, message: Message) -> bool:
        _, classmate_name = parsers.parse_user_temperature_input(message.text)
        return bool(classmate_name)


class StudentOwnTemperatureFilter(BoundFilter):
    """
    This filter ensures that user is going to mark his own temperature.
    """
    key = 'student_own_temperature'

    async def check(self, message: Message) -> bool:
        _, classmate_name = parsers.parse_user_temperature_input(message.text)
        return not classmate_name


class ValidTemperatureFilter(BoundFilter):
    """
    This filter validates temperature and classmate's name (if passed).
    Also filter passes out them into handler.
    """
    key = 'valid_temperature'

    async def check(self, message: Message) -> Union[bool, dict]:
        temperature, classmate_name = parsers.parse_user_temperature_input(message.text)
        try:
            temperature = parsers.parse_str_to_float(temperature, rounding=1)
        except ValueError:
            await message.answer('Неправильно введена температура')
            raise CancelHandler
        if not parsers.is_temperature_in_valid_range(temperature):
            await message.answer('🥶 Температура живого человека должна быть '
                                 'от 30 до 45 °C 🥵')
            raise CancelHandler
        return {'temperature': temperature, 'classmate_name': classmate_name}


class NameMatchRatioThresholdFilter(BoundFilter):
    """
    This filter ensures classmate's name that user entered matches to any classmate.
    Also filter passes out that classmate's user object and matched ratio in percent.
    """
    key = 'name_match_ratio_threshold'

    def __init__(self, ratio_threshold: Union[int, float]):
        self.__ratio_threshold = ratio_threshold

    async def check(self, message: Message) -> Union[bool, dict]:
        all_students = db.User.select()
        _, classmate_name = parsers.parse_user_temperature_input(message.text)
        student, ratio = parsers.get_user_with_most_similar_name(classmate_name, all_students)
        if ratio < self.__ratio_threshold:
            await message.answer(f'Ученик по имени <b>{classmate_name}</b> не найден')
            raise CancelHandler
        return {'classmate_user': student, 'ratio': ratio}


class OnlyAdminsFilter(BoundFilter):

    key = 'only_admins'

    async def check(self, message: Message) -> Union[dict, bool]:
        return message.from_user.id in config.ADMIN_CHAT_IDS


class OnlyStudentsFilter(BoundFilter):

    key = 'only_students'

    async def check(self, message: Message) -> Union[dict, bool]:
        user_or_none = db.get_user_or_none_by_telegram_id(message.from_user.id)
        if user_or_none is None:
            return False
        return {'current_user': user_or_none}
