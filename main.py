import urllib.request
import json
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

requests.get(base + "server start running...")

try:
    while True:
        page = urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
        infile = urllib.request.urlopen(page).read()
        data = infile.decode("utf-8") # Read the content as string decoded with ISO-8859-1
        
        #response = urllib.request.urlopen(url);
        #data = json.loads(response.read().decode("utf-8"))
        # only my zone
        for i in data[:40]:
            if i.get('data') in loc: # if in my zone
                if i not in last_alert: # if new alert
                    last_alert.pop(0) # pop from the list
                    last_alert.append(i) # add to the list
                    if first_run == False:
                        msg_time = i.get('alertDate')[11:]
                        info = "צבע אדום!\nשעה " + msg_time + ':\t מיקום:' + str(i.get('data')).lstrip()
                        requests.get(base + info)
                        print('@' * 40)

        print('-' * 40)
        # all zones
        for i in data[:1]:
            if first_run == False:
                msg_time = i.get('alertDate')[11:]
                info_msg = "צבע אדום!\nשעה " + msg_time + ':\t מיקום:' + str(i.get('data')).lstrip()
                requests.get(base + info_msg)
                info = i.get('alertDate') +'\t'+ i.get('data')
                # requests.get(base + info)
                print(info)
        first_run = False
        time.sleep(5)
        screen_clear()
finally:
    pass