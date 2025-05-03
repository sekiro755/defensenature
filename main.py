import telebot
from config import API_TOKEN
import os
import random
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton





bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Это бот по проверке твоих знаний насчет борьбы с загрязнением окружающей среды, если что то не помнишь пропиши /info, если готов то пиши /ready')
    


def inform_url():    
        url = 'https://school-science.ru/24/8/60816'
        return url

@bot.message_handler(commands=['info'])
def info_url(message):
    information_url = inform_url()
    bot.reply_to(message, information_url)


def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("49", callback_data="cb_11"),
                               InlineKeyboardButton("51", callback_data="cb_13"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_11":
        bot.answer_callback_query(call.id, "Верно! Ты молодец")
    elif call.data == "cb_13":
        bot.answer_callback_query(call.id, "Нет.. но если вдруг знаешь больше ты молодец")

@bot.message_handler(func=lambda message: True)
def message_handler(message):
    bot.send_message(message.chat.id, "Сколько способов ты изучил в данном справочнике?", reply_markup=gen_markup())

    

    




bot.infinity_polling()
