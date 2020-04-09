from flask import Flask, request, abort
import telebot
from bot import bot
from utils import PORT


app = Flask(__name__)
WEBHOOK_URL = f"/{bot.token}"


# Webserver webhook route
@app.route('/WEBHOOK_URL', methods=['GET'])
def webhook():
    """Check if the verify token is correct"""
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return 'OK', 200
    return abort(403)


if __name__ == '__main__':
    app.run(port=PORT, debug=True)
