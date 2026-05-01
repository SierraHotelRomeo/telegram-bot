import os
from telethon import TelegramClient
from telethon.sessions import StringSession

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
SESSION_STRING = os.environ["SESSION_STRING"]

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

async def main():
    print("Telegram client started")

    async for dialog in client.iter_dialogs():
        print(dialog.name)

with client:
    client.loop.run_until_complete(main())
