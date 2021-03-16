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
    print(f'{client.user} is connected to the following guilds:')
    for guild in client.guilds:
        print(
            f'{guild.name}(id: {guild.id})'
        )

@client.command(name="prv")
async def listUsers(message):
    if message.author == client.user:
        return
    channel = client.get_channel(811134776492818493)
    members = channel.members
    for member in members:
        #print(member.id)
        username = await client.fetch_user(member.id)
        await message.channel.send(f'{username}   ------    id: ({member.id})')
        print(
            f'{username}(id: {member.id})'
        )
    if not members:
        await message.channel.send("I couldn't find any connected members.. ¯\_(ツ)_/¯")

@client.command(name="pub")
async def listUsers(message):
    if message.author == client.user:
        return
    channel = client.get_channel(810436014828945422)
    members = channel.members
    for member in members:
        #print(member.id)
        username = await client.fetch_user(member.id)
        await message.channel.send(f'{username}   ------   id: ({member.id})')
        print(
            f'{username}(id: {member.id})'
        )
    if not members:
        await message.channel.send("I couldn't find any connected members.. ¯\_(ツ)_/¯")

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


@client.command(name='join')
async def joinVC(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@client.command(name='die')
async def leaveVC(ctx):
    await ctx.voice_client.disconnect()

@client.event
async def on_message(message):
    if message.author is client.user:
        return
    if 'what is my height' in message.content:
        rnNumber = ((random.random() / random.random()) *180)
        await message.channel.send(f'Your height is not {rnNumber} cm')


@client.event
async def on_voice_state_update(member, before, after):
    now = datetime.now()
    timestamp = datetime.timestamp(now)

    msrPath = os.getcwd()
    mbrPath = f"{msrPath}/{member}/"
    mbrPath_exists = os.path.exists(mbrPath)
    if mbrPath_exists is not True:
        os.mkdir(mbrPath)

    if before.channel is None and after.channel is not None:
        print(f'({member}) Has Joined Channel: ({after.channel.name}) On Server: ({member.guild}) At: ({now})')
        with open(f"{msrPath}/{member}/"+"TempDat.txt", 'w') as tmpDat:
            #tmpDatArray = [now, member, member.guild, after.channel.name]
            tmpDat.write(str(timestamp))

    if before.channel is not None and after.channel is None:
        print(f'({member}) Has Left Channel: ({before.channel.name}) On Server: ({member.guild}) At: ({now})')

        with open(f"{msrPath}/{member}/"+'TempDat.txt', 'r') as tmpDat:
            tmpDat = tmpDat.read()
            joinTime = datetime.fromtimestamp(float(tmpDat))
            #joinTime = datetime.strftime(joinTimeStr, "%Y-%m-%d %H:%M:%S.%f")
        
        memberTtime_exists = os.path.isfile(f"{msrPath}/{member}/"+'Ttime.txt')
        if memberTtime_exists is not True:
            with open(f"{msrPath}/{member}/"+'Ttime.txt', "w") as crtFile:
                crtFile.write('0')
            
        with open(f"{msrPath}/{member}/"+'Ttime.txt', "r") as tTime:
            tmpTdat = tTime.read()
            TTime = timedelta(seconds=float(tmpTdat))

        timeDif = now - joinTime
        toltalTtime = TTime + timeDif
        print(toltalTtime)

        with open(f"{msrPath}/{member}/"+'stats.csv', 'a') as mbrcsv:
            writer = csv.writer(mbrcsv)
            writer.writerow([joinTime, now, timeDif, toltalTtime])
        
        with open(f"{msrPath}/{member}/"+'Ttime.txt', 'w') as ntTime:
            tstToltal = toltalTtime.total_seconds()
            print(tstToltal)
            ntTime.write(str(tstToltal))


client.run(TOKEN)