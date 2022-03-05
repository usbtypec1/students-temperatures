from typing import Union, Iterable

import db

__all__ = (
    'is_student_temperature_suspicious',
    'filter_and_sort_unique_dates',
)


def is_student_temperature_suspicious(
        temperature: Union[int, float], suspicious_temperature_threshold: int = 37) -> bool:
    """Check if student is sick by checking his temperature.

    Args:
        temperature: Student's temperature.
        suspicious_temperature_threshold: Student's temperature will be compared with this value.

    Returns:
        True if passed temperature is over than certain threshold, otherwise False.
    """
    return temperature >= suspicious_temperature_threshold


def filter_and_sort_unique_dates(
        temperature_records: Iterable[db.TemperatureRecord]) -> list[db.TemperatureRecord]:
    """Filter dates from TemperatureRecord objects.
    It might be useful if you want to get all dates when at least one temperature was recorded.

    Args:
        temperature_records: Collection that contains TemperatureRecord objects.

    Returns:
        Sorted(ASC) list of unique dates.
    """
    return sorted({record.recorded_at_date for record in temperature_records})
