import config
from db.models import User

telegram_id_to_user = {user.telegram_id: user for user in User.select()}

for student in config.STUDENTS:
    if student.telegram_id not in telegram_id_to_user:
        User.create(telegram_id=student.telegram_id,
                    first_name=student.first_name,
                    last_name=student.last_name)
