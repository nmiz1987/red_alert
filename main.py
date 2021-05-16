import json

import bs4 as bs4

import requests

import time

import os

from os import environ


url = 'https://www.google.com'
url2 = 'https://www.oref.org.il/WarningMessages/History/AlertsHistory.json'
try:

    while True:
        r = requests.get(url)
        soup = bs4.BeautifulSoup(r.content, "html.parser").decode("utf-8")
        print(soup)
        time.sleep(5)

finally:

    pass
