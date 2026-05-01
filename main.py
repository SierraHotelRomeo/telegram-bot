import os
from telethon import TelegramClient
from telethon.sessions import StringSession

API_ID = int(os.environ["31153420"])
API_HASH = os.environ["0edc0b36cee78e68fa4c78d092b51276"]
SESSION_STRING = os.environ.get("SESSION_STRING", "")

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

async def main():
    print("Telegram client started")

    async for dialog in client.iter_dialogs():
        print(dialog.name)

with client:
    client.loop.run_until_complete(main())
