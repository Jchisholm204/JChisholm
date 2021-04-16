# bot.py
import os
import os.path
import sys
from discord import Permissions
from discord import role
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
import discord

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix='#')

@client.event
async def on_ready():
    bot_status = discord.Status.idle
    #await client.change_presence(activity=discord.Game(name="GTA IRL"))
    await client.change_presence(status=bot_status, activity=discord.Activity(type=discord.ActivityType.watching, name ='The Hours Pass'))
    print(f'{client.user} is connected to the following guilds:')
    for guild in client.guilds:
        print(
            f'{guild.name}(id: {guild.id})'
        )
client.run(TOKEN)