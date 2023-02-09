#!/usr/bin/python3
# main.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_GUILD_ID = os.getenv('DISCORD_GUILD_ID')
SERVER_PATH = "/home/dano/danos-game-servers-discord"
PERMITTED_ROLE = os.getenv('GUILD_PERMITTED_ROLE')
BOT_PREFIX = "!danogs"

class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has Connected!')

    async def on_message(self, message):
        # Disable Messages from the Bot
        if message.author == client.user:
            return

        if f'{BOT_PREFIX} start' in message.content:
            print(f"Got Server Start Command")
            
            # Allow only Authorized Users
            if not self.check_role(message.author, PERMITTED_ROLE):
                print(f"{message.author} unauthorized command attempt.")
                response = f"{message.author}, You are Not authorized to issue Bot Commands."
                await message.channel.send(response)
                return
            
            os.chdir(SERVER_PATH)
            cmd_output = os.popen('docker-compose up -d').read()
            response = f"{message.author}, Server Startup Command sent!\n\n ```\n{cmd_output}\n```"
            await message.channel.send(response)

        if f'{BOT_PREFIX} stop' in message.content:
            print(f"Got Server Stop Command")
            
            # Allow only Authorized Users
            if not self.check_role(message.author, PERMITTED_ROLE):
                print(f"{message.author} unauthorized command attempt.")
                response = f"{message.author}, You are Not authorized to issue Bot Commands."
                await message.channel.send(response)
                return
            
            response = f"{message.author}, Server Stop Command sent! Please Allow a few Minutes..."
            await message.channel.send(response)
            os.chdir(HOME_PATH)
            cmd_output = os.popen('docker-compose down').read()
            response = f"{message.author}, Shutdown Response:\n\n ```\n{cmd_output}\n```"
            await message.channel.send(response)

    ######################
    ### Helper Methods ###
    ######################
    def check_role(self, member: discord.member, role_name: str):
        for role in member.roles:
            if role.name.lower() == role_name.lower():
                print(f"{member} was found to have {role_name} role!")
                return True
            
        # If none of those roles match, return false.
        print(f"{member} does not have {role_name} role!")
        return False

client = CustomClient()
client.run(DISCORD_TOKEN)
