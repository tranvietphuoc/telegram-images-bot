import telebot
from utils import BOT_TOKEN, PROJECT_NAME, request_image
import time
import random


bot = telebot.TeleBot(BOT_TOKEN, threaded=True)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    itembtn = telebot.types.KeyboardButton('/teddy')
    markup.add(itembtn)
    bot.reply_to(message, "Hi there, welcome to my bot!")
    bot.send_message(message.chat.id, "Click the button: /teddy bellow", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


@bot.message_handler(commands=['teddy'])
def send_response(message):
    # Hide a previously sent ReplyKeyboardMarkup
    # markup = telebot.types.ReplyKeyboardRemove(selective=True)
    # Get random teddy photo from unsplash
    # response = requests.get('https://source.unsplash.com/')
    resp = request_image(message).json()
    results = resp['results']
    photos = []
    for result in results:
        photos.append(result['urls']['regular'])
    # choose random photo from list of photos
    choice = random.randint(0, len(photos))

    bot.send_message(message.chat.id, photos[choice])


# @bot.message_handler(commands=['4k'])
# def send_random_4k_photo(message):
#     response = requests.get('https://source.unsplash.com/random/4096x2160')
#     bot.send_photo(message.chat.id, response.content)
#     bot.send_document(message.chat.id, response.content,
#                       caption='rename_to_jpeg')


time.sleep(1)
# configure webhook for the bot, with the url of the Glitch project
bot.set_webhook(f"https://{PROJECT_NAME}.glitch.me/{BOT_TOKEN}")
bot.polling()
