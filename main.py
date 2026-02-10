import requests
import time
import os
from flask import Flask

app = Flask(__name__)

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

UPPER_BREAK = 26000
LOWER_BREAK = 25870

alert_sent_up = False
alert_sent_down = False


def get_nifty_price():
    url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=%5ENSEI"
    data = requests.get(url).json()
    price = data['quoteResponse']['result'][0]['regularMarketPrice']
    return price


def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})


@app.route('/')
def run_bot():
    global alert_sent_up, alert_sent_down

    price = get_nifty_price()

    if price > UPPER_BREAK and not alert_sent_up:
        send_telegram(f"🚀 NIFTY BREAKOUT UP\nPrice: {price}")
        alert_sent_up = True
        alert_sent_down = False

    if price < LOWER_BREAK and not alert_sent_down:
        send_telegram(f"🔻 NIFTY BREAKDOWN\nPrice: {price}")
        alert_sent_down = True
        alert_sent_up = False

    return "Bot Running"


if __name__ == "__main__":
    while True:
        try:
            requests.get("https://niftybot.onrender.com")
            time.sleep(60)
        except:
            pass
