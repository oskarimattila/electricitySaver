import requests
import json
from datetime import datetime
from lights import turnOn, changeLight
from telegram import sendTelegram
import daytime

# These are the IP adddresses of the wiz lights
light_ip_pekka = "192.168.100.45"
light_ip_okko = "192.168.1.240"
# Predefined colours for indicating different colors. These rgb values will be injected 
# to the lights via UDP byte stream
green = {
  "r": 100,
  "g": 255,
  "b": 20,
  "dimming": 100
}
red = {
  "r": 255,
  "g": 0,
  "b": 0,
  "dimming":100
}
yellow = {
  "r": 99,
  "g": 66,
  "b": 23,
  "dimming": 100
}

# This function retrieves the current price for electricity for the hour
def getPrice():
  today = datetime.now()

  url = "https://api.porssisahko.net/v1/price.json?date={}&hour={}".format(today.date(), today.hour)
  res = requests.get(url)

  prices = open("prices.json", "w")
  json_object = json.dumps(res.json(), indent=2)
  prices.write(json_object)
  prices.close()
  f = open("prices.json", "r")
  values = json.load(f)
  f.close()
  return values["price"]

midPrice = 8
highPrice = 11.65
message = "\nElectricity price right now ----- {} snt/kWh\n"

# The point is to repeat this loop every hour
# Our ceiling value is 11 snt/kWh compare the current value every hour to our ceiling value
# First check if we are in the operation time 08-18
now = datetime.now()
hour = now.hour
currentPrice = getPrice()
if hour >= 7 and hour <= 22:
  turnOn(True, light_ip_okko)
  if currentPrice > highPrice:
    changeLight(red, light_ip_okko)
    sendTelegram(f"\nElectricity price is expensive right now ----- {currentPrice} snt/kWh\n")
  elif currentPrice >= midPrice and currentPrice <= highPrice:
    changeLight(yellow, light_ip_okko)
    sendTelegram(message.format(currentPrice))
  else:
    changeLight(green, light_ip_okko)
    sendTelegram(message.format(currentPrice))

else: 
  turnOn(False, light_ip_okko)

