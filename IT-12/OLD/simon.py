def simonSays():
  print("Ok. You go first")
  initil = input("Say something:\n")
  print(initil)
  i=0
  while i < 3:
    sysimon = input()
    print(sysimon)
    i+=1
  wrongAwnser = 0
  print("Ok. Now its my turn.\n")
  simonList = ["ahh", "pineapple", "red", "purple", "william", "door", "wood", "computer", "variable", "projector", "funny"]
  simonOne = random.choice(simonList)
  simonTwo = random.choice(simonList)
  simonThree = random.choice(simonList) 
  respoOne = input(simonOne+"\n")
  if respoOne is not simonOne:
    wrongAwnser +=1
    print("Comon, you can do better than that")
  respoTwo = input(simonTwo+"\n")
  if respoTwo is not simonTwo:
    wrongAwnser +=1
    print("Really. Try harder.")
  respoThree = input(simonThree+"\n")
  if str(respoThree) is not str(simonThree):
    wrongAwnser +=1
    print("Seriously dude?")
  if wrongAwnser >= 2:
    print(f"Your really bad at Simon says.  I mean you got {wrongAwnser} questions wrong")
  return