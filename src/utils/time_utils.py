import pendulum

import config

__all__ = (
    'get_current_time',
    'get_today_date',
)


def get_today_date() -> pendulum.date:
    """Get current date in Bishkek (+6 GMT) UTC."""
    return pendulum.now(config.BISHKEK_UTC).date()


def get_current_time() -> pendulum.time:
    """Get current time in Bishkek (+6 GMT) UTC."""
    return pendulum.now(config.BISHKEK_UTC).time()
