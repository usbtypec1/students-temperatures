from aiogram.types import Message

from telegram_bot.bot import dp


@dp.message_handler(
    state='*'
)
async def on_non_user_action(message: Message):
    await message.answer('Кажется вы не являетесь пользователем этого бота 😐.\n'
                         'Если вы считаете что это ошибка, свяжитесь с @usbtypec.\n'
                         f'Ваш ID: <code>{message.from_user.id}</code>')
