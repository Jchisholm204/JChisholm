#DUM
#Author: jChisholm204
#Date: 2021-05-12
import random
import time
def chungus():
  amerianlist = ["bruger", "pizza", "fries"]
  americanPlaces = ["whitespot", "mcDonalds", "dominos", "chupacabra"]
  canadianlist = ["pancakes", "surup", "poutine"]
  canadianPlaces = ["Tim Hortons", "whistler"]
  drinkList = ["coffee", "ice tea", "soda"]
  reply = input("Hya, What Kind of Food do you like\t").lower().strip("!@#$%^&*()_-+=?/.>,<")
  if reply == "pineapple":
    print("BINEAPPLE BOIZ")
  elif reply in amerianlist:
    print(f"nice, I like {reply.lower()} as well, the best place to get some is {random.choice(americanPlaces)}.")
  elif reply in canadianlist:
    print(f"nice, I like {reply.lower()} as well, the best place to get some is {random.choice(canadianPlaces)}.")
  elif reply in drinkList:
    print(f"nice, I like {reply.lower()} as well, the best place to get some is Tim Hortons. Not Starbucks. Dont go to Starbucks. They charge way to much.")
  else:
    print(f"what the hell kind of food is {reply}")
  return 1
while 1:
  chungus()
  print("\n")