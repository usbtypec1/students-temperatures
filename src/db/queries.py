from typing import Optional, Iterable

from db.models import User, TemperatureRecord
from utils import time_utils

__all__ = (
    'get_user_or_none_by_telegram_id',
    'get_temperature_by_record_date_or_none',
    'get_today_student_temperature_or_none',
    'add_user_today_temperature',
    'get_student_temperature_records',
    'update_student_temperature_by_current_time',
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
        today_temperature: TemperatureRecord, temperature_value: float):
    TemperatureRecord.update(
        temperature_value=temperature_value,
        recorded_at_date=time_utils.get_today_date().isoformat(),
        edited_at_time=time_utils.get_current_time().isoformat(),
    ).where(TemperatureRecord == today_temperature).execute()
