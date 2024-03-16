from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
import logging
import dotenv
import os


dotenv.load_dotenv('./.env')

logging.basicConfig(level=logging.INFO)
bot = Bot(os.environ["BOT_TOKEN"], parse_mode=ParseMode.HTML)
dp = Dispatcher()
