import requests
import json
import time
from datetime import datetime

def getPrice():
  today = datetime.now()

  url = "https://api.porssisahko.net/v1/price.json?date={}&hour={}".format(today.date(), today.hour)
  res = requests.get(url)
  print("\n{} klo {}".format(today.date(), today.hour))

  
  prices = open("prices.json", "w")
  json_object = json.dumps(res.json(), indent=2)
  prices.write(json_object)
  prices.close()
  f = open("prices.json", "r")
  values = json.load(f)
  f.close()
  return values["price"]

# Telegram bot
TOKEN = "6229224424:AAHcXshLpKyrM9rOJLWRLJURKt5ZxLDh0gw"
chat_id_okko = "1168008459"
chat_id_pekka = "5841092259"

while True:
  message = "\nElectricity price right now ----- {} snt/kWh\n".format(getPrice())
  url1 = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id_okko}&text={message}"
  url2 = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id_pekka}&text={message}"
  requests.get(url1).json()
  requests.get(url2).json()
  print(message)
  time.sleep(3600)


