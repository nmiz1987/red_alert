import json
import urllib.request
import bs4 as bs4

import requests

import time

import os

from os import environ

url = 'https://www.oref.org.il/WarningMessages/History/AlertsHistory.json'
try:

    while True:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode("utf-8"))
        
        print(soup)
        time.sleep(10)

finally:

    pass
