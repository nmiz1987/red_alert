import urllib.request
import json
import time
import os


# The screen clear function
def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')


last_alert = []

loc = ['גיאה', 'בית שקמה', 'תלמי יפה', 'בת הדר']
url = 'https://www.oref.org.il/WarningMessages/History/AlertsHistory.json'

while True:
    response = urllib.request.urlopen(url);
    data = json.loads(response.read().decode("utf-8"))
    for i in data[:20]:
        if i.get('data') in loc:
            print(i.get('alertDate') + '\t' + i.get('data'))
            if i.get('alertDate') not in last_alert:
                last_alert.append(i.get('alertDate'))
                print('@' * 40)

    print('-' * 40)
    print("All alerts:")
    for i in data[:11]:
        print(i.get('alertDate') + '\t' + i.get('data'))
    time.sleep(60)
    screen_clear()