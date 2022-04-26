import requests
import os
import telegram
from time import sleep
from dotenv import dotenv_values
from urllib.parse import urlparse

def get_apod(apod_link, api_key):
    apod_link = f"https://api.nasa.gov/planetary/apod?count=50&api_key={api_key}"
    apod_picture_num = 0
    response = requests.get(apod_link)
    response.raise_for_status()
    for apod_picture in response.json():
        apod_picture_num += 1
        try:
            picture_download(apod_picture["url"], f"APOD_pictures/Apod{apod_picture_num}")
        except:
            print("Ошибка,Ошибка!")


def get_epic_picture(epic_link, api_key):
    epic_link = f"https://api.nasa.gov/EPIC/api/natural/images?api_key={api_key}"
    epic_picture_num = 0
    response = requests.get(epic_link)
    response.raise_for_status()
    for epic_picture in response.json():
        epic_picture_num += 1
        pic_name = epic_picture['image']
        year = pic_name[8:12]
        month = pic_name[12:14]
        day = pic_name[14:16]
        finished_epic_link = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{epic_picture['image']}.png?api_key=YjSmH3pN6d3J7YGlSmNN1NdlYnXnHvmak9DpbLbV"
        print(finished_epic_link)
        try:
            picture_download(finished_epic_link, f"EPIC_pictures/EPIC{epic_picture_num}")
        except:
            print("ЭПИЧЕСКАЯ ОШИБКА!")


def get_image_extansion(picture_link):
    parse_url = urlparse(picture_link)
    finished_parse_url = parse_url.path
    extension_of_url = os.path.splitext(finished_parse_url)
    return extension_of_url[1]


def picture_download(link, picture_name):
    response = requests.get(link)
    response.raise_for_status()
    with open(picture_name + get_image_extansion(link), 'wb') as file:
        file.write(response.content)


def get_spacex_picture_url():
    link = "https://api.spacexdata.com/v3/launches"
    response = requests.get(link)
    response.raise_for_status()
    return response.json()[66]["links"]["flickr_images"]


def fetch_spacex_last_launch():
    picture_num = 0
    pictures_of_rocket = get_spacex_picture_url()
    for url in pictures_of_rocket:
        picture_num += 1
        picture_download(url, f"SpaceX_pictures/SpaceX{picture_num}")


def publish_infinite(token):
    bot = telegram.Bot(token=token)
    updates = bot.get_updates()
    while True:
        for address, dirs, files in os.walk("EPIC_pictures"):
            for file in files:
                picture_adress = address+'/'+file
                print (picture_adress)
                with open(picture_adress, "rb") as file:
                    photo = file.read()
                bot.send_photo(chat_id="@EPIC_NASA_pictures_group", photo=photo)
                sleep(float(period))

if __name__ == '__main__':
    api_key = dotenv_values(".env")["API_KEY"]
    period = dotenv_values(".env")["PERIOD"]
    token = dotenv_values(".env")["TOKEN"]
    chat_id = dotenv_values(".env")["CHAT_ID"]

    publish_infinite(token)