from dotenv import load_dotenv
import os
import requests
import re


app_root = os.path.join(os.path.dirname(__file__), '.')
env_path = os.path.join(app_root, '.env')
load_dotenv(env_path, verbose=True, override=True)

BOT_TOKEN = os.getenv('BOT_TOKEN')
PROJECT_NAME = os.getenv('PROJECT_NAME')
PORT = os.getenv('PORT')
PIXABAY_KEY = os.getenv('PIXABAY_KEY')
PIXABAY_URL = os.getenv('PIXABAY_URL')
PIXABAY_PAGES = os.getenv('PIXABAY_PAGES')
PIXABAY_PER_PAGE = os.getenv('PIXABAY_PER_PAGE')


def request_image(keyword: str):
    """Get the response from https://pixabay.com/api/ follow keyword"""
    payload = {
        "key": PIXABAY_KEY,
        "q": keyword,
        "page": PIXABAY_PAGES,
        "per_page": PIXABAY_PER_PAGE
    }
    return requests.get(PIXABAY_URL, params=payload)


def filter_images(photos):
    """Filter photos extension allowed"""
    # photos is a list of photo urls get from requests
    pattern = r'([^.]*)$'
    allowed_extensions = ['jpg', 'jpeg', 'png', 'gif']
    file_extension = ''
    for photo in photos:
        while file_extension not in allowed_extensions:
            file_extension = re.search(pattern, photo).group(1).lower()
    return photos
