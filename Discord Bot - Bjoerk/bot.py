# bot.py
# RICKLE PICK - Discord Bot
# Authors: jchisholm204
# Date: Mar 10, 2021

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
from discord.ext import tasks
from discord.utils import get
from dotenv import load_dotenv
import discord
from scoreBoard import scoreboard as timeSorter

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

@client.command(name='tscore')
async def TimeScoreBoard(ctx):
    await ctx.channel.send(timeSorter())


@client.command(name='status')
async def status(ctx):
    folder_count = 0  # type: int
    input_path = f"{os.getcwd()}"  # type: str
    folder_count = len(os.listdir(input_path))
    await ctx.channel.send(f'```ini\nCLIENT STATUS:      [ONLINE]\nTIME STATUS:        [TRACKING]\nTRACKED MEMBERS:    {folder_count}```')
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
        usrDir = f"{wkdir}/{ctx.author.discriminator}/"
        usrName = 'Your'
    else:
        usrDir = f"{wkdir}/{member}/"
        usrName = f"{member}'s"
    usrDir_exists = os.path.exists(usrDir)

    if usrDir_exists is not True:
        await ctx.channel.send("Im sorry, but the records for that user are not avalible at this time,")
        await ctx.channel.send("To access records, please use the numbers after the # in your name.\n ThankYou")
        return
    with open(f'{usrDir}/Ttime.txt', 'r') as fpT:
        usrTseconds = fpT.read()
        usrTtime = timedelta(seconds=float(usrTseconds))
        await ctx.channel.send(f"{usrName} total time is {usrTtime}")

@client.command(name="10")
async def tenDaysMarker(ctx, member=None):
    wkdir = os.getcwd()
    if member is None:
        timFD = f"{wkdir}/{ctx.author.discriminator}/10Days.txt"
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
    if member is None:
        member  = ctx.author.discriminator
    wkdir = os.getcwd()
    mbr = member
    statsFdir = f"{wkdir}/{mbr}/stats.csv"
    await ctx.channel.send(file=discord.File(statsFdir))

@client.event
async def on_voice_state_update(member, before, after):
    now = datetime.now()
    timeNow = datetime.strftime(now, '%m/%d/%Y %H:%M:%S')
    mbr = member.discriminator
    timestamp = datetime.timestamp(now)
    
    bjoerkChannel = client.get_channel(835204702924046346) #821473151342870548
    brianChannel = client.get_channel(847143897448316948)

    msrPath = os.getcwd()
    mbrPath = f"{msrPath}/{mbr}/"
    mbrPath_exists = os.path.exists(mbrPath)
    if mbrPath_exists is not True:
        os.mkdir(mbrPath)

    if before.channel is None and after.channel is not None:
        print(f'({mbr}) Has Joined Channel: ({after.channel.name}) On Server: ({member.guild}) At: ({timeNow})')
        await bjoerkChannel.send(f'"{member}" Has Joined Channel: "{after.channel.name}" On Server: "{member.guild}" At: {timeNow}')
        await brianChannel.send(f'"{member}" Has Joined Channel: "{after.channel.name}" On Server: "{member.guild}" At: {timeNow}')
        await bjoerkChannel.send("-----   ¯\_(ツ)_/¯  -----")
        await brianChannel.send("-----   ¯\_(ツ)_/¯  -----")
        with open(f"{msrPath}/{mbr}/"+"TempDat.txt", 'w') as tmpDat:
            #tmpDatArray = [now, member, member.guild, after.channel.name]
            tmpDat.write(str(timestamp))

    if before.channel is not None and after.channel is None:
        print(f'({member}) Has Left Channel: ({before.channel.name}) On Server: ({member.guild}) At: ({timeNow})')
        await bjoerkChannel.send(f'"{member}" Has Left Channel: "{before.channel.name}" On Server: "{member.guild}" At: {timeNow}')
        await brianChannel.send(f'"{member}" Has Left Channel: "{before.channel.name}" On Server: "{member.guild}" At: {timeNow}')
        

        with open(f"{msrPath}/{mbr}/"+'TempDat.txt', 'r') as tmpDat:
            tmpDat = tmpDat.read()
            joinTime = datetime.fromtimestamp(float(tmpDat))
            #joinTime = datetime.strftime(joinTimeStr, "%Y-%m-%d %H:%M:%S.%f")
        
        memberTtime_exists = os.path.isfile(f"{msrPath}/{mbr}/"+'Ttime.txt')
        if memberTtime_exists is not True:
            with open(f"{msrPath}/{mbr}/"+'Ttime.txt', "w") as crtFile:
                crtFile.write('0')
            
        with open(f"{msrPath}/{mbr}/"+'Ttime.txt', "r") as tTime:
            tmpTdat = tTime.read()
            TTime = timedelta(seconds=float(tmpTdat))

        timeDif = now - joinTime
        toltalTtime = TTime + timeDif
        print(toltalTtime)

        mbr10Days_true = os.path.exists(f"{msrPath}/{mbr}/10Days.txt")
        tentime = timedelta(days=10)

        if mbr10Days_true is not True and toltalTtime >= tentime:
            with open(f"{msrPath}/{mbr}/"+'10Days.txt', 'w') as tenDays:
                print(f"{member} Has Surpassed 10 Days")
                tenDays.write(str(now))
                await bjoerkChannel.send(f"@everyone {member} has just surpassed Ten whole days on discord! What the fuck is wrong with you..?")
                await bjoerkChannel.send(f"@everyone {member}'s Toltal Time is now {toltalTtime}")
        else:
            await bjoerkChannel.send(f"{member}'s Total Time is {toltalTtime}")
        
        await bjoerkChannel.send(" -----   ¯\_(ツ)_/¯  -----")
        await brianChannel.send(" -----   ¯\_(ツ)_/¯  -----")

        with open(f"{msrPath}/{mbr}/"+'stats.csv', 'a') as mbrcsv:
            writer = csv.writer(mbrcsv)
            writer.writerow([joinTime, now, timeDif, toltalTtime])
        
        with open(f"{msrPath}/{mbr}/"+'Ttime.txt', 'w') as ntTime:
            tstToltal = toltalTtime.total_seconds()
            print(tstToltal)
            ntTime.write(str(tstToltal))


client.run(TOKEN)