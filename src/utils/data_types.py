from typing import NamedTuple

__all__ = (
    'StudentFromConfig',
)


class StudentFromConfig(NamedTuple):
    telegram_id: int
    first_name: str
    last_name: str
