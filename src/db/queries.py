from typing import Optional, Iterable

import db
from db.models import User, TemperatureRecord
from utils import time_utils

__all__ = (
    'get_user_or_none_by_telegram_id',
    'get_temperature_by_record_date_or_none',
    'get_today_student_temperature_or_none',
    'add_user_today_temperature',
    'get_student_temperature_records',
    'update_student_temperature_by_current_time',
    'get_today_temperature_records',
    'get_users_exclude_by_id',
    'get_user_telegram_ids',
)


def get_user_or_none_by_telegram_id(telegram_id: int) -> User:
    return User.get_or_none(telegram_id=telegram_id)


def get_temperature_by_record_date_or_none(user: User, record_date: str) -> TemperatureRecord:
    return TemperatureRecord.get_or_none(student=user, recorded_at_date=record_date)


def get_student_temperature_records(
        user: User, limit: Optional[int] = None) -> Iterable[TemperatureRecord]:
    query = (TemperatureRecord.select()
             .where(TemperatureRecord.student == user)
             .order_by(TemperatureRecord.recorded_at_date.desc()))
    if limit is not None:
        query.limit(limit)
    return query.execute()


def get_today_student_temperature_or_none(user: User) -> TemperatureRecord:
    record_date = time_utils.get_today_date().isoformat()
    return get_temperature_by_record_date_or_none(user, record_date)


def add_user_today_temperature(temperature_value: float, student: User,
                               recorded_by: Optional[User] = None):
    edited_at_time = time_utils.get_current_time().isoformat()
    recorded_at_date = time_utils.get_today_date().isoformat()
    return TemperatureRecord.create(
        student=student, recorded_by=recorded_by, temperature_value=temperature_value,
        edited_at_time=edited_at_time, recorded_at_date=recorded_at_date)


def update_student_temperature_by_current_time(
        today_temperature: TemperatureRecord, temperature_value: float,
        recorded_by: Optional[db.User] = None):
    TemperatureRecord.update(
        temperature_value=temperature_value,
        recorded_by=recorded_by,
        recorded_at_date=time_utils.get_today_date().isoformat(),
        edited_at_time=time_utils.get_current_time().isoformat(),
    ).where(TemperatureRecord.id == today_temperature.id).execute()


def get_today_temperature_records() -> Iterable[TemperatureRecord]:
    today_date = time_utils.get_today_date().isoformat()
    return (TemperatureRecord.select(TemperatureRecord, User)
            .join(User, on=(User.id == TemperatureRecord.student))
            .where(TemperatureRecord.recorded_at_date == today_date).execute())


def get_users_exclude_by_id(user_ids: Iterable[int]) -> Iterable[User]:
    return User.select().where(User.id.not_in(user_ids)).execute()


def get_user_telegram_ids() -> list[int]:
    return [user.telegram_id for user in User.select()]
