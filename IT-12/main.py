#spotify data
#Author: jChisholm204
#Date: 2021-06-22

import csv

SpotifyFile = open("spotify.csv","r")
data = list(csv.reader(SpotifyFile))

artist = 'Drake'
factor = 2

print(f'Artist:\t{artist}\nRating Factor:\t{data[0][factor]}\n\nSong Name + {data[0][factor]}')

songsBY = []
rating = []

for i in range(len(data)):
  if data[i][16] == artist:
    songsBY += [data[i][15]]
    rating += [float(data[i][factor])]

n=len(rating)
for i in range(0, n):
  for j in range(0, n-1):#-i
    if rating[j] < rating[j+1]:
      rating[j], rating[j+1] = rating[j+1], rating[j]
      songsBY[j], songsBY[j+1] = songsBY[j+1], songsBY[j]

for f in range(len(songsBY)):
  print(songsBY[f],rating[f])