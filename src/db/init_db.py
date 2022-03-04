import config
from db.engine import database
from db.models import User, TemperatureRecord

database.create_tables((
    User,
    TemperatureRecord,
))

telegram_id_to_user = {user.telegram_id: user for user in User.select()}

for student in config.STUDENTS:
    if student.telegram_id not in telegram_id_to_user:
        User.create(telegram_id=student.telegram_id,
                    first_name=student.first_name,
                    last_name=student.last_name)
