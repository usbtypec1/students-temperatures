import json
import pathlib

import pendulum

from utils import data_types

__all__ = (
    'BISHKEK_UTC',
    'ADMIN_CHAT_IDS_PATH',
    'STUDENTS_FILE_PATH',
    'SRC_DIR',
    'NAME_MATCH_RATIO_THRESHOLD',
    'TMP_FOLDER_PATH',
    'ADMIN_CHAT_IDS',
    'STUDENTS',
)

SRC_DIR = pathlib.Path(__file__).parent.parent

STUDENTS_FILE_PATH = pathlib.Path.joinpath(SRC_DIR.parent, 'initial_data', 'students.json')

ADMIN_CHAT_IDS_PATH = pathlib.Path.joinpath(SRC_DIR.parent, 'initial_data', 'admins.json')

BISHKEK_UTC = pendulum.timezone('Asia/Bishkek')

NAME_MATCH_RATIO_THRESHOLD = 33

TMP_FOLDER_PATH = SRC_DIR / 'tmp'


with open(ADMIN_CHAT_IDS_PATH, encoding='utf-8') as admin_chat_ids_file:
    ADMIN_CHAT_IDS: list[int] = json.load(admin_chat_ids_file)

with open(STUDENTS_FILE_PATH, encoding='utf-8') as students_file:
    STUDENTS = [(data_types.StudentFromConfig(**student))
                for student in json.load(students_file)]
