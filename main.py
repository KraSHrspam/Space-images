import requests
import os
import telegram
import logging
from time import sleep
from dotenv import dotenv_values
from urllib.parse import urlparse
from datetime import datetime


def get_apod_pictures(api_key):
    payload = {"api_key": f"{api_key}",
               "count": "50"}
    apod_link = "https://api.nasa.gov/planetary/apod"
    picture_apod_num = 0
    response = requests.get(apod_link, params=payload)
    response.raise_for_status()
    for picture_apod in response.json():
        picture_apod_num += 1
        picture_download(picture_apod["url"], f"APOD_pictures/Apod{picture_apod_num}")
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
        picture_download(finished_epic_link, f"EPIC_pictures/EPIC{epic_picture_num}", params=payload)


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


def publish_infinite(token):
    bot = telegram.Bot(token=token)
    updates = bot.get_updates()
    while True:
        for address, dirs, files in os.walk("EPIC_pictures"):
            for file in files:
                picture_adress = (f"{address}'/'{file}")
                with open(picture_adress, "rb") as file:
                    photo = file.read()
                bot.send_photo(chat_id="@EPIC_NASA_pictures_group", photo=photo)
                sleep(float(period))

if __name__ == '__main__':
    api_key = dotenv_values(".env")["API_KEY"]
    period = dotenv_values(".env")["PERIOD"]
    token = dotenv_values(".env")["TOKEN"]
    chat_id = dotenv_values(".env")["CHAT_ID"]

    try:
        get_apod_pictures(api_key)
    except requests.exceptions.HTTPError as error:
        logging_error("Can't get data from server:\n{0}".format(error))

    try:
        get_epic_picture(api_key)
    except requests.exceptions.HTTPError as error:
        logging_error("Can't get data from server:\n{0}".format(error))

    try:
        fetch_spacex_last_launch()
    except requests.exceptions.HTTPError as error:
        logging_error("Can't get data from server:\n{0}".format(error))

    publish_infinite(token)
