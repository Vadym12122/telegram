import requests

API_link = "https://api.telegram.org/bot5191742091:AAGh97F41M0rntw2xFauKeEphqvhGmfDauE"

updates = requests.get(API_link + "/getUpdates?offset=-1").json()

print(updates)

message = updates["result"][0]["message"]

chat_id = message ["from"]["id"]
text = message["text"]

send_message = requests.get(API_link + f"/sendMessage?chat_id={chat_id}&text=Привет, ты написал {text}")

