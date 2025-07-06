from telethon import TelegramClient, events
import asyncio

api_id = 'YOUR_API_ID'  # از my.telegram.org
api_hash = 'YOUR_API_HASH'
channel = '@YourChannel'

client = TelegramClient('session', api_id, api_hash)

async def main():
    async with client:
        async for message in client.iter_messages(channel, limit=100):
            if message.text and ('vmess://' in message.text or 'vless://' in message.text or 'trojan://' in message.text):
                with open('configs.txt', 'a') as f:
                    f.write(message.text + '\n')

asyncio.run(main())
