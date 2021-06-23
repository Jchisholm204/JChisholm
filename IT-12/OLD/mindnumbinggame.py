#mind numbing game
#Author: jChisholm204
#Date: 2021-05-13
import random
import time
import replit
global score
score = 0
wordlist = ['cat', 'jupiter', 'nasa']
for topic in wordlist:
  replit.clear()
  print(f"Welcome to the most mind numbing game ever created besides possibly fall guys\nenter three words related to the word {topic}:")
  first = input("First Word:\t").lower().strip()
  second = input("Second Word:\t").lower().strip()
  third = input("Third Word:\t").lower().strip()
  name = input("Lastly, What is your name?\t")

  replit.clear()

  guess = input(f"Enter a word you think {name} associates with the topic {topic}:\t").lower().strip()
  if guess in [first, second, third]:
    print("You actually got it, maybe you are telepathic")
    score+=1
  else:
    print(f"Wrong, the right awnsers were {first}, {second}, {third}")
  input("\nPress enter to continue")
replit.clear()
print(f"\nGAME OVER:\n SCORE:\t{score}\n   {score}/{len(wordlist)}")

