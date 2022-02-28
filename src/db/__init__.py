from .engine import *
from .models import *
from .queries import *

database.create_tables((
    User,
    TemperatureRecord,
))
