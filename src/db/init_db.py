import csv
import logging

from peewee import IntegrityError

import config
from db.models import User

with open(config.STUDENTS_CSV_FILE_PATH, encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)

    for telegram_id, first_name, last_name in reader:
        try:
            User.create(telegram_id=telegram_id, first_name=first_name, last_name=last_name)
        except IntegrityError:
            logging.debug('Could not create user in DB: '
                          f'{telegram_id=} {first_name=} {last_name=}')
