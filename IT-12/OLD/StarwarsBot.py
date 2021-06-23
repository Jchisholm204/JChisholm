#personal question bot
#Author: jChisholm204
#Date: 2021-05-17
yeslist = ['yes', 'yha', 'y', 'sure']
print("This test will decide your risk of joining the dark side\n")
red = input("Do you like the color red?\t").strip("!.").lower() in yeslist
capes = input("Do you like capes?\t").strip("!.").lower() in yeslist
if red or capes:
  print("Dark Side it is")
else:
  print("Welcome to the light side")