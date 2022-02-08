import webbrowser
import os
import time
from pynput.keyboard import Key, Controller
import requests
from bs4 import BeautifulSoup

keyboard = Controller()  # Create the controller


url = 'https://www.google.com'

webbrowser.open_new(url)
time.sleep(1)

keyboard.press(Key.ctrl)
keyboard.press('h')
keyboard.release('h')
keyboard.release(Key.ctrl)

html = requests.get(url).content
soup = BeautifulSoup(html)
#title = soup.select('#visit-title')[0].text
title = soup.find_all('visit-url')
print(title)