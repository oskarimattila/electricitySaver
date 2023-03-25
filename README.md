-------- SMARTLIGHT PROJECT FOR CONTROLLING A WIZ SMART LED ACCORDING TO ELECTRICITY PRICE ---------

   This program has three main elements

     1. Retrieve latest price data from https://api.porssisahko.net/
     
     2. "Connect" to a predefined smartlight in the WLAN. More accurately this program just sends RGB values
         in a JSON format, encoded to bytes, using the UDP protocol. Hence, it doesn't really connect to the light.

     3. Send price info to predefined users via Telegram.

To see detailed description how the lights are controlled, refer to the comments in the lights.py file.
