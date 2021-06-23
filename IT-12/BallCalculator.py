#ball location calculator
#Author: jChisholm204, aryanmp
#Date: 2021-06-21
#378, 185
import imageFunctions as imWorks
from PIL import Image as imUtils
import time

t0 = time.time()

IMG = imUtils.open('kidball.png')
imArray = IMG.load()

t1 = time.time() - t0

width, height = IMG.size
print(f'Image Width: {width}, Height: {height}')

PixLasR = False

rightChords = [0, 0]
leftChords = [9999, 9999]

for x in range(260, 520):
  for y in range(0, 300):
    r, g, b = imArray[x, y]
    rl, gl, bl = imArray[x, y-1]
    if rl > 200 and gl > 200 and bl > 200:
      PixLasR = False
    if imWorks.findRGB(r, g, b) == 'red':
      imArray[x,y] = 0, 0, 0
      if PixLasR == True and x >= rightChords[0]:
        rightChords = [x, y]
      if PixLasR == False and x <= leftChords[0]:
        leftChords = [x, y]
      PixLasR = True

t2 = ((time.time() - t0) - t1)

rx, ry = rightChords
lx, ly = leftChords
imArray[rx, ry] = 0, 0, 255
imArray[lx, ly] = 0, 0, 255
print(f'Left Most Cordanate of Ball: {leftChords}\nRight Most Cordanate of Ball: {rightChords}')
aproxX = (rightChords[0] + leftChords[0])/2
aproxY = (rightChords[1] + leftChords[1])/2
imArray[aproxX, aproxY] = 0, 255, 0
print(f'Ball Aproximate Location: (X,Y)\n{aproxX}, {aproxY}')

t3 = (((time.time() - t0) - t1) - t2)

IMG.save("output.png")

t4 = ((((time.time() - t0) - t1) - t2) - t3)

print('\nPlease refer to the image named "output.png" to see everything the program marked as RED in black, if you zoom in, you should see some blue pixels as well, these are the locations that the program is using to get the location of the ball, lastly there should be a single green pixel in the very center of the ball')
print("\nas you can see, it should be about 3 or 4 pixels lower to be in the exact center, and that is a flaw of this algorithm, the best way to do it would be to average all of the red pixels in the image, that way you would get a perfect center, doing it this way would however take a much longer amount of time to write and compute")
print()
print('Time To:\nOpenImage: {:.3f}s\nCompute Colors: {:.3f}s\nCalculate Center: {:.6f}s\nSave Image: {:.3f}s'.format(t1, t2, t3, t4))
print("Toltal Time:{:.3f}s".format(t1+t2+t3+t4))