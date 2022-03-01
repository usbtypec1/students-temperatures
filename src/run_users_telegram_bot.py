from aiogram import executor

from users_telegram_bot import middlewares, handlers
from users_telegram_bot.bot import dp, on_bot_startup, setup_middlewares


def main():
    middlewares_for_setup = (middlewares.ProcessResponseMiddleware(),
                             middlewares.OnlyStudentsMiddleware(),)
    setup_middlewares(dp, middlewares_for_setup)
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
        on_startup=on_bot_startup,
    )


if __name__ == '__main__':
    main()
