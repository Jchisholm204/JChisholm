#greenscreen an image
#Author: jChisholm204
#Date: 2021-06-14
from PIL import Image
from colorFunctions import is_green as ig
green_pix = 0
color_pix = 0

beach =  Image.open("ySbtj.png")
boi = Image.open("image2.jpg")

#load image pix data as an array
boi_pix = boi.load()
beach_pix = beach.load()
#get pix array x and y max vals
width, height = boi.size

for x in range(width):
  for y in range(height):
    r, g, b = boi_pix[x, y]
    if ig(r, g, b) == True:
      green_pix += 1
      boi_pix[x, y] = beach_pix[x, y]
    else:
      #debug by printing all non green pix in boi image
      color_pix += 1
      print([r, g, b])

boi.save("product2.jpg")
print(f'Green Pixels: {green_pix}')
print(f'Color Pixels: {color_pix}')