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
            return [True, tenDays.read()]
    else:
        return [False, 0]

def monthConverter(monthNumber):
    if monthNumber == 1:
        return "January"
    elif monthNumber == 2:
        return "Febuary"
    elif monthNumber == 3:
        return "March"
    elif monthNumber == 4:
        return "April"
    elif monthNumber == 5:
        return "May"
    elif monthNumber == 6:
        return "June"
    elif monthNumber == 7:
        return "July"
    elif monthNumber == 8:
        return "August"
    elif monthNumber == 9:
        return "September"
    elif monthNumber == 10:
        return "October"
    elif monthNumber == 11:
        return "November"
    elif monthNumber == 12:
        return "December"
    else:
        return "{ERROR: Unknown Month}"


def timeConverter(timestamp):
    pam = "am"
    time = datetime.fromtimestamp(timestamp)
    hour = time.hour
    minute = time.minute
    day = time.day
    month = time.month
    if hour > 12:
        hour -= 12
        pam = "pm"

    oString = f"{monthConverter(month)} {day}, {hour}:{minute}{pam}"
    return [monthConverter(month), day, hour, minute, pam, oString]

def inList(arr, item):
    for i in range(0,len(arr)):
        if str(arr[i]) == str(item):
            return i

#returns usrNames, usrTimes
def scoreSorter():
    input_path = f"{os.getcwd()}/UserData"  # type: str
    user_paths = os.listdir(input_path)

    usrTimes = []
    usrNames = []

    for path in user_paths:
        timePath = f"{os.getcwd()}/UserData/{path}/Ttime.txt"
        if os.path.exists(timePath) == True:   
            with open(timePath, 'r') as fpT:
                usrTseconds = fpT.read()
                usrTimes.append(float(usrTseconds))
                usrNames.append(path)
    n=len(usrTimes)
    for i in range(0, n):
        for j in range(0, n-i-1):#-i
            if usrTimes[j] < usrTimes[j+1]:
                usrTimes[j], usrTimes[j+1] = usrTimes[j+1], usrTimes[j]
                usrNames[j], usrNames[j+1] = usrNames[j+1], usrNames[j]
    return [usrNames, usrTimes]

def rankCheck(member):
    usrNames, usrTimes = scoreSorter()
    rank = inList(usrNames, member) + 1
    if rank == None:
        return "ERROR: Rank could not be determined"
    return rank, usrTimes[rank-1]

#print("yeet skeet and", monthConverter(13),"my meat")