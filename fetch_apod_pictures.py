import logging
import os
import requests
from datetime import datetime

from dotenv import dotenv_values

from tools import picture_download
APOD_file_path="APOD_pictures"
COUNT=50


def get_apod_pictures(api_key):
    payload = {"api_key": f"{api_key}",
               "count": {COUNT}}
    apod_link = "https://api.nasa.gov/planetary/apod"
    response = requests.get(apod_link, params=payload)
    response.raise_for_status()
    for apod_picture_num, picture_apod in enumerate(response.json()):
        picture_download(picture_apod["url"], os.path.join(APOD_file_path, f"{apod_picture_num}"))
        print(f"#Загружаю Апод фотку номер {apod_picture_num}")


if __name__ == '__main__':
    api_key = dotenv_values(".env")["NASA_IMPLICIT_FLOW_TOKEN"]
    os.makedirs("APOD_pictures")


try:
    get_apod_pictures(api_key)
except requests.exceptions.HTTPError as error:
    logging.error("Can't get data from server:\n{0}".format(error))