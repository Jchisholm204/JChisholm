# scoreBoard.py
# Discord Hours Scoreboard Generator
# Authors: jchisholm204
# Date: June 23, 2021

import os
import os.path
from datetime import timedelta
from datetime import datetime
import csv
import sysHelper

def scoreboard():
    usrNames, usrTimes = sysHelper.scoreSorter()
    #print(f"HIGHSCORES:\n1. {usrNames[0]}\t-\t{timedelta(seconds=float(usrTimes[0]))}\n2. {usrNames[1]}\t-\t{timedelta(seconds=float(usrTimes[1]))}\n3. {usrNames[2]}\t-\t{timedelta(seconds=float(usrTimes[2]))}\n4. {usrNames[3]}\t-\t{timedelta(seconds=float(usrTimes[3]))}")

    with open(f"{os.getcwd()}/SysData/ScoreBoard.csv", "w") as sbFile:
        sbCSV = csv.writer(sbFile)
        sbCSV.writerow(usrNames)
        sbCSV.writerow(usrTimes)
        sbCSV.writerow(sysHelper.timeConverter(datetime.timestamp(datetime.now())))
    
    return f"HIGHSCORES:\n1. {usrNames[0]}\t-\t{timedelta(seconds=float(usrTimes[0]))}\n2. {usrNames[1]}\t-\t{timedelta(seconds=float(usrTimes[1]))}\n3. {usrNames[2]}\t-\t{timedelta(seconds=float(usrTimes[2]))}\n4. {usrNames[3]}\t-\t{timedelta(seconds=float(usrTimes[3]))}\n5. {usrNames[4]}\t-\t{timedelta(seconds=float(usrTimes[4]))}\n6. {usrNames[5]}\t-\t{timedelta(seconds=float(usrTimes[5]))}"


#usrTtime = timedelta(seconds=float(usrTseconds))
scoreboard()