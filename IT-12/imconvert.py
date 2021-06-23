#convert images
#Author: jChisholm204
#Date: 2021-06-15
import imageFunctions as imWorks
import glob
print("Valid Image Names:\nimage2.jpg\nbeach.jpg\ncolorgrade.png")

#load the image
sample = input("Enter the valid image name of the image you would like to convert:\n")

print("You can find your output images as:")
#for filename in glob.glob('*.jpg'):
  #sample = filename
print(imWorks.greyScale(sample))
print(imWorks.colorInvert(sample))
print(imWorks.blackScale(sample))