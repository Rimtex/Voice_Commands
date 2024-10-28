import telebot

# Введите сюда ваш токен
API_TOKEN = '7015949895:AAGGtCsnPvfGS_PeiWSou8gSHsmnW-yqlf8'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я простой бот.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
