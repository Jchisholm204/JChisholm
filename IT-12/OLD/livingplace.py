#liveing place
#Author: jChisholm204
#Date: 2021-05-17
import math
toltalScore = 0
print("This tool will help you rate a city.")
city = input("What city would you like to rate?\n")
print("Please rate the following things on a scale of 1 to 10")
questions = ["Weather:", "Housing:", "Saftey", "Public services"]
for question in questions:
  rating = int(input(question+"\t").strip("%"))
  importance = int(input("How important is this to you?\t"))
  toltalScore += (rating/2) * (importance/2)
print(f"{toltalScore}%")
print(str(int(math.sqrt(toltalScore)))+"/10")