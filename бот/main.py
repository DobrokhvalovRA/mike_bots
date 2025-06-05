import os
import random

import dp
import telebot
import telegram
from telebot import types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup, InlineKeyboardButton


bot_token = '7884231655:AAGYAbYDB0iv5d1wlXzHMeXSek7s4jH_K3w'
#bot = telebot.TeleBot("7884231655:AAGYAbYDB0iv5d1wlXzHMeXSek7s4jH_K3w")
token = str(os.environ.get('7884231655:AAGYAbYDB0iv5d1wlXzHMeXSek7s4jH_K3w'))
bot = telebot.TeleBot('7884231655:AAGYAbYDB0iv5d1wlXzHMeXSek7s4jH_K3w')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=4)
    markup.add(
        types.InlineKeyboardButton("♑",callback_data='козерог'),
        types.InlineKeyboardButton("♎",callback_data='весы'),
        types.InlineKeyboardButton("♍",callback_data='дева'),
        types.InlineKeyboardButton("♏",callback_data='скорпион'),
        types.InlineKeyboardButton("♓",callback_data='рыбы'),
        types.InlineKeyboardButton("♌",callback_data='лев'),
        types.InlineKeyboardButton("♒",callback_data='водолей'),
        types.InlineKeyboardButton("♐",callback_data='стрелец'),
        types.InlineKeyboardButton("♋",callback_data='рак'),
        types.InlineKeyboardButton("♊",callback_data='близнецы'),
        types.InlineKeyboardButton("♉",callback_data='телец'),
        types.InlineKeyboardButton("♈",callback_data='овен'))
    bot.reply_to(message, "Добро пожаловать в игру 'Гороскоп на день '! Узнай что ожидает тебя сегодня по твоему знаку зодиака:", reply_markup=markup)

fraizes = ["День пройдёт неплохо, если удастся избежать лишнего риска и конфликтов." , "Споры могут возникнуть, но их можно вести конструктивно, не переходя на личности.",
"Стоит найти способ смягчить напряжение с теми, кто усложняет жизнь.",
"Вероятны бытовые проблемы, решить которые придётся незапланированными расходами."]
@bot.callback_query_handler(lambda c: c.data)
def process_callback(callback_query: types.CallbackQuery):
    match callback_query.data:
            case "козерог":
                  bot.send_message(callback_query.from_user.id, text="Козерогов сегодня ждет",)
            case "весы":
                bot.send_message(callback_query.from_user.id, text="Весов сегодня ждет")
            case "дева":
                bot.send_message(callback_query.from_user.id, text="Дев сегодня ждет")
            case "скорпион":
                bot.send_message(callback_query.from_user.id, text="Скорпионов сегодня ждет")
            case "рыбы":
                bot.send_message(callback_query.from_user.id, text="Рыб сегодня ждет")
            case "лев":
                bot.send_message(callback_query.from_user.id, text="Львов сегодня ждет")
            case "водолей":
                bot.send_message(callback_query.from_user.id, text="Водолеев сегодня ждет")
            case "стрелец":
                bot.send_message(callback_query.from_user.id, text="Стрельцов сегодня ждет")
            case "рак":
                bot.send_message(callback_query.from_user.id, text="Раков сегодня ждет")
            case "близнецы":
                bot.send_message(callback_query.from_user.id, text="Близнецов сегодня ждет")
            case "телец":
                bot.send_message(callback_query.from_user.id, text="Тельцов сегодня ждет")
            case "овен":
                bot.send_message(callback_query.from_user.id, text="Овенов сегодня ждет")
            case "_":
                bot.answer_callback_query(callback_query.from_user.id, text="Получены неизвестные данные: {callback_data}")
bot.polling()
