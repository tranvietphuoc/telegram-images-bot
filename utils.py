from dotenv import load_dotenv
import os


app_root = os.path.join(os.path.dirname(__file__), '.')
env_path = os.path.join(app_root, '.env')
load_dotenv(env_path, verbose=True, override=True)

BOT_TOKEN = os.getenv('BOT_TOKEN')
PROJECT_NAME = os.getenv('PROJECT_NAME')
PORT = os.getenv('PORT')
