import os
import requests

from tools import picture_download


def get_spacex_picture_url():
    link = "https://api.spacexdata.com/v3/launches"
    launch_number = os.getenv("SPACEX_LAUNCH_NUMBER")
    response = requests.get(link)
    response.raise_for_status()
    return response.json()[launch_number]["links"]["flickr_images"]


def fetch_spacex_last_launch():
    pictures_of_rocket = get_spacex_picture_url()
    for picture_num, picture in enumerate(pictures_of_rocket):
        picture_name = f"SpaceX{picture_num}"
        picture_download(picture, os.path.join())

if __name__ == '__main__':
    launch_number = os.getenv["SPACEX_LAUNCH_NUMBER"]
    picture_dir = "SpaceX_pictures"
    os.makedirs(picture_dir, exist_ok=True)
