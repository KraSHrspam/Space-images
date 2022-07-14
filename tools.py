from urllib.parse import urlparse
import requests
import os

def get_image_extension(picture_link):
    parse_url = urlparse(picture_link)
    parse_url_path = parse_url.path
    extension_of_url = os.path.splitext(parse_url_path)
    return extension_of_url[1]

def picture_download(link, picture_path, params=""):
    response = requests.get(link, params=params)
    response.raise_for_status()
    with open(picture_path + get_image_extension(link), 'wb') as file:
        file.write(response.content)