import requests
import os
import telegram
from time import sleep
from dotenv import dotenv_values
EPIC_path="EPIC_pictures"


def publish_infinite(token):
    bot = telegram.Bot(token=token)
    while True:
        for address, dirs, files in os.walk(f"{EPIC_path}"):
            for file in files:
                picture_adress = f"{address}/{file}"
                with open(picture_adress, "rb") as file:
                    photo = file.read()
                bot.send_photo(chat_id=f"{CHAT_ID}", photo=photo)
                sleep(float(period))


if __name__ == '__main__':
    api_key = dotenv_values(".env")["API_KEY"]
    period = dotenv_values(".env")["PERIOD"]
    token = dotenv_values(".env")["TOKEN"]
    chat_id = dotenv_values(".env")["CHAT_ID"]

    publish_infinite(token)
