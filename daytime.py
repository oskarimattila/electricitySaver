import urllib.request
import json
from dateutil import parser
from datetime import datetime
import zoneinfo

# Following code fetches sunrise and sunset data from an api
#
# Cool thing about this is that it takes into account the changing timezones in Finland.
# Can be paired with programs that follow sunrise/sunset!

url = "https://api.sunrise-sunset.org/json?lat=60.1753072&lng=24.9210280&formatted=0"
data = urllib.request.urlopen(url)
json_data = json.load(data)
# Get local timezone, changes with kesäpäiväntasaus ;)
hel = datetime.now().astimezone().tzinfo
sunrise = parser.parse(json_data["results"]["sunrise"]).astimezone(hel)
sunset = parser.parse(json_data["results"]["sunset"]).astimezone(hel)
test = parser.parse(json_data["results"]["sunrise"])
print(f"Sun rises at {sunrise.hour}:{sunrise.minute} and sets at {sunset.hour}:{sunset.minute}\n\n")
