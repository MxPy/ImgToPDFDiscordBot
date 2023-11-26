import discord
import responses
import os
from dotenv import load_dotenv


class Bot:
    def __init__(self):
        self.isParsing = False
    async def send_message(self, message, id, user_message, channel):
        response = responses.handle_respons(id, user_message)
        try:
            await message.channel.send(response)

        except Exception as e:
            print(e)
            
    async def directly_send_message(self, message, text):
        try:
            await message.channel.send(text)
        except Exception as e:
            print(e)
            
    def run_discord_bot(self):
        load_dotenv()
        TOKEN = os.getenv("BOT_TOKEN")
        intents = discord.Intents.default()
        intents.message_content = True 
        intents.members = True
        client = discord.Client(intents=intents)
        
        
        
        @client.event
        async def on_ready():
            print(f'{client.user} is now running')
            
        @client.event
        async def on_message(message):
            if message.author == client.user:
                return 
            
            user_id = str(message.author.id)
            username = str(message.author)
            user_message = str(message.content)
            channel = str(message.channel)
            if message.attachments:
                if message.attachments[0].filename.endswith(".jpg") or message.attachments[0].filename.endswith(".jpeg") or message.attachments[0].filename.endswith(".png"):
                    img_url = str(message.attachments[0])
            
            
            print(f"{username} said '{user_message}' on channel '{channel}'")
            
            if channel == 'boty':
                if user_message == '??start' and self.isParsing == False:
                    self.isParsing = True
                    await self.directly_send_message(message, "Start Parsing")
                elif(self.isParsing == True):
                    await self.directly_send_message(message, "noted")
                else:
                    await self.send_message(message, user_id, user_message, channel)
            
        client.run(TOKEN)