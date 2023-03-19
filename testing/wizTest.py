import requests
import socket
import sys
import json

testColor = {"r": 255, "g":20, "b":0, "dimming":100}

def changeLight(color):

  udpPayload = {
    "id":1,
    "method":"setPilot",
    "params":color
  }

  jsonResult = json.dumps(udpPayload).encode('utf-8')
  try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  except socket.error as err:
    print(f"Socket error because of {err}")

  port = 38899
  address = "192.168.100.45"

  try:
    sock.sendto(bytes(jsonResult), (address, port))
  except socket.gaierror:
    print("There an error resolving the host")
    sys.exit() 
          
  print(f"{jsonResult}, was sent!")
  sock.close()

changeLight(testColor)