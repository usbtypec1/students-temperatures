import os

__all__ = (
    'DATABASE_URL',
)

DATABASE_URL = os.getenv('DATABASE_URL')

if DATABASE_URL is None:
    print('DATABASE_URL environment variable is not set up')
else:
    DATABASE_URL = '://'.join(('postgresql+asyncpg', DATABASE_URL.split('://')[1]))
