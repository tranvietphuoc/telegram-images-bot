import telebot
from utils import BOT_TOKEN, PROJECT_NAME, request_image, filter_images
import time
import random


bot = telebot.TeleBot(BOT_TOKEN, threaded=True)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """When start the bot or /help is typed. It sends a ReplyKeyboardMarkup to user"""
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    teddybtn = telebot.types.KeyboardButton('Teddy')
    dogbtn = telebot.types.KeyboardButton('Dog')
    catbtn = telebot.types.KeyboardButton('Cat')
    markup.add(teddybtn, dogbtn, catbtn)
    bot.reply_to(message, "Hi there, welcome to my bot!")
    bot.send_message(message.chat.id,
                     "Click one button to choose one object that you want to get images",
                     reply_markup=markup)


@bot.message_handler(regexp=r'(Teddy|Dog|Cat)+')
def send_response(message):
    # First, read the chat information
    chat_info = bot.get_chat(message.chat.id)
    print(chat_info)
    # Hide a previously sent ReplyKeyboardMarkup
    # markup = telebot.types.ReplyKeyboardRemove(selective=True)
    # Get a list of photo's urls
    resp = request_image(message.text).json()
    results = resp['hits']
    list_images = []
    for result in results:
      list_images.append(result['largeImageURL'])

    # Filter extensions are allowed
    photos = filter_images(list_images)
    # choose random element from photos list
    choose = random.choice(photos)
    bot.send_photo(message.chat.id, choose)


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)


time.sleep(1)  # to idling
# configure webhook for the bot, with the url of the Glitch project
bot.set_webhook(f"https://{PROJECT_NAME}.glitch.me/{bot.token}")
