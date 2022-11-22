import os
import logging
from time import sleep

import telegram
from dotenv import load_dotenv


def publish_infinite(token, chat_id, period, pictures_dir):
    bot = telegram.Bot(token=token)
    while True:
        for address, dirs, files in os.walk(pictures_dir):
            for file in files:
                try:
                    picture_address = os.path.join(address, file)
                    publish_photo(picture_address, bot, chat_id)
                    sleep(float(period))
                except telegram.error.TelegramError:
                    time.sleep(60)
                    logging.exception("Ошибка телеграмм")


def publish_photo(path, bot, chat_id):
    with open(path, "rb") as file:
        bot.send_photo(chat_id, photo=file.read())


if __name__ == '__main__':
    load_dotenv()
    pictures_dir = os.getenv("PICTURE_DIR", "EPIC_pictures")
    period = int(os.getenv("PERIOD", "14400"))
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    publish_infinite(token, chat_id, period, pictures_dir)
    