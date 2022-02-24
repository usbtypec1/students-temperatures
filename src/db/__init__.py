from .engine import *
from .models import *

database.create_tables((
    User,
    TemperatureRecord,
))
