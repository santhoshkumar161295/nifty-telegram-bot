import requests
import os
from flask import Flask, request

TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

app = Flask(__name__)

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, data=payload)

@app.route("/")
def home():
    return "Nifty Bot Running"

@app.route("/alert", methods=["POST"])
def alert():
    data = request.json
    message = data.get("message", "Test alert")
    send_telegram_message(message)
    return {"status": "sent"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
