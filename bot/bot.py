import telebot

API_TOKEN = '7687887794:AAFIOgETFuymVGizQipTmiqWAClBsaWt7OI'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я телеграм-бот внутри Docker!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling()