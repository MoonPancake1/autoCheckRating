"""
Check my rating to HSU - файл с командами
"""


import os
import telebot
from app.messages_for_answer import *
from app.parse_work import *
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = os.getcwd()

bot = telebot.TeleBot(os.getenv('TELEGRAM_TOKEN'))
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, START_MESSAGE)
    user_id = message.chat.id
    
    send_menu_message(message)
    
@bot.message_handler(commands=['menu'])
def send_menu_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='СПбПУ 🥶', 
    callback_data='spbpu'))
    markup.add(telebot.types.InlineKeyboardButton(text='СПбГУТ 🥶', 
    callback_data='spbgut'))
    markup.add(telebot.types.InlineKeyboardButton(text='МИРЭА ⚡️', 
    callback_data='mirea'))
    markup.add(telebot.types.InlineKeyboardButton(text='УРФУ ⛰️', 
    callback_data='urfu'))
    markup.add(telebot.types.InlineKeyboardButton(text='АГТУ ☀️', 
    callback_data='agtu'))
    
    bot.send_message(message.chat.id, MENU_MESSAGE, 
                     reply_markup=markup, parse_mode='Markdown')
    

@bot.message_handler(commands=['spbpu'])
def send_spbpu_parse(message):
    """
    Парсинг данных с сайта СПбПУ
    """
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='К ВУЗам', 
    callback_data='menu'))
    
    bot.send_message(message.chat.id,
                    IN_DEVELOPMENT,
                    reply_markup=markup,
                    parse_mode="Markdown")
    

@bot.message_handler(commands=['spbgut'])
def send_spbgut_parse(message):
    """
    Парсинг данных с сайта СПбГУТ
    """
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='К ВУЗам', 
    callback_data='menu'))
    
    bot.send_message(message.chat.id,
                    IN_DEVELOPMENT,
                    reply_markup=markup,
                    parse_mode="Markdown")


@bot.message_handler(commands=['mirea'])
def send_mirea_parse(message):
    """
    Парсинг данных с сайта МИРЭА
    """
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='К ВУЗам', 
    callback_data='menu'))
    
    bot.send_message(message.chat.id,
                     '_Ожидайте пожалуйста..._',
                     parse_mode='Markdown',)
    
    data_parse = get_data_mirea_parse()
    
    mirea_message = generate_mirea_message(data_parse)
    
    bot.send_message(message.chat.id,
                    mirea_message,
                    parse_mode='Markdown',
                    reply_markup=markup)


@bot.message_handler(commands=['urfu'])
def send_urfu_parse(message):
    """
    Парсинг данных с сайта УРФУ
    """
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='К ВУЗам', 
    callback_data='menu'))
    
    bot.send_message(message.chat.id,
                     '_Ожидайте пожалуйста..._',
                     parse_mode='Markdown',)
    
    data_parse = get_data_urfu_parse()
    
    urfu_message = generate_urfu_message(data_parse)
    
    bot.send_message(message.chat.id,
                    urfu_message,
                    parse_mode='Markdown',
                    reply_markup=markup)


@bot.message_handler(commands=['agtu'])
def send_agtu_parse(message):
    """
    Парсинг данных с сайта АГТУ
    """
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='К ВУЗам', 
    callback_data='menu'))
    
    bot.send_message(message.chat.id,
                    IN_DEVELOPMENT,
                    reply_markup=markup,
                    parse_mode="Markdown")


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    req = call.data.split()
    
    if req[0] == 'spbpu':
        send_spbpu_parse(call.message)
    
    elif req[0] == 'spbgut':
        send_spbgut_parse(call.message)
    
    elif req[0] == 'mirea':
        send_mirea_parse(call.message)
    
    elif req[0] == 'urfu':
        send_urfu_parse(call.message)
    
    elif req[0] == 'agtu':
        send_agtu_parse(call.message)
    
    elif req[0] == 'menu':
        send_menu_message(call.message)