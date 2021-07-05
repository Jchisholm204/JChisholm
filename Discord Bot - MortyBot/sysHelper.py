# sysHelper.py
# MORTYBOT - Discord Bot
# Authors: jchisholm204
# Date: July 5, 2021

import os
import os.path
import sys
import json
from datetime import timedelta
from datetime import datetime
import discord
import csv
import random

def get_CurrentTime(ctx, member):
    wkdir = os.getcwd()
    if member is None:
        usrDir = f"{wkdir}/{ctx.author.discriminator}/"
        usrName = 'Your'
    else:
        usrDir = f"{wkdir}/{member}/"
        usrName = f"{member}'s"
    usrDir_exists = os.path.exists(usrDir)

    if usrDir_exists is not True:
        return ("Im sorry, but the records for that user are not avalible at this time,\nTo access records, please use the numbers after the # in your name.\n ThankYou")
    with open(f'{usrDir}/Ttime.txt', 'r') as fpT:
        usrTseconds = fpT.read()
        usrTtime = timedelta(seconds=float(usrTseconds))
        return(f"{usrName} total time is {usrTtime}")

def bn99Test():   
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        'bruh',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
    return (random.choice(brooklyn_99_quotes))

def tenDaysCheck(usr):
    usrDir = f"{os.getcwd()}/UserData/{usr}"
    fileExists = os.path.exists(f"{usrDir}/10Days.txt")
    if fileExists == True:
        with open(f"{usrDir}/10Days.txt", "r") as tenDays:
            return True, tenDays.read()
    else:
        return False, 0
