import requests
import json
from datetime import datetime
from lights import turnOn, changeLight
from telegram import sendTelegram
from priceInfo import getAllPrices, getPrice
#import daytime

# ------------- SMARTLIGHT PROJECT FOR CNTROLLING LIGHT COLOUR ACCORDING TO ELECTRICITY PRICE -------------- #
#
#   This program has three main elements
#
#     1. Retrieve latest price data from https://api.porssisahko.net/
#     
#     2. "Connect" to a predefined smartlight in the WLAN. More accurately this program just sends RGB values
#         in a JSON format, encoded to bytes, using the UDP protocol. Hence, it doesn't really connect to the light.
#
#     3. Send price info to predefined users via Telegram.
#
#   To see detailed description how the lights are controlled, refer to the comments in the lights.py file.
#

# These are the IP adddresses of the wiz lights 
light_ip_pekka = "192.168.100.45"                   # Not a security risk, as these are local IPs assigned by the router.
light_ip_okko = "192.168.1.240"

# Predefined colours for indicating different colors. These rgb values will be injected 
# to the smartlights via UDP protocol
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

midPrice = 8
highPrice = 11.65
message = "\nElectricity price right now ----- {} snt/kWh\n"

# First check if we are in the operation time 07-22
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

