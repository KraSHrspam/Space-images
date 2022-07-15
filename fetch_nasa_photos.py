import logging
import requests
from datetime import datetime

from dotenv import dotenv_values

from tools import picture_download
COUNT=50
EPIC_path="EPIC_pictures"
APOD_path="APOD_pictures"


def get_apod_pictures(api_key):
    payload = {"api_key": f"{api_key}",
               "count": {COUNT}}
    apod_link = "https://api.nasa.gov/planetary/apod"
    response = requests.get(apod_link, params=payload)
    response.raise_for_status()
    for apod_picture_num, picture_apod in enumerate(response.json()):
        picture_download(picture_apod["url"], f"{APOD_path}/Apod{apod_picture_num}")
        print(f"#Загружаю Апод фотку номер {apod_picture_num}")


def get_epic_pictures(api_key):
    payload = {"api_key": f"{api_key}"}
    epic_link = "https://api.nasa.gov/EPIC/api/natural/images"
    response = requests.get(epic_link, params=payload)
    response.raise_for_status()
    for epic_picture_num, epic_picture in enumerate(response.json()):
        date = epic_picture["date"]
        parsed_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        date_with_slash = parsed_date.strftime("%Y/%m/%d")
        finished_epic_link = f"https://api.nasa.gov/EPIC/archive/natural/{date_with_slash}/png/{epic_picture['image']}.png"
        picture_download(finished_epic_link, f"{EPIC_path}/EPIC{epic_picture_num}", params=payload)
        print(f"#Загружаю Эпик фотку номер {epic_picture_num}")


if __name__ == '__main__':
    api_key = dotenv_values(".env")["API_KEY"]
    chat_id = dotenv_values(".env")["CHAT_ID"]

try:
        get_apod_pictures(api_key)
except requests.exceptions.HTTPError as error:
        logging.error("Can't get data from server:\n{0}".format(error))

try:
        get_epic_pictures(api_key)
except requests.exceptions.HTTPError as error:
        logging.error("Can't get data from server:\n{0}".format(error))
