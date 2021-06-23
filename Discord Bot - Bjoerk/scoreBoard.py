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
async def scoreboard():
    input_path = f"{os.getcwd()}"  # type: str
    user_paths = os.listdir(input_path)

    usrNames = []
    usrTimes = []

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

    return usrNames, usrTimes
#usrTtime = timedelta(seconds=float(usrTseconds))