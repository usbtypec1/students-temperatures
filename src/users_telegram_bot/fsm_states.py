from aiogram.dispatcher.filters.state import StatesGroup, State

__all__ = (
    'MarkTemperatureStates',
)


class MarkTemperatureStates(StatesGroup):
    temperature = State()
