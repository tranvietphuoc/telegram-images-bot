from app import app
from utils import PORT


if __name__ == '__main__':
    app.run(port=PORT, debug=True)