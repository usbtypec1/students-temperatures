import pathlib

import pendulum

__all__ = (
    'BISHKEK_UTC',
    'DATABASE_PATH',
    'STUDENTS_FILE_PATH',
    'STUDENTS_CSV_FILE_PATH',
    'SRC_DIR',
    'NAME_MATCH_RATIO_THRESHOLD',
)

SRC_DIR = pathlib.Path(__file__).parent.parent

STUDENTS_FILE_PATH = SRC_DIR / 'config/students.json'

DATABASE_PATH = SRC_DIR / 'db/database.db'

BISHKEK_UTC = pendulum.timezone('Asia/Bishkek')

STUDENTS_CSV_FILE_PATH = SRC_DIR.parent / 'students.csv'

NAME_MATCH_RATIO_THRESHOLD = 33
