import pendulum

import config

__all__ = (
    'get_current_time',
    'get_today_date',
)


def get_today_date() -> pendulum.date:
    return pendulum.now(config.BISHKEK_UTC).date()


def get_current_time() -> pendulum.time:
    return pendulum.now(config.BISHKEK_UTC).time()
