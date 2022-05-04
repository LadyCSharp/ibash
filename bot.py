import telebot
from telebot import apihelper
import time
import os
from parser_ibash import pibash

TOKEN='sensored'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
help='/timer - Таймер на 10 секунд \n/ibash - Три цитаты с ibash по ключевым словам\n/help - помощь\n/echo - эхо\n/rev - перевернутое эхо'
@bot.message_handler(commands=[ 'help'])
def send_help(message):
    bot.reply_to(message, help)
# Команда в параметром
@bot.message_handler(commands=['say'])
def say(message):
    # получить то что после команды
    text = ' '.join(message.text.split(' ')[1:])
    bot.reply_to(message, f'***{text.upper()}!***')


@bot.message_handler(commands=['rev'])
def rev(message):
    # получить то что после команды
    text = ' '.join(message.text.split(' ')[1:])
    bot.reply_to(message, text[-1::-1])


@bot.message_handler(commands=['echo'])
def echo(message):
    # получить то что после команды

    bot.reply_to(message, ' '.join(message.text.split(' ')[1:]))

@bot.message_handler(commands=['ibash'])
def ibash(message):
    # получить то что после команды
    mess = pibash( message.text.split(' ')[1:])

    bot.reply_to(message, mess)


# Обработка команд
@bot.message_handler(commands=['timer'])
def timer(message):
    for i in range(10):
        time.sleep(1)
        bot.send_message(message.chat.id, i + 1)

@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    FILE_ID = 'CAADAgADPQMAAsSraAsqUO_V6idDdBYE'
    bot.send_sticker(message.chat.id, FILE_ID)


bot.polling()
