import os
from time import sleep

while True:
    for address, dirs, files in os.walk("EPIC_pictures"):
        for file in files:
            print(address+'/'+file)
            sleep(10)
