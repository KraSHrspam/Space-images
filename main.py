import os
import requests
from time import sleep

import telegram
from dotenv import dotenv_values
EPIC_path="EPIC_pictures"


def publish_infinite(token):
    bot = telegram.Bot(token=token)
    while True:
        for address, dirs, files in os.walk(f"{EPIC_path}"):
            for file in files:
                picture_address = os.path.join(addres, file)
                with open(picture_address, "rb") as file:
                    bot.send_photo(chat_id=f"{CHAT_ID}", photo=file.read)
                sleep(float(period))


if __name__ == '__main__':
    api_key = dotenv_values(".env")["NASA_IMPLICIT_FLOW_TOKEN"]
    period = dotenv_values(".env")["PERIOD"]
    token = dotenv_values(".env")["TELEGRAM_TOKEN"]
    chat_id = dotenv_values(".env")["TELEGRAM_CHAT_ID"]