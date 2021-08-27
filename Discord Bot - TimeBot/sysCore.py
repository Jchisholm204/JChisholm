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
import authority

CrypticToken = scrambler.load_token()

TOKEN = scrambler.parse(CrypticToken)

#load_dotenv()
#TOKEN = os.getenv("DISCORD_TOKEN")

help_command = commands.DefaultHelpCommand(
    no_category = 'Commands'
)

client = commands.Bot(command_prefix='#', help_command=help_command)

@client.event
async def on_ready():
    #await client.change_presence(activity=discord.Game(name="GTA IRL"))
    await  client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="The Time Vortex"))
    print("TIMEBOT:  ONLINE")
    print(f'{client.user} is connected to the following guilds:')
    with open(f"{os.getcwd()}/SysData/online.txt", "w") as online:
        online.write(str(datetime.timestamp(datetime.now())))

    with open(f"{os.getcwd()}/SysData/guilds.csv", "w", newline='') as writeable:
        startupCSV = csv.writer(writeable)
        for guild in client.guilds:
            print(f"{guild.name}(id: {guild.id})")
            startupCSV.writerow([guild.name, guild.id])
    
    if (os.path.exists(f"{os.getcwd()}/SysData/startup.txt")):
        startup_fp = open(f"{os.getcwd()}/SysData/startup.txt", "r")
        startup_msg = startup_fp.read()
        for guild in client.guilds:
            for channel in guild.text_channels:
                try:
                    await channel.send(startup_msg)
                except Exception:
                    continue
                else:
                    break

@client.command(name='99', help='Generates a random Brooklyn Nine Nine Quote', brief='BR99 Quote')
async def testResponce(message):
    if message.author == client.user:
        return
    await message.channel.send(sysHelper.bn99Test())

@client.command(name='rm', help='Generates a random Rick and Morty Quote', brief='R/M Quote')
async def testResponce(message):
    if message.author == client.user:
        return
    await message.channel.send(sysHelper.rmTest())

@client.command(name='tscore', help='Sends a time Scoreboard')
async def TimeScoreBoard(ctx):
    await ctx.channel.send(timeSorter())

@client.command(name='authorize', brief='ADMIN ONLY', help='Adds a new authorized ADMIN user')
async def user_authorization(ctx, newOP=None):
    if authority.checkAuth(ctx.author.discriminator) == False:
        await ctx.channel.send("ERROR\nYou are not authorized to use this command")
        return
    if authority.checkAuth(newOP) == True:
        await ctx.channel.send("ERROR\nThis user is already authorized")
        return
    authority.new_auth(newOP)
    ctx.channel.send(f'{newOP} is now authorized')
    print(f'{newOP} has been authorized by {ctx.author.discriminator}')

@client.command(name='snd', hidden=True)
async def snd(ctx, fpN=None, atts=None):
    if ctx.author.discriminator != '4727':
        await ctx.channel.send("ERROR:\nThis command requires creator authorization -- You are not authorized")
        return
    else:
        if fpN == None:
            await ctx.channel.send("Please specify fpN")
            return
        elif fpN == 'updatemsg':
            if (os.path.exists(f"{os.getcwd()}/SysData/patchNotes.txt")):
                startup_fp = open(f"{os.getcwd()}/SysData/patchNotes.txt", "r")
                startup_msg = startup_fp.read()
                for guild in client.guilds:
                    for channel in guild.text_channels:
                        try:
                            await channel.send(startup_msg)
                        except Exception:
                            continue
                        else:
                            break
            else:
                await ctx.channel.send("ERROR:\nCould not retrive update notes")

@client.command(name='req', brief='Request Bot Records', help='Use this command to request Bot records\nAvalible Records:\nu -- User Data Files\ns -- Full Scoreboard.csv')
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

@client.command(name="backup", brief="ADMIN ONLY", help="Use this command to run a full backup of the bot's user Data.  USER DATA ONLY!")
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

@client.command(name='rank', brief='Get Scoreboard Rank', help="This can be used to obtain your rank if you are not on the leaderboard.\nAdd another members discriminator after the command to get their rank.")
async def rankChecker(ctx, member=None):
    if member == None:
        member = ctx.author.discriminator
    rank = sysHelper.rankCheck(member)
    await ctx.channel.send(f"Client:\t{member}\nRank:\t{rank}")


@client.command(name='status', brief='Get Bot Status', help='No additional information available')
async def status(ctx):
    folder_count = 0  # type: int
    input_path = f"{os.getcwd()}/UserData"  # type: str
    folder_count = len(os.listdir(input_path))
    await ctx.channel.send(f'```ini\nCLIENT STATUS:      [ONLINE]\nTIME STATUS:        [TRACKING]\nTRACKED MEMBERS:    {folder_count}```')

@client.command(name="time", brief='Check your current accumulated time', help="This can be used to obtain your total time on discord since the addition of this bot to your server.\nAdd another members discriminator after the command to get their total time.")
async def checktime(ctx, member=None):
    await ctx.channel.send(sysHelper.get_CurrentTime(ctx, member))

@client.command(name="10", hidden=True)
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

@client.command(name="records", brief='Download your stats.csv', help='This can be used to download your own stats.csv file.\nAdd another members discriminator after the command to obtain their stats.csv file.\n')
async def release_records(ctx, member=None):
    if member is None:
        member  = ctx.author.discriminator
    wkdir = f"{os.getcwd()}/UserData"
    mbr = member
    statsFdir = f"{wkdir}/{mbr}/stats.csv"
    await ctx.channel.send(file=discord.File(statsFdir))

@client.command(name='records-', brief='#records, but in the new format', help="Same as #records, but also includes server and channel information, spacing has also been fixed.\nUsefull if you want to use them for something besides looking at.")
async def release_usrLogs(ctx, member=None):
    if member is None:
        member  = ctx.author.discriminator
    wkdir = f"{os.getcwd()}/UserData"
    mbr = member
    statsFdir = f"{wkdir}/{mbr}/UsrLogs.csv"
    await ctx.channel.send(file=discord.File(statsFdir))


@client.event
async def on_voice_state_update(member, before, after):
    now = datetime.now()
    timeNow = datetime.strftime(now, '%m/%d/%Y %H:%M:%S')
    mbr = member.discriminator
    timestamp = datetime.timestamp(now)
    
    SvrUpdootChnl = discord.utils.get(member.guild.channels, name='timebot')
    

    msrPath = os.getcwd()
    mbrPath = f"{msrPath}/UserData/{mbr}/"
    mbrPath_exists = os.path.exists(mbrPath)
    if mbrPath_exists is not True:
        os.mkdir(mbrPath)

    if before.channel is None and after.channel is not None:
        print(f'({mbr}) Joined Channel: ({after.channel.name}) On Server: ({member.guild}) On: ({timeNow})')
        if SvrUpdootChnl is not None:
            await SvrUpdootChnl.send(f'"{member}" Joined Channel: "{after.channel.name}" On: {sysHelper.timeConverter(datetime.timestamp(datetime.now()))[-1]}\n-----   ¯\_(ツ)_/¯  -----')
        with open(mbrPath+"TempDat.txt", 'w') as tmpDat:
            #tmpDatArray = [now, member, member.guild, after.channel.name]
            tmpDat.write(str(timestamp))

    if before.channel is not None and after.channel is None:
        with open(mbrPath+'TempDat.txt', 'r') as tmpDat:
            tmpDat = tmpDat.read()
            joinTime = datetime.fromtimestamp(float(tmpDat))
        
        with open(f"{os.getcwd()}/SysData/online.txt", "r") as oFile:
            oTime = float(oFile.read())
            #Only process 0x0BOJT if bot has been online for more than 5 mins
            if (timedelta(datetime.timestamp(now) - oTime)) > timedelta(minutes=5):
                #if client joined before the bot was online, the jointime could be incorrect, so discard the time and process error 0x0BOJT
                if oTime > datetime.timestamp(joinTime):
                    print(f"ERROR: (0x0BOJT) Bot offline at join time\nUSER(s) AFFECTED: {mbr}")
                    if SvrUpdootChnl is not None:
                        await SvrUpdootChnl.send(f"ERROR: (0x0BOJT) Bot offline at join time\nUSER(s) AFFECTED: {mbr}")
                    return

        print(f'({mbr}) Has Left Channel: ({before.channel.name}) On Server: ({member.guild}) On: ({timeNow})')
        if SvrUpdootChnl is not None:
            await SvrUpdootChnl.send(f'"{member}" Left Channel: "{before.channel.name}" On: {sysHelper.timeConverter(datetime.timestamp(datetime.now()))[-1]}\n-----   ¯\_(ツ)_/¯  -----')
        
        memberTtime_exists = os.path.isfile(mbrPath+'Ttime.txt')
        if memberTtime_exists is not True:
            print(f'NEW USER: {mbr}')
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

        if os.path.exists(mbrPath+"UsrLogs.csv") == False:
            with open(mbrPath+"UsrLogs.csv", "w", newline='') as usrLogs_fp:
                writer = csv.writer(usrLogs_fp)
                writer.writerow(['Server','Channel','Join Time','Leave Time', 'TimeDif', 'Toltal Accumulative'])

        with open(mbrPath+'UsrLogs.csv', 'a', newline='') as mbrcsv:
            writer = csv.writer(mbrcsv)
            writer.writerow([member.guild, before.channel.name, joinTime, now, timeDif, toltalTtime])       

        if os.path.exists(mbrPath+"stats.csv") == False:
            with open(mbrPath+"stats.csv", "w",) as stats_fp:
                writer = csv.writer(stats_fp)
                writer.writerow(['Join Time','Leave Time', 'TimeDif', 'Toltal Accumulative'])

        with open(mbrPath+'stats.csv', 'a',) as mbrcsv:
            writer = csv.writer(mbrcsv)
            writer.writerow([joinTime, now, timeDif, toltalTtime])
        
        with open(mbrPath+'Ttime.txt', 'w') as ntTime:
            tstToltal = toltalTtime.total_seconds()
            print(tstToltal)
            ntTime.write(str(tstToltal))


client.run(TOKEN)