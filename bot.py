import os
import requests
import time

TOKEN = os.getenv("BOT_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}"

last_update_id = None

def send_message(chat_id, text):
    requests.post(f"{URL}/sendMessage", json={
        "chat_id": chat_id,
        "text": text
    })

print("Bot started...")

while True:
    try:
        r = requests.get(f"{URL}/getUpdates").json()

        if r["result"]:
            for update in r["result"]:
                update_id = update["update_id"]

                if last_update_id is None or update_id > last_update_id:
                    last_update_id = update_id

                    if "message" in update:
                        chat_id = update["message"]["chat"]["id"]
                        text = update["message"]["text"]

                        print("Message:", text)

                        send_message(chat_id, "🔥 NIFTY BOT IS LIVE 🔥")

    except Exception as e:
        print("Error:", e)

    time.sleep(2)
