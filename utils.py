from dotenv import load_dotenv
import os
import requests
from datetime import datetime


app_root = os.path.join(os.path.dirname(__file__), '.')
env_path = os.path.join(app_root, '.env')
load_dotenv(env_path, verbose=True, override=True)

BOT_TOKEN = os.getenv('BOT_TOKEN')
PROJECT_NAME = os.getenv('PROJECT_NAME')
PORT = os.getenv('PORT')
UNSPLASH_SEARCH_PHOTO_API = 'https://api.unsplash.com/search/photos'
UNSPLASH_ACCESS_KEY = os.getenv('UNSPLASH_ACCESS_KEY')
UNSPLASH_SECRET_KEY = os.getenv('UNSPLASH_SECRET_KEY')
UNSPLASH_APP_URI = os.getenv('UNSPLASH_APP_URI')


def request_image(keyword: str):
    """Get the response from api.unsplash.com follow keyword"""
    payload = {
            "query": keyword,
            "page": 8,
            "per_page": 20,
            "client_id": UNSPLASH_ACCESS_KEY
        }
    return requests.get(UNSPLASH_SEARCH_PHOTO_API, params=payload)


# def parse_response(request):
#     resp = request.json()
#     results = resp['results']
#     photos = []
#     for result in results:
#         photos.append(result['urls']['regular'])
#     return photos

def log_to_file(message: str):
    with open(os.path.join(app_root, 'work.log'), 'a') as f:
        f.write(datetime.utcnow().strftime('%d-%b-%Y (%H:%M:%S.%f)'))
        f.write(message)
        f.flush()
