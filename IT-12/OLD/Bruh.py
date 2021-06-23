#Quote Generator
#Author: jChisholm204
#Date: 2021-05-05
import random
import time
yesList = ["yha", "yes", "y", "sure", "a lot", "ok", "k", "why not"]
noList = ["no", "nope", "nah", "no thanks", "n"]

def nothing_left():
  dum = input("So.. anything cool to tell me?\t")
  print("That's neat.")
  one = input("Seen any good movies recently?\t")
  if one in noList:
    print("oh.")
  else:
    print("Was it good? I've been dying to see "+one)
    input()
    print("I've got to go.. See you later")
    
def spirit(year):
  if(year - 4)%12==0:
    print("Your a Rat")
  if(year - 5)%12==0:
    print("Your a Ox")
  if(year - 6)%12==0:
    print("Your a Tiger")
  if(year - 7)%12==0:
    print("Your a Rabbit")
  if(year - 8)%12==0:
    print("Your a Dragon")
  if(year - 9)%12==0:
    print("Your a Snake")
  if(year - 10)%12==0:
    print("Your a Horse")
  if(year - 11)%12==0:
    print("Your a Goat")
  if(year - 12)%12==0:
    print("Your a Monkey")
  if(year - 13)%12==0:
    print("Your a Rooster")
  if(year - 14)%12==0:
    print("Your a Dog")
  if(year - 15)%12==0:
    print("Your a Pig")
  nothing_left()

def likesProg():
  print("REALLY? I like programming as well.")
  print("Thats great to hear. I hear bad things happen to people who dont like programming")
  age = input("anyways, how old are you? I'll go first, I was created on 2021-05-05.\t")
  if int(age) > 45:
    print('damn u an old grandpa then..')
  elif int(age) > 23:
    print("damn u old") 
  if int(age) == 9:
    print("I dont talk to people in the 9yr old army")
  elif int(age) < 12:
    print("SHEEEESH")
  elif int(age) < 23:
    print("ahh so ur what a melenial is..")
  born = 2021-int(age)
  print("You Know I can tell you your chinese spirit animal right?")
  spirit_q = input("Do you want me to?\t")
  if spirit_q in yesList:
    spirit(int(born))
  else:
    sure = input("Are you sure?\t")
    if sure in yesList:
      print("Ok then.")
      nothing_left()
    else:
      print('Ok then,')
      spirit(int(born))
    
    
def insultFunction():
  name = input("Hi, I'm Rick, Whats your name?\t")
  responcef = [f"sup, nice to meet you {name}", f"Hiya {name}", f"toppa the morning {name}"]
  print(random.choice(responcef))
  favThing = input("Whats your fav thing?\t")
  responces = [f"WHAT? I love {favThing} too!", f"Thats neat, I've heard {favThing} is fantastic"]
  print(random.choice(responces))
  while 1:
    ulikeq = input("Hey, do you like programing?\t")
    if ulikeq in yesList:
      likesProg()
      return 0
    else:
      print("Well, I'm just a program, so I'm incapable of phycical damage, but... I'll ask you again...")
  return 1

while 1:
  insultFunction()
  print("\n\n")
  time.sleep(3)