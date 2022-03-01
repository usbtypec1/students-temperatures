from aiogram import executor

from admins_telegram_bot import middlewares, handlers
from admins_telegram_bot.bot import dp, setup_middlewares


def main():
    middlewares_for_setup = (
        middlewares.ProcessResponseMiddleware(),
        middlewares.OnlyAdminsMiddleware(),
    )
    setup_middlewares(dp, middlewares_for_setup)
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
    )


if __name__ == '__main__':
    main()
