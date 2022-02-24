import pathlib

import pendulum

__all__ = (
    'BISHKEK_UTC',
    'SRC_DIR',
    'STUDENTS_FILE_PATH',
    'DATABASE_PATH',
)

SRC_DIR = pathlib.Path(__file__).parent.parent

STUDENTS_FILE_PATH = SRC_DIR / 'config/students.json'

DATABASE_PATH = SRC_DIR / 'db/database.db'

BISHKEK_UTC = pendulum.timezone('Asia/Bishkek')
