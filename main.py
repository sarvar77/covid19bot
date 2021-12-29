import telebot
import COVID19Py
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)
covid19 = COVID19Py.COVID19()

@bot.message_handler(commands=['start', 'help'])
def greating(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
    all_countries = types.KeyboardButton('Во всем мире')
    uzb = types.KeyboardButton('🇺🇿 Узбекистан')
    rus = types.KeyboardButton('🇷🇺 Россия')
    ukr = types.KeyboardButton('🇺🇦 Украина')
    usa = types.KeyboardButton('🇺🇸 США')

    markup.add(uzb, rus, ukr, usa, all_countries)
    bot.send_message(message.chat.id, f'Добро пожаловать <u>{message.from_user.first_name}!</u>\nВыберите название страны.',
                     reply_markup=markup, parse_mode='html')

@bot.message_handler(content_types=['text'])
def covid_info(message):
    if message.text == '🇺🇿 Узбекистан':
        uz = covid19.getLocationByCountryCode('UZ')
        bot.send_message(message.chat.id, f"<b><u>Население:</u></b> {uz[0]['country_population']}\n"
                                          f"<b><u>Заболевшие:</u></b> {uz[0]['latest']['confirmed']}\n"
                                          f"<b><u>Смерти:</u></b> {uz[0]['latest']['deaths']}\n"
                                          f"<b><u>Выздоровшие:</u></b> {uz[0]['latest']['recovered']}\n"
                                          f"<b><u>Последнее обновление:</u></b> {uz[0]['last_updated']}\n\n"
                                          f"<b>@covidResultRobot</b> - 🦠 Получай инфо о коронавирусе!",
                         parse_mode='html')

    elif message.text == '🇷🇺 Россия':
        ru = covid19.getLocationByCountryCode('RU')
        bot.send_message(message.chat.id, f"<b><u>Население:</u></b> {ru[0]['country_population']}\n"
                                          f"<b><u>Заболевшие:</u></b> {ru[0]['latest']['confirmed']}\n"
                                          f"<b><u>Смерти:</u></b> {ru[0]['latest']['deaths']}\n"
                                          f"<b><u>Выздоровшие:</u></b> {ru[0]['latest']['recovered']}\n"
                                          f"<b><u>Последнее обновление:</u></b> {ru[0]['last_updated']}\n\n"
                                          f"<b>@covidResultRobot</b> - 🦠 Получай инфо о коронавирусе!",
                         parse_mode='html')
    elif message.text == '🇺🇦 Украина':
        ua = covid19.getLocationByCountryCode('UA')
        bot.send_message(message.chat.id, f"<b><u>Население:</u></b> {ua[0]['country_population']}\n"
                                          f"<b><u>Заболевшие:</u></b> {ua[0]['latest']['confirmed']}\n"
                                          f"<b><u>Смерти:</u></b> {ua[0]['latest']['deaths']}\n"
                                          f"<b><u>Выздоровшие:</u></b> {ua[0]['latest']['recovered']}\n"
                                          f"<b><u>Последнее обновление:</u></b> {ua[0]['last_updated']}\n\n"
                                          f"<b>@covidResultRobot</b> - 🦠 Получай инфо о коронавирусе!",
                         parse_mode='html')

    elif message.text == '🇺🇸 США':
        us = covid19.getLocationByCountryCode('US')
        bot.send_message(message.chat.id, f"<b><u>Население:</u></b> {us[0]['country_population']}\n"
                                          f"<b><u>Заболевшие:</u></b> {us[0]['latest']['confirmed']}"
                                          f"\n<b><u>Смерти:</u></b> {us[0]['latest']['deaths']}\n"
                                          f"<b><u>Выздоровшие:</u></b> {us[0]['latest']['recovered']}"
                                          f"\n<b><u>Последнее обновление:</u></b> {us[0]['last_updated']}\n\n"
                                          f"<b>@covidResultRobot</b> - 🦠 Получай инфо о коронавирусе!",
                                parse_mode='html')

    else:
        all_info = covid19.getLatest()
        bot.send_message(message.chat.id, f"<b><u>Заболевшие во всем мире:</u></b> {all_info['confirmed']}\n"
                                          f"<b><u>Смерти во всем мире:</u></b> {all_info['deaths']}\n"
                                          f"<b><u>Выздоровшие во всем мире:</u></b> {all_info['recovered']}\n\n"
                                          f"<b>@covidResultRobot</b> - 🦠 Получай инфо о коронавирусе!",
                                parse_mode='html')


bot.polling(none_stop=True)