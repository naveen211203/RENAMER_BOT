from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "")

APP_ID = int(os.environ.get("APP_ID", "15353622"))

API_HASH = os.environ.get("API_HASH", "dd2993a34a1cf6ff991b64fa12266581")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "renamer",
        bot_token=TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    app.run()
