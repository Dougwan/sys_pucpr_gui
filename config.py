import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()


APP_NAME = os.getenv("APP_NAME", "SYS_PUCPR_GUI")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
APP_ROOT_DIR = Path(__file__).resolve().parent

# GEOMETRY
WINDOW_WIDTH = int(os.getenv("WINDOW_WIDTH", 800))
WINDOW_HEIGHT = int(os.getenv("WINDOW_HEIGHT", 600))

# STYLE
PRIMARY_COLOR = os.getenv("PRIMARY_COLOR", "#8A0538")
PRIMARY_COLOR_DARKER = os.getenv("PRIMARY_COLOR_DARKER", "#5A0728")

LIGHT_COLOR = os.getenv("LIGHT_COLOR", "#F8F9FA")

# FILES PATH
FONTS_PATH = APP_ROOT_DIR / "application" / "assets" / "fonts"

# IMAGES
IMAGES_PATH = APP_ROOT_DIR / "application" / "assets" / "images"

# ENABLED FEATURES
ENABLED_FEATURES = {
    "students": {
        "enable": True,
        "actions": {"create": True, "read": True, "update": False, "delete": False},
    },
}

# DATABASe

DATABASE_PATH = APP_ROOT_DIR / "database"
