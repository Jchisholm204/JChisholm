#Bubble Sort
#Author: jChisholm204
#Date: 2021-05-14

def bubbleSort(arr):
  n=len(arr)
  for i in range(0, n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1] :
        arr[j], arr[j+1] = arr[j+1], arr[j]

test = [3, 7, 9, 12, 1, 2, 6, 4]
bubbleSort(test)
print(test)