from flask import Flask, request
from pixabay import Image



PIXABAY_TOKEN = '15937854-63f680d18ab450ec8bc18c075'


app = Flask(__name__)


@app.route('/webhook')
def verify():
    """Check if the verify token is correct"""
    verify_token = request.args.get('hub.verify_token')
    