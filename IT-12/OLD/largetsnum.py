#max num in a list
#Author: jChisholm204, aryanmp
#Date: 2021-06-02
ls = []
maxnum = 0
for i in range(0, 5):
  ls.append(int(input("Enter a Number:\t")))
for num in ls:
  if num > maxnum:
    maxnum = num
print(f'Biggest Number:\t{maxnum}')