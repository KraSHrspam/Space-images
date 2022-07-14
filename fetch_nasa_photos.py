import requests
import logging
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
    picture_apod_num = 0
    response = requests.get(apod_link, params=payload)
    response.raise_for_status()
    for picture_apod in response.json():
        picture_apod_num += 1
        picture_download(picture_apod["url"], f"{APOD_path}/Apod{picture_apod_num}")
        print("#Загружаю фотку")


def get_epic_pictures(api_key):
    payload = {"api_key": f"{api_key}"}
    epic_link = "https://api.nasa.gov/EPIC/api/natural/images"
    epic_picture_num = 0
    response = requests.get(epic_link, params=payload)
    response.raise_for_status()
    for epic_picture in response.json():
        epic_picture_num += 1
        date = epic_picture["date"]
        parsed_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        date_with_slash = parsed_date.strftime("%Y/%m/%d")
        finished_epic_link = f"https://api.nasa.gov/EPIC/archive/natural/{date_with_slash}/png/{epic_picture['image']}.png"
        picture_download(finished_epic_link, f"{EPIC_path}/EPIC{epic_picture_num}", params=payload)


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
