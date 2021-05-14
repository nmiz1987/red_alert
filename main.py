import json
import bs4 as bs4
import requests
import time
import os
from os import environ

# The screen clear function
def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')

last_alert = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # 20 slots
first_run = True

loc = ['גיאה', 'בית שקמה', 'תלמי יפה', 'בת הדר']
url = 'https://www.oref.org.il/WarningMessages/History/AlertsHistory.json'
base = environ['key']

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

refresh = 3

requests.get(base + "server start running...")
requests.get(base + f"Refresh interval: {refresh} seconds")
print("Red Alert server start running...")
print(f"Refresh interval: {refresh} seconds")

try:
    while True:
        r = requests.get(url, headers=headers)
        soup = bs4.BeautifulSoup(r.content, "html.parser").decode("utf-8")
        data = json.loads(soup)
        # only my zone
        for i in data[:20]:
            # if i.get('data') in loc: # if in my zone
                if i not in last_alert: # if new alert
                    last_alert.pop(0) # pop from the list
                    last_alert.append(i) # add to the list
                    if first_run == False:
                        msg_time = i.get('alertDate')[11:]
                        info = "צבע אדום!\nשעה " + msg_time + ':\t מיקום:' + str(i.get('data')).lstrip()
                        requests.get(base + info)
        first_run = False
        time.sleep(refresh)
        # screen_clear()
finally:
    pass