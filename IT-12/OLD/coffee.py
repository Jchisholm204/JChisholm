#best coffee place
#Author: jChisholm204
#Date: 2021-05-17
import csv
import time
import replit
def ask():
  print("Whats the best place to get coffee?")
  print("1.\tStarbucks")
  print("2.\tTim Hortons")
  print("3.\tOther")
  respo = input("Awnser:\t")
  with open("bungus.csv", "a") as fp:
    writer = csv.writer(fp)
    writer.writerow(respo)
  return 1
for i in range(0, 10):
  ask()
  time.sleep(0.25)
  replit.clear()
starbucks = 0
tim_Hortons = 0
other = 0
with open("bungus.csv", "r") as fd:
  data = list(csv.reader(fd))
  for row in data:
    if row == ['1']:
      starbucks +=1
    if row == ['2']:
      tim_Hortons +=1
    if row == ['3']:
      other +=1
print(f"Starbucks: {int(starbucks/len(data)*100)}%, Tim Hortons: {int(tim_Hortons/len(data)*100)}%, Other: {int(other/len(data)*100)}%")
if starbucks > tim_Hortons and starbucks > other:
  overall = "Starbucks"
elif tim_Hortons > starbucks and tim_Hortons > other:
  overall = "Tim Hortons"
elif other > tim_Hortons and other > starbucks:
  overall = "Other"
else:
  overall = "There Was a Tie! ie I win and its Tim Hortons"
print(f"Overall Best Place: {overall}") 