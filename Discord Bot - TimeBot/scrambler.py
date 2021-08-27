# scrambler.py
# Basic Text Encryption
# Authors: jchisholm204
# Date: July 7, 2021

import os
import os.path
import dotenv

def load_token():
    dotenv.load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")
    return TOKEN

def parse(item):
    inItem = list(item)
    finalString = ""
    for item in inItem:
        if item == '1':
            finalString = finalString + '0'
        elif item == '2':
            finalString = finalString + '9'
        elif item == '3':
            finalString = finalString + '8'
        elif item == '4':
            finalString = finalString + '7'
        elif item == '5':
            finalString = finalString + '6'
        elif item == '6':
            finalString = finalString + '5'
        elif item == '7':
            finalString = finalString + '4'
        elif item == '8':
            finalString = finalString + '3'
        elif item == '9':
            finalString = finalString + '2'
        elif item == '0':
            finalString = finalString + '1'
        elif item == '-':
            finalString = finalString + '.'
        else:
            finalString = finalString + item
    return finalString

def scramble(item):
    inItem = list(item)
    finalString = ""
    for item in inItem:
        if item == '0':
            finalString = finalString + '1'
        elif item == '9':
            finalString = finalString + '2'
        elif item == '8':
            finalString = finalString + '3'
        elif item == '7':
            finalString = finalString + '4'
        elif item == '6':
            finalString = finalString + '5'
        elif item == '5':
            finalString = finalString + '6'
        elif item == '4':
            finalString = finalString + '7'
        elif item == '3':
            finalString = finalString + '8'
        elif item == '2':
            finalString = finalString + '9'
        elif item == '1':
            finalString = finalString + '0'
        elif item == '.':
            finalString = finalString + '-'
        else:
            finalString = finalString + item
    return finalString