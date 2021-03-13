# bot.py
import os
import sys
import json
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
    if before.channel is None and after.channel is not None:
        print(f'({member}) Has Joined Channel: ({after.channel.name}) On Server: ({member.guild})')

    if before.channel is not None and after.channel is None:
        print(f'({member}) Has Left Channel: ({before.channel.name}) On Server: ({member.guild})')






client.run(TOKEN)