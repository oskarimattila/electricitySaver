import requests
TOKEN = "6229224424:AAHcXshLpKyrM9rOJLWRLJURKt5ZxLDh0gw"
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
print(requests.get(url).json())