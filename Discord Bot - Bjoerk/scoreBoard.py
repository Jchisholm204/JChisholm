# scoreBoard.py
# RICKLE PICK - Discord Bot
# Scoreboard Testing file
# Authors: jchisholm204
# Date: June 23, 2021

import os
import os.path
from datetime import timedelta
from datetime import datetime
import csv

#returns usrNames, usrTimes
def scoreboard():
    input_path = f"{os.getcwd()}"  # type: str
    user_paths = os.listdir(input_path)

    usrTimes = []
    usrNames = []

    for path in user_paths:
        timePath = f"{os.getcwd()}/{path}/Ttime.txt"
        if os.path.exists(timePath) == True:   
            with open(f'{path}/Ttime.txt', 'r') as fpT:
                usrTseconds = fpT.read()
                usrTimes.append(float(usrTseconds))
                usrNames.append(int(path))

    n=len(usrTimes)
    for i in range(0, n):
        for j in range(0, n-i-1):#-i
            if usrTimes[j] < usrTimes[j+1]:
                usrTimes[j], usrTimes[j+1] = usrTimes[j+1], usrTimes[j]
                usrNames[j], usrNames[j+1] = usrNames[j+1], usrNames[j]

    return (f"HIGHSCORES:\n1. {usrNames[0]}\t-\t{timedelta(seconds=float(usrTimes[0]))}\n2. {usrNames[1]}\t-\t{timedelta(seconds=float(usrTimes[1]))}\n3. {usrNames[2]}\t-\t{timedelta(seconds=float(usrTimes[2]))}\n4. {usrNames[3]}\t-\t{timedelta(seconds=float(usrTimes[3]))}")
#usrTtime = timedelta(seconds=float(usrTseconds))