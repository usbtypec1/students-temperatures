from typing import Optional, Iterable, Union

__all__ = (
    'parse_str_to_float',
    'parse_user_temperature_input',
    'get_user_with_most_similar_name',
)

from fuzzywuzzy import fuzz

import db


def parse_user_temperature_input(message_text: str) -> tuple[str, str]:
    temperature, *classmate = message_text.split()
    classmate = ' '.join(classmate).lower()
    return temperature, classmate


def parse_str_to_float(text: str, rounding: Optional[int] = None) -> float:
    parsed_float = float(text.replace(',', '.'))
    if rounding is not None:
        parsed_float = round(parsed_float, rounding)
    return parsed_float


def get_user_with_most_similar_name(first_name: str,
                                    users: Iterable[db.User]) -> tuple[db.User, int]:
    ratios = [(user, fuzz.ratio(first_name, user.first_name)) for user in users]
    return max(ratios, key=lambda x: x[1])


def is_temperature_in_valid_range(temperature: Union[int, float]) -> bool:
    return 30 < temperature < 45
