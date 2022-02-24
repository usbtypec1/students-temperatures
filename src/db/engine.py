from peewee import SqliteDatabase

import config

__all__ = (
    'database',
)

database = SqliteDatabase(config.DATABASE_PATH)
