from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup
from functions import Token, cat

bot = Bot(token=Token)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот\n@first_edu_aiogram_bot\nзапущен', cat)

# @dp.
async def welcome():








if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
