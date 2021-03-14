from datetime import datetime
import datetime
#0000000000.000000
#first = datetime.fromtimestamp(1615676456.085404)
#second = datetime.fromtimestamp(1615676459.795775)
#diff = second - first
sofarts = 1545730073
#sofar = datetime.fromtimestamp(sofarts)
bum = "87500"
print('bum: ',bum)
#hum = datetime.strptime(bum, "%Y-%m-%d %H:%M:%S.%f")
hum = datetime.timedelta(seconds=float(bum)) #days=(bum/86400), hours= (bum/3600), 
print('hum: ',hum)
#toltal = diff + sofar

#timespent = datetime.fromtimestamp(diff)
#print('dum: ', dum)