from aiogram import executor

from admins_telegram_bot import handlers
from admins_telegram_bot.bot import dp, on_startup


def main():
    executor.start_polling(
        dispatcher=dp,
        on_startup=on_startup,
        skip_updates=True,
    )


if __name__ == '__main__':
    main()
