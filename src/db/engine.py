from peewee import PostgresqlDatabase

import config

__all__ = (
    'database',
)

database = PostgresqlDatabase(
    port=config.DATABASE.port,
    user=config.DATABASE.username,
    host=config.DATABASE.hostname,
    password=config.DATABASE.password,
    database=config.DATABASE.path.lstrip('/'),
    autorollback=True,
)
