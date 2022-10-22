import os
import requests
from time import sleep

import telegram
from dotenv import dotenv_values
EPIC_path="EPIC_pictures"
period = "14400"


def publish_infinite(token, chat_id):
    bot = telegram.Bot(token=token)
    while True:
        for address, dirs, files in os.walk(f"{EPIC_path}"):
            for file in files:
                picture_address = os.path.join(address, file)
                with open(picture_address, "rb") as file:
                    bot.send_photo(chat_id, photo=file.read())
                sleep(float(period))


if __name__ == '__main__':
    token = dotenv_values(".env")["TELEGRAM_TOKEN"]
    chat_id = dotenv_values(".env")["TELEGRAM_CHAT_ID"]
    publish_infinite(token, chat_id)