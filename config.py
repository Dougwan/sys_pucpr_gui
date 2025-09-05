import os
from dotenv import load_dotenv

load_dotenv()


APP_NAME = os.getenv("APP_NAME", "SYS_PUCPR_GUI")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
WINDOW_WIDTH = int (os.getenv("WINDOW_WIDTH", 800))
WINDOW_HEIGHT = int (os.getenv("WINDOW_HEIGHT", 600))

MAIN_STYLE = {"background-color": "#F8F9FA", "color": "#8A0538"}