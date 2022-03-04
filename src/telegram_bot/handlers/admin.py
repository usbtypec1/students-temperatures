from aiogram.dispatcher.filters import Text, Command
from aiogram.types import ContentType, Message, CallbackQuery

import db
from telegram_bot import responses, filters
from telegram_bot.bot import dp


@dp.callback_query_handler(
    filters.OnlyAdminsFilter(),
)
async def on_notify_to_mark_temperatures_cb(callback_query: CallbackQuery):
    await callback_query.answer()
    today_records = db.get_today_temperature_records()
    user_ids = [record.student.id for record in today_records]
    users_without_temperature_records = db.get_users_exclude_by_id(user_ids)
    mark_temperature_notifications = [
        responses.MarkTemperatureNotificationResponse(user.telegram_id)
        for user in users_without_temperature_records]
    return responses.NotificationsSentResponse(), *mark_temperature_notifications


@dp.message_handler(
    Text('📄 Отчёт о температурах учеников'),
    filters.OnlyAdminsFilter(),
    state='*',
    content_types=ContentType.TEXT,
)
@dp.message_handler(
    Command('temperatures_report'),
    filters.OnlyAdminsFilter(),
    state='*',
    content_types=ContentType.TEXT,
)
async def on_temperatures_report_command(message: Message):
    today_records = db.get_today_temperature_records()
    user_ids = [record.student.id for record in today_records]
    users_without_temperature_records = db.get_users_exclude_by_id(user_ids)
    return (responses.MarkedTemperaturesReportResponse(today_records),
            responses.StudentsWithoutTemperatureRecordsResponse(users_without_temperature_records))


@dp.message_handler(
    filters.OnlyAdminsFilter(),
    state='*',
    content_types=ContentType.TEXT,
)
async def on_admin_start_command(message: Message):
    return responses.AdminMenuResponse()
