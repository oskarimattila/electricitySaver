import socket
import json

# ---- Following code provides functions for manipulating a Wiz smart LED ------- #

# This is the exciting part of this project ;D Rather than opting to buy an expensive
# Philips HUE, that provides a ready made API for controlling the lights, I wanted to see
# if there could be a cheaper option.
#
# Now, following common sense, this light is connected to wifi and you can control the light
# using your phone, so there HAS to be a way to mimic that communication between the phone and the light,
# thus controlling the light via your program.
#
# Turns out, there indeed is a way. I think someone recorded the wifi traffic using wireshark or something
# similar, to find out the precise format of data the light expects to operate.
#
# Luckily someone has figured this out. https://aleksandr.rogozin.us/blog/2021/8/13/hacking-philips-wiz-lights-via-command-line 
# The link above is where I got all the information I needed, credits to Aleksandr Rogozin
#
# The wiz light communicates with the UDP protocol, not TCP. This is convenient, as we don't have to connect to the light,
# we just send datagrams (packets) to the lights IP via WLAN, without any backwards communication. Sure, we can't tell whether
# the light received the packets but it allows the engineering of the bulb to be much simpler.
# The port it listens to is 38899
#

def changeLight(color, address):

# The light expects a JSON formatted object, containing the following info:
#   id -> always "1" I think :D
#   method -> determines what the light will do, and what kind of params it expects
#   params -> a json object, containing data that will alter the lights state, in our case either color change or on/off

  # We create a python dictionary that we convert into JSON
  udpPayload = {
    "id":1,
    "method":"setPilot",
    "params":color
  }

  # Format the payload into json and encode to string format
  jsonString = json.dumps(udpPayload).encode('utf-8')

  # Configure a socket to follow UDP protocol
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

  port = 38899

  # Send datagrams (2 for redundancy). Address is the IP of the light.
  # we encode the jsonString into raw byte stream
  sock.sendto(bytes(jsonString), (address, port))
  sock.sendto(bytes(jsonString), (address, port))
          
  print(f"{jsonString}, was sent!")
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
