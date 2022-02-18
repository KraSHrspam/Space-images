import requests
import os
from urllib.parse import urlparse
import io
from pprint import pprint

link = "https://api.spacexdata.com/v3/launches"
apod_link = "https://api.nasa.gov/planetary/apod?api_key=YjSmH3pN6d3J7YGlSmNN1NdlYnXnHvmak9DpbLbV"

def get_apod(apod_link):
    response = requests.get(apod_link)
    response.raise_for_status()
    return response.json()["hdurl"]

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
        picture_download(url, f"SpaceX{picture_num}")

#fetch_spacex_last_launch()
pprint(get_apod(apod_link))
