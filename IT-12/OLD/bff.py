#Quote Generator
#Author: jChisholm204
#Date: 2021-05-05
import random
import time
import csv
myData = ["Jacob Chisholm","Tim Horton's","Dominos","Booster Juice","The Keg","McDonald's"]
simm = 0            
bff = ""
tsim = 0
with open("cp.csv", "r") as fp:
  for row in fp:
    data = row.split(",")
    #print(data[1],tsim)
    tsim = 0
    for q in data:
      if q in myData:
        tsim += 1
      if tsim > simm:
        bff = data[1]
        simm = tsim
    print(data[1],tsim)
print(f"Best Match: {bff} ")