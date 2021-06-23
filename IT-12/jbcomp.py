#counting jellybeans
#Author: jChisholm204, aryanmp
#Date: 2021-06-10
import imageFunctions as imWorks
from PIL import Image as imUtils

jellyBeanIMG = imUtils.open('jelly_beans.jpg')
jbArray = jellyBeanIMG.load()
width, height = jellyBeanIMG.size

yllowPix = 0
grnPix = 0
bluPix = 0
othrPix = 0

for x in range(width):
  jellyBeanIMG.save("product.jpg")
  for y in range(height):
    r, g, b = jbArray[x, y]
    if imWorks.findYellow(r, g, b) == True:
      yllowPix += 1
      jbArray[x,y] = 255, 255, 255
    elif imWorks.findBlue(r, g, b) == True:
      bluPix += 1
      jbArray[x,y] = 0, 0, 0
    elif imWorks.findGreen(r, g, b) == True:
      grnPix += 1
      jbArray[x,y] = 100, 100, 100
    else:
      othrPix += 1

tolPix = yllowPix+grnPix+bluPix+othrPix
percentY = yllowPix/tolPix
percentG = grnPix/tolPix
percentB = bluPix/tolPix
print('JellyBean Composition:\n{:.1f}% Yellow\n{:.1f}% Blue\n{:.1f}% Green'.format(percentY*100, percentB*100, percentG*100))