import os
from dotenv import load_dotenv

load_dotenv()


APP_NAME = os.getenv("APP_NAME")
APP_VERSION = os.getenv("APP_VERSION")
WINDOW_WIDTH = int (os.getenv("WINDOW_WIDTH"))
WINDOW_HEIGHT = int (os.getenv("WINDOW_HEIGHT"))