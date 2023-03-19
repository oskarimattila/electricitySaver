import requests
import json
from datetime import datetime


def getAllPrices():
  url = "https://api.porssisahko.net/v1/latest-prices.json"

  res = requests.get(url)

  prices = open("allPrices.json", "w")
  json_object = json.dumps(res.json(), indent=2)
  prices.write(json_object)
  prices.close()
  f = open("allPrices.json", "r")
  values = json.load(f)
  f.close()
  return values["prices"]

def getCurrentPrice():
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

print(getAllPrices())