import os
import urllib.parse

__all__ = (
    'TELEGRAM_BOT_TOKEN',
    'DATABASE',
)


TELEGRAM_BOT_TOKEN: str = os.getenv('TELEGRAM_BOT_TOKEN')
DATABASE: urllib.parse.ParseResult = urllib.parse.urlparse(os.getenv('DATABASE_URL'))
