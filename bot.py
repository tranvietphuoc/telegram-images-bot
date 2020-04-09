import telebot
import requests
from utils import BOT_TOKEN, PROJECT_NAME


bot = telebot.TeleBot(BOT_TOKEN, threaded=True)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi there, welcome to my bot!")


@bot.message_handler(commands=['4k'])
def send_random_4k_photo(message):
    response = requests.get('https://source.unsplash.com/random/4096x2160')
    bot.send_photo(message.chat_id, response.content)
    bot.send_document(message.chat_id, response.content,
                      caption='rename_to_jpeg')



# configure webhook for the bot, with the url of the Glitch project
bot.set_webhook(f"https://{PROJECT_NAME}.glitch.me/{BOT_TOKEN}")
bot.polling()
