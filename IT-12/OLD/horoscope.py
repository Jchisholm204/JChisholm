#Horiscope Bot
#Author: jChisholm204
#Date: 2021-05-05
import random
name = input("Hi, I'm Rick, Whats your name?\t")
responcef = [f"sup, nice to meet you {name}", f"Hiya {name}", f"toppa the morning {name}"]
print(random.choice(responcef))
favThing = input("Whats your fav thing?\t")
responces = [f"WHAT? I love {favThing} too!", f"Thats neat, I've heard {favThing} is fantastic"]
print(random.choice(responces))
year = int(input("What year were you born?\n"))
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