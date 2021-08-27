# Authority.py
# Basic Authority Program
# Authors: jchisholm204
# Date: August 27, 2021

import csv
import os

def checkAuth(usr=None):
    with open(f'{os.getcwd()}/sysData/authorized.csv', 'r', newline='') as authorizedFile:
        authorized = list(csv.reader(authorizedFile))
        if usr == None:
            return 'ERROR\nUser Not Specified'
        elif usr in authorized:
            return True
        elif usr not in authorized:
            return False

def get_auths():
    with open(f'{os.getcwd()}/sysData/authorized.csv', 'r', newline='') as authorizedFile:
        authorized = list(csv.reader(authorizedFile))
        return authorized

def new_auth(newOP):
    with open(f'{os.getcwd()}/sysData/authorized.csv', 'a', newline='') as authorizedFile:
        writer = csv.writer(authorizedFile)
        writer.writerow([newOP])