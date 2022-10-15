import telebot
from functions import Token, cat, out

bot = telebot.TeleBot(Token)


def on_startup(_):
    print('Бот\n@cuteness_helper_bot\nзапущен', cat)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.answer_callback_query(message.chat.id,
                              'Привет, этот бот создан, чтобы пересылать сообщения в отдельный канал')


@bot.message_handler(commands=['F'])
def forward(message):
    bot.forward_message(message_id=message.id, from_chat_id='-1001523047524')


if __name__ == '__main__':
    bot.infinity_polling()
