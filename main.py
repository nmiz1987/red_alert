import urllib.request
import json
import requests
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

url = 'https://www.oref.org.il/WarningMessages/History/AlertsHistory.json'

while True:
	response = urllib.request.urlopen(url);
	data = json.loads(response.read().decode("utf-8"))
	for i in data[:20]:
			info = i.get('alertDate')[11:] +'\t'+ i.get('data')
			print(info)
	time.sleep(10)
	screen_clear() 
