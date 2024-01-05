import os

from dotenv import load_dotenv

from sources import *


load_dotenv()


API_ID = os.environ["API_ID"]
API_HASH = os.environ["API_HASH"]
TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHANNEL_NAME = os.environ["TELEGRAM_CHANNEL_NAME"]
SYSTEM_VERSION = os.environ["SYSTEM_VERSION"]
DB_FILE = os.environ["DB_FILE"]
ADMIN_ID = os.environ["ADMIN_ID"]