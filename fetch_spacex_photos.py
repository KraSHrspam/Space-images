import os
import requests
from dotenv import load_dotenv

from tools import download_pictures


def fetch_spacex_last_launch(launch_id, picture_dir):
    link = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(link)
    response.raise_for_status()
    pictures_of_rocket = response.json()["links"]["flickr"]["original"]
    for picture_number, picture in enumerate(pictures_of_rocket):
        print(f"#Загружаю СпейсИКС фотку номер {picture_number}")
        picture_name = f"SpaceX{picture_number}"
        download_pictures(picture, os.path.join(picture_dir, picture_name))


if __name__ == '__main__':
    load_dotenv()
    launch_id = os.getenv("SPACEX_LAUNCH_ID", "5eb87d46ffd86e000604b388")
    picture_dir = "SpaceX_pictures"
    os.makedirs(picture_dir, exist_ok=True)
    fetch_spacex_last_launch(launch_id, picture_dir)
