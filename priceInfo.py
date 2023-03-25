import requests
import json
from datetime import datetime

# Retrieves price data for the next 24h (there is data for 48h but the other 24h is past prices) and stores them in a file. 
# Returns an array of dictionary objects containing the data in following format: 
# [{'price': 2.093, 'startDate': '2023-03-26T21:00:00.000Z', 'endDate': '2023-03-26T22:00:00.000Z'}, ...]
# This will be useful tool to determine the cheapest hours within the next 24h

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

# This function retrieves the current price for electricity for the hour
def getPrice():
  # Get the current date and time
  today = datetime.now()

  url = "https://api.porssisahko.net/v1/price.json?date={}&hour={}".format(today.date(), today.hour)
  # Request data from the api, returns a response object. We need to extract the raw json content and
  # convert it to python dictionary to extract the price value.
  res = requests.get(url)
  price = json.loads(res.content)["price"]
  return price

#print(getAllPrices())