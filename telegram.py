import requests
import json

TOKEN = "6229224424:AAHcXshLpKyrM9rOJLWRLJURKt5ZxLDh0gw"
chat_id_okko = "1168008459"
chat_id_nea = "1244624626"
# chat_id_pekka = "5841092259"

# Takes a messages as a parameter and sends it to corresponding chat ids

def sendTelegram(message):
  url1 = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id_okko}&text={message}"
  #url2 = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id_nea}&text={message}"
  requests.get(url1).json()
  #requests.get(url2).json()