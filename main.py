import requests
import io
import os
import telegram
from pprint import pprint
from telegram import Update
from dotenv import load_dotenv
from urllib.parse import urlparse
from telegram.ext import Updater, CommandHandler, CallbackContext

link = "https://api.spacexdata.com/v3/launches"
apod_link = "https://api.nasa.gov/planetary/apod?count=50&api_key=YjSmH3pN6d3J7YGlSmNN1NdlYnXnHvmak9DpbLbV"
epic_link = "https://api.nasa.gov/EPIC/api/natural/images?api_key=YjSmH3pN6d3J7YGlSmNN1NdlYnXnHvmak9DpbLbV"

load_dotenv()
token = os.getenv('TOKEN')

def get_apod(apod_link):
    apod_picture_num = 0
    response = requests.get(apod_link)
    response.raise_for_status()
    for apod_picture in response.json():
        apod_picture_num += 1
        try:
            picture_download(apod_picture["url"], f"APOD_pictures/Apod{apod_picture_num}")
        except:
            print("Ошибка,Ошибка!")

#t.me/EPIC_NASA_pictures_bot
#5136479351:AAG7H078n17prSyg0gZNS64sL2svFJxF2UE

def get_epic_pictures(epic_link):
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

def get_spacex_pictures():
    link = "https://api.spacexdata.com/v3/launches"
    response = requests.get(link)
    response.raise_for_status()
    return response.json()[66]["links"]["flickr_images"]

def fetch_spacex_last_launch():
    picture_num = 0
    pictures_of_rocket = get_spacex_pictures()
    for url in pictures_of_rocket:
        picture_num += 1
        picture_download(url, f"SpaceX_pictures/SpaceX{picture_num}")

bot = telegram.Bot(token=token)
updates = bot.get_updates()
bot.send_message(text='Hi Mark!', chat_id="@EPIC_NASA_pictures_group")

#get_epic_pictures(epic_link)
