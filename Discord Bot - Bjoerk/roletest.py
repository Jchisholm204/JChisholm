# bot.py
import os
import os.path
import sys
import json
from datetime import timedelta
from datetime import datetime
import csv
import random
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
    #await client.change_presence(activity=discord.Game(name="GTA IRL"))
    await  client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Rick and Morty"))
    print(f'{client.user} is connected to the following guilds:')
    for guild in client.guilds:
        print(
            f'{guild.name}(id: {guild.id})'
        )


@client.command(name='99')
async def bn99(message):
    if message.author == client.user:
        return
    
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        'bruh',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
    response = random.choice(brooklyn_99_quotes)
    await message.channel.send(response)

@client.command(name='fk')
async def fk(ctx):
    user = discord.utils.get(ctx.guild.members, id=".Iz#9723")
    if ".Iz#9723" is ctx.message.author:
        await ctx.channel.send("fk me? fk u")
    else:
        await ctx.channel.send(user)

@client.command(name='duck')
async def fk(ctx):
    await ctx.channel.send(ctx.author.discriminator)
client.run(TOKEN)