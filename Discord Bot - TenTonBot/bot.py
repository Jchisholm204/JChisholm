# bot.py
import os
import os.path
import csv
import json
from discord import Permissions
from discord import role
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
import discord

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="VEX Change Up"))
    print(f'{client.user} is connected to the following guilds:')
    for guild in client.guilds:
        print(
            f'{guild.name}(id: {guild.id})'
        )
wkDir = os.getcwd()

@client.command(name='next')
async def nextQue(ctx):
    okRole  = discord.utils.get(ctx.guild.roles, name="Field Tech")
    if okRole not in ctx.author.roles:
        return
    with open(f'{wkDir}/Lrow.txt', "r") as LastRow_file:
        LastRow = int(LastRow_file.read())
        Arow = LastRow

    updootChnl = client.get_channel(835381836762841119)

    with open(f'{wkDir}/schedule.csv', 'r') as schedule_file:
        data = list(csv.reader(schedule_file))
        team1 = data[Arow][0]
        team2 = data[Arow][1]
        team3 = data[Arow][2]
        team4 = data[Arow][3]
        team1A = discord.utils.get(ctx.guild.roles, name=team1)
        team2A = discord.utils.get(ctx.guild.roles, name=team2)
        team3A = discord.utils.get(ctx.guild.roles, name=team3)
        team4A = discord.utils.get(ctx.guild.roles, name=team4)
        await updootChnl.send(f'Qual: {Arow} ¯\_(ツ)_/¯ Red: {team1A.mention} {team2A.mention} Blue: {team3A.mention} {team4A.mention}')

    with open(f'{wkDir}/Lrow.txt', "w") as LastRow_file:
        LastRow += 1
        LastRow_file.write(str(LastRow))

@client.command(name='reset')
async def reset_list(ctx):
    okRole = team4A = discord.utils.get(ctx.guild.roles, name="Field Tech")
    if okRole not in ctx.author.roles:
        return
    with open(f'{wkDir}/Lrow.txt', "w") as LRow_file:
        LRow_file.write(str(0))
        await ctx.channel.send('List Position Reset')

@client.command(name='set')
async def reset_list(ctx, row):
    okRole = team4A = discord.utils.get(ctx.guild.roles, name="Field Tech")
    if okRole not in ctx.author.roles:
        return
    with open(f'{wkDir}/Lrow.txt', "w") as LastRow_file:
        LastRow_file.write(str(row))   
        await ctx.channel.send(f'Row Number has been set to match {row}')

@client.command(name='setmatch')
async def reset_list(ctx, row):
    okRole = team4A = discord.utils.get(ctx.guild.roles, name="Field Tech")
    if okRole not in ctx.author.roles:
        return
        row -= 1
    with open(f'{wkDir}/Lrow.txt', "w") as LastRow_file:
        LastRow_file.write(str(row))   
        await ctx.channel.send(f'The Next match will be match {row}')

@client.command(name='hi')
async def hi(ctx):
    await ctx.channel.send(f"hi {ctx.author.mention}")

@client.command(name='send')
async def skeet(ctx):
    updootChnl = client.get_channel(835381836762841119)
    await updootChnl.send('Thanks @everyone and especially Mr Ablett, Dr. Chugani and Ms. Wilson for a great tournament today')
client.run(TOKEN)