from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup
from functions import Token, cat

bot = Bot(token=Token)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот\n@first_edu_aiogram_bot\nзапущен', cat)


@dp.message_handler(commands=['start'])
async def welcome(message: types.message):
    await bot.send_message(message.from_user.id, 'Привет, этот бот создан, чтобы пересылать сообщения в отдельный канал')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
