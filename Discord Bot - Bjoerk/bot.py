# bot.py
import os
import sys
import json
import datetime
from datetime import datetime
import csv
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv

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
async def on_voice_state_update(member, before, after):
    now = datetime.now()
    timestamp = datetime.timestamp(now)

    if before.channel is None and after.channel is not None:
        print(f'({member}) Has Joined Channel: ({after.channel.name}) On Server: ({member.guild}) At: ({now})')
        with open(f'{member}.txt', 'w') as fd:
            fd.write(f'Server: {member.guild}, Channel: {after.channel.name}, Joined:{now}')
        with open(f'{member}Time.txt', 'w') as fnt:
            fnt.write(str(timestamp))

    if before.channel is not None and after.channel is None:
        print(f'({member}) Has Left Channel: ({before.channel.name}) On Server: ({member.guild}) At: ({now})')

        with open(f'{member}.txt', 'r') as fo:
            oldDat = fo.read()
        with open(f'{member}Time.txt', 'r') as fot:
            timeDatStr = fot.read()
            #timeDat = datetime.strptime(timeDatStr, '%Y-%m-%d %H:%M:%S.%f')
            timeDat = datetime.fromtimestamp(float(timeDatStr)).isoformat()
        with open(f'{member}TToltal.txt', 'r') as ttfd:
            oldTTstr = ttfd.read()
            oldTtoltal = datetime.fromtimestamp(float(oldTTstr)).isoformat()
        with open(f'{member}.csv', 'a') as fd:
            timeDif = now - timeDat
            newTtoltal = oldTtoltal + timeDif
            writer = csv.writer(fd)
            writer.writerow(oldDat, now, timeDif, newTtoltal)
        with open(f'{member}TToltal.txt', 'w') as tTfd:
            timestampToltal = datetime.timestamp(newTtoltal)
            tTfd.write(timestampToltal)






client.run(TOKEN)