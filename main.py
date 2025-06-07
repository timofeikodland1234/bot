import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from q import *
bot = telebot.TeleBot("7814433366:AAH5so3TXjAx1W5GSTsNFnAktiFitkR7UPo")

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = InlineKeyboardMarkup()
    keyboard.row(
        InlineKeyboardButton("что сделало глобальное потепление?", callback_data="q1")
    )
    keyboard.row(
        InlineKeyboardButton("Из за чего произошло глобальное потепление?)", callback_data="q2")
    )
    keyboard.row(
        InlineKeyboardButton("Можно ли остановить глобальное потепление?", callback_data="q3")
    )
    keyboard.row(
        InlineKeyboardButton("К чему все это привести?)", callback_data="q4"))
    keyboard.row(
        InlineKeyboardButton("Что же мешает это сделать?)", callback_data="q5"))

    bot.send_message(message.chat.id, "Выберите вопрос:", reply_markup=keyboard)

# Ответы на нажатие кнопок
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "q1":
        bot.send_message(call.message.chat.id, q1)
    elif call.data == "q2":
        bot.send_message(call.message.chat.id, q2)

    elif call.data == "q3":
        bot.send_message(call.message.chat.id, q3)
    elif call.data == "q4":
        bot.send_message(call.message.chat.id, q4)
    elif call.data == "q5":
        bot.send_message(call.message.chat.id, q5)
    else:
        bot.send_message(call.message.chat.id, "Неизвестный вопрос.")

bot.infinity_polling()