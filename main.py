import requests
import time
data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    while True:
        bot.send_message(message.chat.id, data['Valute']['USD']['Value'])
        time.sleep(5)

# RUN
bot.polling(none_stop=True)