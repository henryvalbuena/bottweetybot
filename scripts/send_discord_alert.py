import os

import requests
from dotenv import load_dotenv

load_dotenv(".secrets")


def send_alert(msg):
    url = os.environ["DISCORD_WEBHOOK"]
    data = {"content": msg}

    req = requests.post(url, data=data)

    print(req)
