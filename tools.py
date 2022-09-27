import os
import requests
from urllib.parse import urlparse

def get_image_extension(picture_link):
    parsed_url = urlparse(picture_link)
    parsed_url_path = parsed_url.path
    extension_of_url = os.path.splitext(parsed_url_path)
    return extension_of_url[1]

def picture_download(link, picture_path, params=""):
    response = requests.get(link, params=params)
    response.raise_for_status()
    with open(f"{picture_path}{get_image_extension(link)}", 'wb') as file:
        file.write(response.content)