import os
import logging
import requests
from datetime import datetime

from dotenv import dotenv_values

from tools import download_pictures
EPIC_file_path="EPIC_pictures"


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
        picture_name = f"EPIC{epic_picture_num}"
        download_pictures(finished_epic_link, os.path.join(f"{EPIC_file_path}", picture_name), params=payload)
        print(f"#Загружаю Эпик фотку номер {epic_picture_num}")


if __name__ == '__main__':
    api_key = dotenv_values(".env")["NASA_IMPLICIT_FLOW_TOKEN"]
    os.makedirs("EPIC_pictures", exist_ok=True)

    try:
        get_epic_pictures(api_key)
    except requests.exceptions.HTTPError as error:
        logging.error("Can't get data from server:\n{0}".format(error))
