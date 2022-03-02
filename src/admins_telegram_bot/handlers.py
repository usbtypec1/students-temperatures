from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ChatType, ContentType

import db
from admins_telegram_bot.bot import dp
from admins_telegram_bot import responses


@dp.message_handler(
    Text('📄 Отчёт о температурах учеников'),
    chat_type=ChatType.PRIVATE,
    state='*',
    content_types=ContentType.TEXT,
)
@dp.message_handler(
    Command('temperatures_report'),
    chat_type=ChatType.PRIVATE,
    state='*',
    content_types=ContentType.TEXT,
)
async def on_temperatures_report_command(message: Message):
    today_records = db.get_today_temperature_records()
    user_ids = [record.student.id for record in today_records]
    users_without_temperature_records = db.get_users_exclude_by_id(user_ids)
    return responses.TemperaturesReportResponse(today_records, users_without_temperature_records)


@dp.message_handler(
    chat_type=ChatType.PRIVATE,
    state='*',
    content_types=ContentType.TEXT,
)
async def on_start_command(message: Message):
    return responses.MainMenuResponse()
