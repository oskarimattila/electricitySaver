import socket
import json



def changeLight(color, address):

  udpPayload = {
    "id":1,
    "method":"setPilot",
    "params":color
  }

  jsonResult = json.dumps(udpPayload).encode('utf-8')
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

  port = 38899

  sock.sendto(bytes(jsonResult), (address, port))
  sock.sendto(bytes(jsonResult), (address, port))
          
  print(f"{jsonResult}, was sent!")
  sock.close()

def turnOn(state, address):
  udpPayload = {
    "id":1,
    "method":"setState",
    "params":{"state":state}
  }

  jsonResult = json.dumps(udpPayload).encode('utf-8')
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

  port = 38899

  sock.sendto(bytes(jsonResult), (address, port))
  sock.sendto(bytes(jsonResult), (address, port))
          
  print(f"{jsonResult}, was sent!")
  sock.close()
