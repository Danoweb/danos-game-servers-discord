#!/usr/bin/python3
# main.py
import os

import discord
from discord.ext import commands
from discord.ui import View
from dotenv import load_dotenv

from minecraft_bedrock.mc_bedrock import MinecraftBedrock

load_dotenv()
#DISCORD 
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_GUILD_ID = os.getenv('DISCORD_GUILD_ID')
PERMITTED_ROLE = os.getenv('GUILD_PERMITTED_ROLE')
BOT_PREFIX = "!danogs"
FORM_TIMEOUT = 60

#BEDROCK (Minecraft)
BEDROCK_SERVER_PATH = "/opt/minecraft-bedrock"
BEDROCK_DATA_PATH = "/data"

#CREATEMOD (Minecraft)
CREATEMOD_SERVER_PATH = "/opt/minecraft-createmod"

form_responses = {}

#Prepare the Bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has Connected!')
    

@bot.event
async def on_message(message):
    # Disable Messages from the Bot
    if message.author == bot.user:
        return

    # Get the context from the message
    ctx = await bot.get_context(message)

    if message.content.startswith(f'{BOT_PREFIX} help'):
        print(f"Got Help Command")
        
        # Allow only Authorized Users
        if not check_role(message.author, PERMITTED_ROLE):
            print(f"{message.author} unauthorized command attempt.")
            response = f"<@{message.author.id}>, You are Not authorized to issue Bot Commands."
            await message.channel.send(response)
            return
        
        response = f"<@{message.author.id}> These are the available commands:\n `start minecraft-bedrock` - Starts the Server \n `stop minecraft-bedrock` - Stops the Server \n `start minecraft-createmod` - Starts the Server \n `stop minecraft-createmod` - Stops the Server \n `minecraft-bedrock allowlist add` - Adds a User to the Minecraft Bedrock Server list \n `minecraft-bedrock allowlist list` - Shows the current Allowlist users list \n `minecraft-bedrock allowlist remove` - Removes a User from the Allowlist "
        await message.channel.send(response)

    # Minecraft CreateMod Server
    if message.content.startswith(f'{BOT_PREFIX} start minecraft-createmod'):
        print(f"Got Server Start Command")
        
        # Allow only Authorized Users
        if not check_role(message.author, PERMITTED_ROLE):
            print(f"{message.author} unauthorized command attempt.")
            response = f"<@{message.author.id}>, You are Not authorized to issue Bot Commands."
            await message.channel.send(response)
            return
        
        os.chdir(CREATEMOD_SERVER_PATH)
        cmd_output = os.popen('docker-compose up -d').read()
        response = f"<@{message.author.id}>, Server Startup Command sent!\n\n ```\n{cmd_output}\n```"
        await message.channel.send(response)

    if message.content.startswith(f'{BOT_PREFIX} stop minecraft-createmod'):
        print(f"Got Server Stop Command")
        
        # Allow only Authorized Users
        if not check_role(message.author, PERMITTED_ROLE):
            print(f"{message.author} unauthorized command attempt.")
            response = f"<@{message.author.id}>, You are Not authorized to issue Bot Commands."
            await message.channel.send(response)
            return
        
        response = f"{message.author}, Server Stop Command sent! Please Allow a few Minutes..."
        await message.channel.send(response)
        os.chdir(CREATEMOD_SERVER_PATH)
        cmd_output = os.popen('docker-compose down').read()
        response = f"<@{message.author.id}>, Shutdown Command Sent, Response:\n\n ```\n{cmd_output}\n```"
        await message.channel.send(response)

    #Minecraft Bedrock Commands
    if message.content.startswith(f'{BOT_PREFIX} start minecraft-bedrock'):
        print(f"Got Server Start Command")
        
        # Allow only Authorized Users
        if not check_role(message.author, PERMITTED_ROLE):
            print(f"{message.author} unauthorized command attempt.")
            response = f"<@{message.author.id}>, You are Not authorized to issue Bot Commands."
            await message.channel.send(response)
            return
        
        os.chdir(BEDROCK_SERVER_PATH)
        cmd_output = os.popen('docker-compose up -d').read()
        response = f"<@{message.author.id}>, Server Startup Command sent!\n\n ```\n{cmd_output}\n```"
        await message.channel.send(response)

    if message.content.startswith(f'{BOT_PREFIX} stop minecraft-bedrock'):
        print(f"Got Server Stop Command")
        
        # Allow only Authorized Users
        if not check_role(message.author, PERMITTED_ROLE):
            print(f"{message.author} unauthorized command attempt.")
            response = f"<@{message.author.id}>, You are Not authorized to issue Bot Commands."
            await message.channel.send(response)
            return
        
        response = f"{message.author}, Server Stop Command sent! Please Allow a few Minutes..."
        await message.channel.send(response)
        os.chdir(BEDROCK_SERVER_PATH)
        cmd_output = os.popen('docker-compose down').read()
        response = f"<@{message.author.id}>, Shutdown Command Sent, Response:\n\n ```\n{cmd_output}\n```"
        await message.channel.send(response)

    
    if message.content.startswith(f'{BOT_PREFIX} minecraft-bedrock allowlist add'):
        print(f"Got Minecraft Bedrock Allowlist Add Command")

        # Allow only Authorized Users
        if not check_role(message.author, PERMITTED_ROLE):
            print(f"{message.author} unauthorized command attempt.")
            response = f"<@{message.author.id}>, You are Not authorized to issue Bot Commands."
            await message.channel.send(response)
            return
        
        form_responses[ctx.author.id] = {}
        await ctx.send("Please enter the XUID (Microsoft Unique Identifier from: https://www.cxkes.me/xbox/xuid ):")
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        try:
            xuid_response = await bot.wait_for('message', check=check, timeout=FORM_TIMEOUT)
            form_responses[ctx.author.id]['xuid'] = xuid_response.content
            
            await ctx.send("Please enter the Player Name of the account (as Displayed to Users in game):")
            name_response = await bot.wait_for('message', check=check, timeout=FORM_TIMEOUT)
            form_responses[ctx.author.id]['name'] = name_response.content

            form_input = form_responses[ctx.author.id]
            mcbedrock = MinecraftBedrock()
            mcbedrock.add_allowlist_user(f"{BEDROCK_SERVER_PATH}{BEDROCK_DATA_PATH}/allowlist.json", xuid=form_input['xuid'], name=form_input['name'])
            msg = f"New User Added {form_input['name']} - {form_input['xuid']}"
            await ctx.send(msg)
            #Reset the Form tracking
            form_responses[ctx.author.id] = {}
            print(msg)
        except Exception as e:
            await ctx.send(f"Input Form aborted. Error {e}") 

    if message.content.startswith(f'{BOT_PREFIX} minecraft-bedrock allowlist remove'):
        print(f"Got Minecraft Bedrock Allowlist Remove Command")

        # Allow only Authorized Users
        if not check_role(message.author, PERMITTED_ROLE):
            print(f"{message.author} unauthorized command attempt.")
            response = f"<@{message.author.id}>, You are Not authorized to issue Bot Commands."
            await message.channel.send(response)
            return
        
        form_responses[ctx.author.id] = {}
        await ctx.send("Please enter the Display Name of the User:")
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        try:
            name_response = await bot.wait_for('message', check=check, timeout=FORM_TIMEOUT)
            form_responses[ctx.author.id]['name'] = name_response.content
            
            form_input = form_responses[ctx.author.id]
            mcbedrock = MinecraftBedrock()
            mcbedrock.remove_allowlist_user(f"{BEDROCK_SERVER_PATH}{BEDROCK_DATA_PATH}/allowlist.json", name=form_input['name'])
            msg = f"User removed {form_input['name']}"
            await ctx.send(msg)
            #Reset the Form tracking
            form_responses[ctx.author.id] = {}
            print(msg)
        except Exception as e:
            await ctx.send(f"Input Form aborted. Error {e}")

    if message.content.startswith(f'{BOT_PREFIX} minecraft-bedrock allowlist list'):
        print(f"Got Minecraft Bedrock Allowlist List Command")

        # Allow only Authorized Users
        if not check_role(message.author, PERMITTED_ROLE):
            print(f"{message.author} unauthorized command attempt.")
            response = f"<@{message.author.id}>, You are Not authorized to issue Bot Commands."
            await message.channel.send(response)
            return
        
        mcbedrock = MinecraftBedrock()
        allowlist = mcbedrock.get_allowlist(f"{BEDROCK_SERVER_PATH}{BEDROCK_DATA_PATH}/allowlist.json")
        msg = f"Current Allowlist:\n```json\n{allowlist}\n```"
        
        await ctx.send(msg)

######################
### Helper Methods ###
######################
def check_role(member: discord.member, role_name: str):
    for role in member.roles:
        if role.name.lower() == role_name.lower():
            print(f"{member} was found to have {role_name} role!")
            return True
        
    # If none of those roles match, return false.
    print(f"{member} does not have {role_name} role!")
    return False


bot.run(DISCORD_TOKEN)