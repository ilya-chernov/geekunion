#Импорт библиотек и констант
import telebot
import mysql.connector
from bo_const import *
from mysql.connector import errorcode

#константы
# token = '5744505847:AAEaSl_GI5r5mc4YUgEYSYCSgcyQzjAolZk'
# bot = telebot.TeleBot(token)
# types = telebot.types


#основная часть кода

@bot.message_handler(commands=['start'])
def dialog_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    info_button = types.KeyboardButton('Регистрация')
    contact_button = types.KeyboardButton('Контакты')
    curs_button = types.KeyboardButton('Курсы')
    markup.add(info_button, contact_button,curs_button)
    bot.send_message(message.chat.id,'Hello World! Мы являемся онлайн-центом «NoName», цель которого является повышение '
                                     'квалификации участников среднего бизнеса. Мы проводим курсы повышения квалификации '
                                     'с присвоением соответствующих сертификатов.Выберите что-то из предложенных команд.',reply_markup=markup)

@bot.message_handler(content_types=['text'])
def text_message(message):
    if message.text == 'Регистрация':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton('URL', url='ProfiBoard.com')
        keyboard.add(url_button)
        bot.send_message(message.chat.id, 'Здесь вы можете зарегистрироваться на наши курсы', reply_markup=keyboard)
    if message.text =='Контакты':
        keyboard = types.InlineKeyboardMarkup()
        message_button = types.InlineKeyboardButton('@Aclyssgay')
        keyboard.add(message_button)
        bot.send_message(message.chat.id,'Мы в ТГ @Aclyssgay')
    elif message.text == 'Курсы':
        # Создаем панельку под сообщением
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton('URL', url='ProfiBoard.com')
        test_button = types.KeyboardButton('Назад')
        message_button = types.InlineKeyboardButton('',callback_data='message')  # лучше callback вносить в переменную, чтобы было удобно обрабатывать
        keyboard.add(url_button, message_button)
        bot.send_message(message.chat.id, 'Наши курсы', reply_markup=keyboard)


#активация бота
while True:
    try:
        bot.polling()
    except BaseException as error:
        print(error.__class__)
#cnx.close()
