#Импорт библиотек и констант
import telebot
from bo_const import *

#основная часть кода

@bot.callback_query_handler(lambda call: True)
def callback_handler(call):
    if call.data == 'pressed_call':
        bot.send_message(call.from_user.id,'@Aclyssgay')

@bot.message_handler(commands=['start'])
def dialog_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    info_button = types.KeyboardButton('Регистрация')
    contact_button = types.KeyboardButton('Контакты')
    curs_button = types.KeyboardButton('Курсы')
    markup.add(info_button, contact_button,curs_button)
    bot.send_message(message.chat.id,'Hello World! Мы являемся онлайн-центом «ProfiBoard», цель которого является повышение '
                                     'квалификации участников среднего бизнеса. Мы проводим курсы повышения квалификации '
                                     'с присвоением соответствующих сертификатов.Выберите что-то из предложенных команд.',reply_markup=markup)

@bot.message_handler(commands=['contacts'])
def button(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_call = telebot.types.InlineKeyboardButton('Контакты',callback_data='pressed_call')
    keyboard.add(button_call)
    bot.send_message(message.chat.id, 'По вопросам обращасться', reply_markup=keyboard)

@bot.message_handler(commands=['curses'])
def button(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton('URL', url='ProfiBoard.com')
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Наши курсы', reply_markup=keyboard)

@bot.message_handler(commands=['registration'])
def button(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton('URL', url='https://profidesk.ichernov.ru/')
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Здесь вы можете ознакомится с нашим сайтом, почитать дайджесты и про нас',reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def text_message(message):
    if message.text == 'Регистрация':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton('URL', url='https://profidesk.ichernov.ru/')
        keyboard.add(url_button)
        bot.send_message(message.chat.id, 'Здесь вы можете ознакомится с нашим сайтом, почитать дайджесты и про нас', reply_markup=keyboard)
    elif message.text =='Контакты':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_call = telebot.types.InlineKeyboardButton('Контакты', callback_data='pressed_call')
        keyboard.add(button_call)
        bot.send_message(message.chat.id, 'По вопросам обращасться', reply_markup=keyboard)
    elif message.text == 'Курсы':
        # Создаем панельку под сообщением
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton('URL', url='ProfiBoard.com')
        keyboard.add(url_button)
        bot.send_message(message.chat.id, 'Наши курсы', reply_markup=keyboard)




#активация бота
while True:
    try:
        bot.polling()
    except BaseException as error:
        print(error.__class__)
#cnx.close()
