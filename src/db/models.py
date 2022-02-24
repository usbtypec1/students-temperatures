from peewee import (
    CharField,
    ForeignKeyField,
    Model,
    BigIntegerField,
    FloatField,
    DateTimeField,
)

from db.engine import database

__all__ = (
    'TemperatureRecord',
    'User',
)


class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    telegram_id = BigIntegerField(unique=True, index=True)
    first_name = CharField(max_length=64)
    last_name = CharField(max_length=64)

    def __repr__(self):
        return f'<User: {self.last_name} {self.first_name}>'

    class Meta:
        table_name = 'users'


class TemperatureRecord(BaseModel):
    student = ForeignKeyField(User, on_delete='CASCADE')
    recorded_by = ForeignKeyField(User, on_delete='CASCADE')
    temperature_value = FloatField()
    edited_at = DateTimeField()

    def __repr__(self):
        return f'<Temperature Record: {self.id}>'

    class Meta:
        table_name = 'temperature_records'
