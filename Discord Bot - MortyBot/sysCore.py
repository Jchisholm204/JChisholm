# sysCore.py
# MORTYBOT - Discord Bot
# Authors: jchisholm204
# Date: July 5, 2021

import os
import os.path
import sys
import json
from datetime import timedelta
from datetime import datetime
import csv
import random
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
import discord
from scoreBoard import scoreboard as timeSorter
import sysHelper
import zipfile
import scrambler

CrypticToken = scrambler.load_token()

TOKEN = scrambler.parse(CrypticToken)

#load_dotenv()
#TOKEN = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix='#')

@client.event
async def on_ready():
    #await client.change_presence(activity=discord.Game(name="GTA IRL"))
    await  client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Rick and Morty"))
    print("MORTYBOT:  ONLINE")
    print(f'{client.user} is connected to the following guilds:')
    with open(f"{os.getcwd()}/SysData/online.txt", "w") as online:
        online.write(str(datetime.timestamp(datetime.now())))
    
    startupPath = f"{os.getcwd()}/SysData/guilds.csv"

    for guild in client.guilds:
        print(f"{guild.name}(id: {guild.id})")
    
    with open(startupPath, "w") as writeable:
        startupCSV = csv.writer(writeable)
        startupCSV.writerow(client.guilds)

@client.command(name='99')
async def testResponce(message):
    if message.author == client.user:
        return
    await message.channel.send(sysHelper.bn99Test())

@client.command(name='tscore')
async def TimeScoreBoard(ctx):
    await ctx.channel.send(timeSorter())

@client.command(name='authorize')
async def user_authorization(ctx, newOP=None):
    with open(f'{os.getcwd()}/sysData/authorized.csv', 'r') as authorizedFile:
        authorized = list(csv.reader(authorizedFile))
        if [ctx.author.discriminator] not in authorized:
            await ctx.channel.send("ERROR:\nYou are not authorized to use this command.")
            return
        elif newOP == None:
            await ctx.channel.send("ERROR:\nYou must specify a user.")
            return
        elif [newOP] in authorized:
            await ctx.channel.send("ERROR:\nThis user is already authorized.")
            return
        await ctx.channel.send("ERROR:\nAuthorization Services Unavalible\n(0x04, function not present)")


@client.command(name='req')
async def dataDump(ctx, request=None):
    if request == None:
        await ctx.channel.send("Please Make A Request:\nu -- User Data Files\ns -- Full Scoreboard.csv")
    elif request == 'u':
        await ctx.channel.send("REQ RECIEVED:\nAll User Data\nZipping Data...\tPlease Wait..")
        wkdir = os.getcwd()
        zf = zipfile.ZipFile(f"{os.getcwd()}/sysData/Requests/UserData.zip", "w")
        for dirname, subdirs, files in os.walk(f"{os.getcwd()}/UserData"):
            zf.write(dirname)
            for filename in files:
                zf.write(os.path.join(dirname, filename))
        zf.close()
        await ctx.channel.send(file=discord.File(f"{os.getcwd()}/sysData/Requests/UserData.zip"))
    elif request == 's':
        await ctx.channel.send("REQ RECIEVED:\nScoreboard.csv Data")
        await ctx.channel.send(file=discord.File(f"{os.getcwd()}/sysData/ScoreBoard.csv"))
    else:
        await ctx.channel.send("ERROR: Unknown file request (0x00)")

@client.command(name="backup")
async def bot_backup(ctx):
    authorized = list(open(f"{os.getcwd()}/sysData/authorized.csv", "r"))
    print(f"{ctx.author} requested a user data backup..")
    await ctx.channel.send("Request Recieved..\nAwaiting Authorization")
    if ctx.author.discriminator not in authorized:
        await ctx.channel.send(f"REQUEST DENIED:\nUser ({ctx.author.discriminator}) Not Authorized")
        print(f"ERROR: {ctx.author.discriminator} Not Authorized")
        return
    wkdir = os.getcwd()
    zf = zipfile.ZipFile(f"{os.getcwd()}/sysData/Backups/{datetime.timestamp(datetime.now())}.zip", "w")
    for dirname, subdirs, files in os.walk(f"{os.getcwd()}/UserData"):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
    zf.close()
    await ctx.channel.send(";) Data Backup Completed ;)")
    print("Backup Completed")

@client.command(name='rank')
async def rankChecker(ctx, member=None):
    if member == None:
        member = ctx.author.discriminator
    rank = sysHelper.rankCheck(member)
    await ctx.channel.send(f"Client:\t{member}\nRank:\t{rank}")


@client.command(name='status')
async def status(ctx):
    folder_count = 0  # type: int
    input_path = f"{os.getcwd()}/UserData"  # type: str
    folder_count = len(os.listdir(input_path))
    await ctx.channel.send(f'```ini\nCLIENT STATUS:      [ONLINE]\nTIME STATUS:        [TRACKING]\nTRACKED MEMBERS:    {folder_count}```')

@client.command(name="time")
async def checktime(ctx, member=None):
    await ctx.channel.send(sysHelper.get_CurrentTime(ctx, member))

@client.command(name="10")
async def tenDaysMarker(ctx, member=None):
    if member == None:
        member = ctx.author.discriminator
        tf, date = sysHelper.tenDaysCheck(member)
    else:
        tf, date = sysHelper.tenDaysCheck(member)
    if tf is not True:
        await ctx.channel.send(f"It would appear that {member} yet to hit the 10 day mark")
    else:
        dateWhen = sysHelper.timeConverter(datetime.timestamp(datetime.fromisoformat(date)))[-1]
        await ctx.channel.send(f"{member} surpassed ten days on {dateWhen}")

@client.command(name="records")
async def release_records(ctx, member=None):
    if member is None:
        member  = ctx.author.discriminator
    wkdir = f"{os.getcwd()}/UserData"
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
    mbrPath = f"{msrPath}/UserData/{mbr}/"
    mbrPath_exists = os.path.exists(mbrPath)
    if mbrPath_exists is not True:
        os.mkdir(mbrPath)

    if before.channel is None and after.channel is not None:
        print(f'({mbr}) Joined Channel: ({after.channel.name}) On Server: ({member.guild}) At: ({timeNow})')
        await bjoerkChannel.send(f'"{member}" Joined Channel: "{after.channel.name}" On Server: "{member.guild}" At: {sysHelper.timeConverter(datetime.timestamp(datetime.now()))[-1]}')
        await brianChannel.send(f'"{member}" Joined Channel: "{after.channel.name}" On Server: "{member.guild}" At: {sysHelper.timeConverter(datetime.timestamp(datetime.now()))[-1]}')
        await bjoerkChannel.send("-----   ¯\_(ツ)_/¯  -----")
        await brianChannel.send("-----   ¯\_(ツ)_/¯  -----")
        with open(mbrPath+"TempDat.txt", 'w') as tmpDat:
            #tmpDatArray = [now, member, member.guild, after.channel.name]
            tmpDat.write(str(timestamp))

    if before.channel is not None and after.channel is None:
        with open(mbrPath+'TempDat.txt', 'r') as tmpDat:
            tmpDat = tmpDat.read()
            joinTime = datetime.fromtimestamp(float(tmpDat))
        with open(f"{os.getcwd()}/SysData/online.txt", "r") as oFile:
            oTime = float(oFile.read())
            if oTime > datetime.timestamp(joinTime):
                print(f"ERROR: Bot offline at join time\nUSER(s) AFFECTED: {mbr}")
                await bjoerkChannel.send(f"ERROR: Bot offline at join time\nUSER(s) AFFECTED: {mbr}")
                await brianChannel.send(f"ERROR: Bot offline at join time\nUSER(s) AFFECTED: {mbr}")
                return

        print(f'({mbr}) Has Left Channel: ({before.channel.name}) On Server: ({member.guild}) At: ({timeNow})')
        await bjoerkChannel.send(f'"{member}" Left Channel: "{before.channel.name}" On Server: "{member.guild}" At: {sysHelper.timeConverter(datetime.timestamp(datetime.now()))[-1]}')
        await brianChannel.send(f'"{member}" Left Channel: "{before.channel.name}" On Server: "{member.guild}" At: {sysHelper.timeConverter(datetime.timestamp(datetime.now()))[-1]}')
        
        memberTtime_exists = os.path.isfile(mbrPath+'Ttime.txt')
        if memberTtime_exists is not True:
            with open(mbrPath+'Ttime.txt', "w") as crtFile:
                crtFile.write('0')
            
        with open(mbrPath+'Ttime.txt', "r") as tTime:
            tmpTdat = tTime.read()
            TTime = timedelta(seconds=float(tmpTdat))

        timeDif = now - joinTime
        toltalTtime = TTime + timeDif
        print(toltalTtime)

        mbr10Days_true, date = sysHelper.tenDaysCheck(mbr)
        tentime = timedelta(days=10)

        if mbr10Days_true is not True and toltalTtime >= tentime:
            with open(mbrPath+'10Days.txt', 'w') as tenDays:
                print(f"{member} Has Surpassed 10 Days")
                tenDays.write(str(now))
                await bjoerkChannel.send(f"@everyone {member} has just surpassed Ten whole days on discord! What the fuck is wrong with you..?")
                await bjoerkChannel.send(f"@everyone {member}'s Toltal Time is now {toltalTtime}")
        else:
            await bjoerkChannel.send(f"{member}'s Total Time is {toltalTtime}")
        
        await bjoerkChannel.send(" -----   ¯\_(ツ)_/¯  -----")
        await brianChannel.send(" -----   ¯\_(ツ)_/¯  -----")

        with open(mbrPath+'stats.csv', 'a') as mbrcsv:
            writer = csv.writer(mbrcsv)
            writer.writerow([joinTime, now, timeDif, toltalTtime])
        
        with open(mbrPath+'Ttime.txt', 'w') as ntTime:
            tstToltal = toltalTtime.total_seconds()
            print(tstToltal)
            ntTime.write(str(tstToltal))


client.run(TOKEN)