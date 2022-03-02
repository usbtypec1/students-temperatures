from aiogram import executor

from users_telegram_bot import handlers
from users_telegram_bot.bot import dp, on_bot_startup


def main():
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
        on_startup=on_bot_startup,
    )


if __name__ == '__main__':
    main()
