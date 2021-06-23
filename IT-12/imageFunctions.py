#ColorFunctions
#Author: jChisholm204
#Date: 2021-06-14
from PIL import Image
def is_green(r, g, b): #determines if a pixel is green
  filter_value = 180 #red and blue pix val must be lower than this for it to be green #120
  if r <= filter_value and r >= 0 and g>100 and g <= 255 and b <= filter_value and b >= 0: #140
    return True
  else:
    return [r, g, b]

def findRGB(r, g, b): #determines if a pixel is green
  filter_value = 120 #red and blue pix val must be lower than this for it to be green #120
  if r <= filter_value and r >= 0 and g>140 and g <= 255 and b <= filter_value and b >= 0: #140
    return 'green'
  if g <= 180 and g >= 0 and r>100 and r <= 255 and b <= 180 and b >= 0: #140
    return 'red'
  if r <= filter_value and r >= 0 and b>140 and b <= 255 and g <= filter_value and g >= 0: #140
    return 'blue'
  else:
    return False


def findYellow(r, g, b):
  if r > 150 and g > 110 and b < 20:
    return True
  else:
    return False

def findBlue(r, g, b):
  if r < 120 and g < 120 and b > 50:
    return True
  else:
    return False

def findGreen(r, g, b):
  if r < 80 and g > 50 and b < 80:
    return True
  else:
    return False

def isLight(r, g, b):
  if (r+g+b)/3 > 128:
    return True
  else:
    return False

#invert an images colors
def colorInvert(imageLoad):
  #load the image
  image = Image.open(imageLoad)

  #load image pix data as an array
  image_pix = image.load()
  #get pix array x and y max vals
  width, height = image.size

  for x in range(width):
    for y in range(height):
      r, g, b = image_pix[x, y]
      image_pix[x, y] = int(255-r), int(255-g), int(255-b)

  image.save(f'Inverted_{imageLoad}')
  return f'Inverted_{imageLoad}'

def greyScale(imageLoad):
  #load the image
  image = Image.open(imageLoad)

  #load image pix data as an array
  image_pix = image.load()
  #get pix array x and y max vals
  width, height = image.size

  for x in range(width):
    for y in range(height):
      r, g, b = image_pix[x, y]
      newColor = int((r+g+b)/3)
      image_pix[x, y] = newColor, newColor, newColor

  image.save(f'GreyScale_{imageLoad}')
  return f'GreyScale_{imageLoad}'

def blackScale(imageLoad):
  #load the image
  image = Image.open(imageLoad)

  #load image pix data as an array
  image_pix = image.load()
  #get pix array x and y max vals
  width, height = image.size

  for x in range(width):
    for y in range(height):
      r, g, b = image_pix[x, y]
      if isLight(r, g, b) == True:
        image_pix[x, y] = 255, 255, 255
      else:
        image_pix[x, y] = 0, 0, 0

  image.save(f'BlackScale_{imageLoad}')
  return f'BlackScale_{imageLoad}'