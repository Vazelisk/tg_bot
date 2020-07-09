import telebot
import conf
import requests
import re
from bs4 import BeautifulSoup
from telebot import types


bot = telebot.TeleBot(conf.TOKEN)

result = requests.get('https://horo.mail.ru/')
html = result.text
soup = BeautifulSoup(html,'html.parser')
posts = []
for post in soup.find_all('a', {'class': 'p-imaged-item p-imaged-item_circle p-imaged-item_rune p-imaged-item_shadow_inner'}):
    #print(post.get_text())
    #print(post.prettify())
    posts.append(str(post))

#достаем линки для каждого знака зодиака
#сделано для каждого знака зодиака отдельно, потому что если что вдруг поменяется на сайте
#всё сразу не рухнет
links = []
for post in posts:
    link = re.search('href="(.+?)"', post)
    link = link.group(1)
    if 'aries' in link:
        aries_link = 'https://horo.mail.ru' + link
        links.append(aries_link)
    if 'taurus' in link:
        taurus_link = 'https://horo.mail.ru' + link
        links.append(taurus_link)
    if 'gemini' in link:
        gemini_link = 'https://horo.mail.ru' + link
        links.append(gemini_link)
    if 'cancer' in link:
        cancer_link = 'https://horo.mail.ru' + link
        links.append(cancer_link)
    if 'leo' in link:
        leo_link = 'https://horo.mail.ru' + link
        links.append(leo_link)
    if 'virgo' in link:
        virgo_link = 'https://horo.mail.ru' + link
        links.append(virgo_link)
    if 'libra' in link:
        libra_link = 'https://horo.mail.ru' + link
        links.append(libra_link)
    if 'scorpio' in link:
        scorpio_link = 'https://horo.mail.ru' + link
        links.append(scorpio_link)
    if 'sagittarius' in link:
        sagittarius_link = 'https://horo.mail.ru' + link
        links.append(sagittarius_link)
    if 'capricorn' in link:
        capricorn_link = 'https://horo.mail.ru' + link
        links.append(capricorn_link)
    if 'aquarius' in link:
        aquarius_link = 'https://horo.mail.ru' + link
        links.append(aquarius_link)
    if 'pisces' in link:
        pisces_link = 'https://horo.mail.ru' + link
        links.append(pisces_link)

def get_prophecy(link):
    result = requests.get(link)
    html = result.text

    soup = BeautifulSoup(html,'html.parser')
    post = soup.find('div', {'class': 'article__item article__item_alignment_left article__item_html'})
    match = post.prettify()
    match = cleaner(match)
    return(match)

def cleaner(match):
    match = re.search('<p>\n(.*)</div>', match, re.DOTALL)
    match = match.group(1)
    match = re.sub(r'[a-z<>"/\=/_\n]', '', match)
    match = re.sub(r'    ', '\n', match)
    match = re.sub(r'  ', '', match)
    return(match)

d = {'aries': [], 'taurus': [], 'gemini': [], 'cancer': [], 'leo': [], 'virgo': [],
     'libra': [], 'scorpio': [], 'sagittarius': [], 'capricorn': [], 'aquarius': [], 'pisces': [],}

for link in links:
    prophecy = get_prophecy(link)
    n = re.search('prediction/([a-z]*)/', link)
    n = n.group(1)
    d[n] = prophecy

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    keyboardmain = types.InlineKeyboardMarkup(row_width=4)
    first_button = types.InlineKeyboardButton(text="Овен", callback_data="first")
    second_button = types.InlineKeyboardButton(text="Телец", callback_data="second")
    third_button = types.InlineKeyboardButton(text="Близнецы", callback_data="third")
    fourth_button = types.InlineKeyboardButton(text="Рак", callback_data="fourth")
    fifth_button = types.InlineKeyboardButton(text="Лев", callback_data="fifth")
    sixth_button = types.InlineKeyboardButton(text="Дева", callback_data="sixth")
    seventh_button = types.InlineKeyboardButton(text="Весы", callback_data="seventh")
    eigth_button = types.InlineKeyboardButton(text="Скорпион", callback_data="eigth")
    ninth_button = types.InlineKeyboardButton(text="Стрелец", callback_data="ninth")
    tenth_button = types.InlineKeyboardButton(text="Козерог", callback_data="tenth")
    eleventh_button = types.InlineKeyboardButton(text="Водолей", callback_data="eleventh")
    twelvth_button = types.InlineKeyboardButton(text="Рыбы", callback_data="twelvth")
    keyboardmain.add(first_button, second_button, third_button, fourth_button, fifth_button,
                     sixth_button, seventh_button, eigth_button, ninth_button, tenth_button,
                     eleventh_button, twelvth_button)
    bot.send_message(message.chat.id, "Здравствуйте! Это бот, который покажет вам актуальный гороскоп",
                     reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == "mainmenu":
        keyboardmain = types.InlineKeyboardMarkup(row_width=4)
        first_button = types.InlineKeyboardButton(text="Овен", callback_data="first")
        second_button = types.InlineKeyboardButton(text="Телец", callback_data="second")
        third_button = types.InlineKeyboardButton(text="Близнецы", callback_data="third")
        fourth_button = types.InlineKeyboardButton(text="Рак", callback_data="fourth")
        fifth_button = types.InlineKeyboardButton(text="Лев", callback_data="fifth")
        sixth_button = types.InlineKeyboardButton(text="Дева", callback_data="sixth")
        seventh_button = types.InlineKeyboardButton(text="Весы", callback_data="seventh")
        eigth_button = types.InlineKeyboardButton(text="Скорпион", callback_data="eigth")
        ninth_button = types.InlineKeyboardButton(text="Стрелец", callback_data="ninth")
        tenth_button = types.InlineKeyboardButton(text="Козерог", callback_data="tenth")
        eleventh_button = types.InlineKeyboardButton(text="Водолей", callback_data="eleventh")
        twelvth_button = types.InlineKeyboardButton(text="Рыбы", callback_data="twelvth")
        keyboardmain.add(first_button, second_button, third_button, fourth_button, fifth_button,
                         sixth_button, seventh_button, eigth_button, ninth_button, tenth_button,
                         eleventh_button, twelvth_button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Вы вернулись в меню",reply_markup=keyboardmain)

    elif call.data == "first":
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="Назад в меню", callback_data="mainmenu")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,
        message_id=call.message.message_id, text=d['aries'], reply_markup=keyboard)

    elif call.data == "second":
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="Назад в меню", callback_data="mainmenu")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,
        message_id=call.message.message_id, text=d['taurus'], reply_markup=keyboard)

    elif call.data == "third":
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="Назад в меню", callback_data="mainmenu")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,
        message_id=call.message.message_id, text=d['gemini'], reply_markup=keyboard)

    elif call.data == "fourth":
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="Назад в меню", callback_data="mainmenu")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,
        message_id=call.message.message_id, text=d['cancer'], reply_markup=keyboard)

    elif call.data == "fifth":
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="Назад в меню", callback_data="mainmenu")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,
        message_id=call.message.message_id, text=d['leo'], reply_markup=keyboard)

    elif call.data == "sixth":
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="Назад в меню", callback_data="mainmenu")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,
        message_id=call.message.message_id, text=d['virgo'], reply_markup=keyboard)

    elif call.data == "seventh":
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="Назад в меню", callback_data="mainmenu")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,
        message_id=call.message.message_id, text=d['libra'], reply_markup=keyboard)

    elif call.data == "eigth":
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="Назад в меню", callback_data="mainmenu")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,
        message_id=call.message.message_id, text=d['scorpio'], reply_markup=keyboard)

    elif call.data == "ninth":
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="Назад в меню", callback_data="mainmenu")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,
        message_id=call.message.message_id, text=d['sagittarius'], reply_markup=keyboard)

    elif call.data == "tenth":
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="Назад в меню", callback_data="mainmenu")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,
        message_id=call.message.message_id, text=d['capricorn'], reply_markup=keyboard)

    elif call.data == "eleventh":
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="Назад в меню", callback_data="mainmenu")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,
        message_id=call.message.message_id, text=d['aquarius'], reply_markup=keyboard)

    elif call.data == "twelvth":
        keyboard = types.InlineKeyboardMarkup()
        backbutton = types.InlineKeyboardButton(text="Назад в меню", callback_data="mainmenu")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,
        message_id=call.message.message_id, text=d['pisces'], reply_markup=keyboard)
    
# этот обработчик реагирует на любое сообщение
@bot.message_handler(func=lambda m: True)
def send_len(message):
    bot.send_message(message.chat.id, 'Напишите /start, чтобы выбрать знак зодиака')


if __name__ == '__main__':
    bot.polling(none_stop=True)