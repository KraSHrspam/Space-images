import requests
import os
from urllib.parse import urlparse

def get_image_extension(picture_link):
    parse_url = urlparse(picture_link)
    parse_url_path = parse_url.path
    extension_of_url = os.path.splitext(parse_url_path)
    return extension_of_url[1]

def picture_download(link, picture_name, params=""):
    response = requests.get(link, params=params)
    response.raise_for_status()
    with open(picture_name + get_image_extension(link), 'wb') as file:
        file.write(response.content)

def get_spacex_picture_url():
    link = "https://api.spacexdata.com/v3/launches"
    launch_number = os.getenv("SPACEX_LAUNCH_NUMBER")
    response = requests.get(link)
    response.raise_for_status()
    return response.json()[launch_number]["links"]["flickr_images"]


def fetch_spacex_last_launch():
    pictures_of_rocket = get_spacex_picture_url()
    for picture_num, picture in enumerate(pictures_of_rocket):
        picture_download(picture, f"SpaceX_pictures/SpaceX{picture_num}")