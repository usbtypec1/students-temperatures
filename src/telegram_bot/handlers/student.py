from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, Command
from aiogram.types import ChatType, ContentType, Message

import config
import db
from telegram_bot import filters, fsm_states, responses
from telegram_bot.bot import dp


@dp.message_handler(
    Text('👦 Одноклассники'),
    filters.OnlyStudentsFilter(),
    state='*',
    content_types=ContentType.TEXT,
)
@dp.message_handler(
    Command('classmates'),
    filters.OnlyStudentsFilter(),
    state='*',
    content_types=ContentType.TEXT,
)
async def on_classmates_command(message: Message, state: FSMContext):
    await state.finish()
    return responses.ClassmatesListResponse(db.User.select())


@dp.message_handler(
    Text('🌡 Отметить температуру'),
    filters.OnlyStudentsFilter(),
    state='*',
    content_types=ContentType.TEXT,
)
@dp.message_handler(
    Command('mark_temperature'),
    filters.OnlyStudentsFilter(),
    state='*',
    content_types=ContentType.TEXT,
)
async def on_mark_temperature_command(message: Message):
    await fsm_states.MarkTemperatureStates.temperature.set()
    return responses.MarkTemperatureFAQResponse()


@dp.message_handler(
    Text('📆 История'),
    filters.OnlyStudentsFilter(),
    chat_type=ChatType.PRIVATE,
    state='*',
    content_types=ContentType.TEXT,
)
@dp.message_handler(
    Command('history'),
    filters.OnlyStudentsFilter(),
    state='*',
    content_types=ContentType.TEXT,
)
async def on_history_command(message: Message, state: FSMContext, current_user: db.User):
    temperature_records = db.get_student_temperature_records(current_user, limit=10)
    await state.finish()
    return responses.TemperaturesHistoryResponse(temperature_records)


@dp.message_handler(
    filters.OnlyStudentsFilter(),
    filters.StudentOwnTemperatureFilter(),
    filters.ValidTemperatureFilter(),
    content_types=ContentType.TEXT,
    state=fsm_states.MarkTemperatureStates.temperature,
)
async def on_student_own_temperature_input(message: Message, current_user: db.User,
                                           temperature: float, state: FSMContext):
    today_temperature = db.get_today_student_temperature_or_none(current_user)
    if today_temperature is None:
        db.add_user_today_temperature(temperature, current_user)
    else:
        db.update_student_temperature_by_current_time(today_temperature, temperature, )
    await state.finish()
    return responses.MyTemperatureMarkedResponse()


@dp.message_handler(
    filters.OnlyStudentsFilter(),
    filters.ClassmateTemperatureFilter(),
    filters.ValidTemperatureFilter(),
    filters.NameMatchRatioThresholdFilter(config.NAME_MATCH_RATIO_THRESHOLD),
    content_types=ContentType.TEXT,
    state=fsm_states.MarkTemperatureStates.temperature,
)
async def on_classmate_temperature_input(
        message: Message, current_user: db.User, temperature: float,
        classmate_user: db.User, state: FSMContext):
    await state.finish()
    today_temperature = db.get_today_student_temperature_or_none(classmate_user)
    responses_on_success = (
        responses.ClassmateTemperatureSuccessfullyMarkedResponse(classmate_user, temperature),
        responses.OwnTemperatureMarkedByClassmateResponse(
            classmate_user.telegram_id, current_user, temperature)
    )
    if today_temperature is None:
        db.add_user_today_temperature(temperature, classmate_user, current_user)
        return responses_on_success
    elif today_temperature.recorded_by is not None:
        db.update_student_temperature_by_current_time(today_temperature, temperature, current_user)
        return responses_on_success
    elif today_temperature.recorded_by is None:
        return responses.ClassmateTemperatureAlreadyMarkedResponse()


@dp.message_handler(
    filters.OnlyStudentsFilter(),
    state='*',
    content_types=ContentType.TEXT,
)
async def on_student_start_command(message: Message):
    return responses.MainMenuResponse()
