#im done with life
#Author: jChisholm204
#Date: 2021-05-28

inio = float(input("Enter Height in m:\t"))
incht = inio*39.37
inch = incht%12
feet = int((incht-inch)/12)
inchr = "{:.1f}".format(inch)
print(f'{inio}m is {feet}\' {inchr}\"')