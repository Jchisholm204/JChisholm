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
    await client.change_presence(activity=discord.Game(name="GTA IRL"))
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


@client.command(name="time")
async def checktime(ctx, member=None):
    wkdir = os.getcwd()
    if member is None:
        usrDir = f"{wkdir}/{ctx.author}/"
        usrName = 'Your'
    else:
        usrDir = f"{wkdir}/{member}/"
        usrName = f"{member}'s"
    usrDir_exists = os.path.exists(usrDir)

    if usrDir_exists is not True:
        await ctx.channel.send("Im sorry, but the records for that user are not avalible at this time,")
        await ctx.channel.send("you may want to try using their full discord name including numbers,")
        await ctx.channel.send("kind of like this OGdiscordUser#0420")
        return
    with open(f'{usrDir}/Ttime.txt', 'r') as fpT:
        usrTseconds = fpT.read()
        usrTtime = timedelta(seconds=float(usrTseconds))
        await ctx.channel.send(f"{usrName} toltal time is {usrTtime}")

@client.command(name="10")
async def tenDaysMarker(ctx, member=None):
    wkdir = os.getcwd()
    if member is None:
        timFD = f"{wkdir}/{ctx.author}/10Days.txt"
        asker = f"you are"
    else:
        timFD = f"{wkdir}/{member}/10Days.txt"
        asker = f"{member} is"
    timFD_exists = os.path.exists(timFD)
    if timFD_exists is not True:
        await ctx.channel.send(f"It would appear that {asker} yet to hit the 10 day mark")
        return
    with open(f'{timFD}', 'r') as timeF:
        tenDayMarker = timeF.read()
        await ctx.channel.send(f"That user surpassed ten days on {tenDayMarker}")

@client.command(name="records")
async def release_records(ctx, member=None):
    wkdir = os.getcwd()
    if member is None:
        statsFdir = f"{wkdir}/{ctx.author}/stats.csv"
    else:
        statsFdir = f"{wkdir}/{member}/stats.csv"
    await ctx.channel.send(file=discord.File(statsFdir))

@client.event
async def on_voice_state_update(member, before, after):
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    
    bjoerkChannel = client.get_channel(821473151342870548)

    msrPath = os.getcwd()
    mbrPath = f"{msrPath}/{member}/"
    mbrPath_exists = os.path.exists(mbrPath)
    if mbrPath_exists is not True:
        os.mkdir(mbrPath)

    if before.channel is None and after.channel is not None:
        print(f'({member}) Has Joined Channel: ({after.channel.name}) On Server: ({member.guild}) At: ({now})')
        await bjoerkChannel.send(f'"{member}" Has Joined Channel: "{after.channel.name}" On Server: "{member.guild}" At: {now}')
        await bjoerkChannel.send("-----   ¯\_(ツ)_/¯  -----")
        with open(f"{msrPath}/{member}/"+"TempDat.txt", 'w') as tmpDat:
            #tmpDatArray = [now, member, member.guild, after.channel.name]
            tmpDat.write(str(timestamp))

    if before.channel is not None and after.channel is None:
        print(f'({member}) Has Left Channel: ({before.channel.name}) On Server: ({member.guild}) At: ({now})')
        await bjoerkChannel.send(f'"{member}" Has Left Channel: "{before.channel.name}" On Server: "{member.guild}" At: {now}')
        

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

        mbr10Days_true = os.path.exists(f"{msrPath}/{member}/10Days.txt")
        tentime = timedelta(days=10)

        if mbr10Days_true is not True and toltalTtime >= tentime:
            with open(f"{msrPath}/{member}/"+'10Days.txt', 'w') as tenDays:
                print(f"{member} Has Surpassed 10 Days")
                tenDays.write(str(now))
                await bjoerkChannel.send(f"@everyone {member} has just surpassed Ten whole days on discord! Congratulations on not having a life.")
                await bjoerkChannel.send(f"@everyone {member}'s Toltal Time is now {toltalTtime}")
        else:
            await bjoerkChannel.send(f"{member}'s Toltal Time is {toltalTtime}")
        
        await bjoerkChannel.send(" -----   ¯\_(ツ)_/¯  -----")

        with open(f"{msrPath}/{member}/"+'stats.csv', 'a') as mbrcsv:
            writer = csv.writer(mbrcsv)
            writer.writerow([joinTime, now, timeDif, toltalTtime])
        
        with open(f"{msrPath}/{member}/"+'Ttime.txt', 'w') as ntTime:
            tstToltal = toltalTtime.total_seconds()
            print(tstToltal)
            ntTime.write(str(tstToltal))


client.run(TOKEN)