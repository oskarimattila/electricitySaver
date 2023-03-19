import json
import urllib.request

url = "https://api.porssisahko.net/v1/latest-prices.jsons"
data = urllib.request.urlopen(url)
json_data = json.load(data)
print(json_data)