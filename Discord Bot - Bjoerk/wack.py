from datetime import datetime
#0000000000.000000
first = datetime.fromtimestamp(1615676456.085404)
second = datetime.fromtimestamp(1615676459.795775)
diff = second - first
sofarts = 1545730073
sofar = datetime.fromtimestamp(sofarts)
bum = "1969-12-31 16:00:19.751128"
hum = datetime.strptime(bum, "%Y-%m-%d %H:%M:%S.%f")
dum = datetime.timestamp(hum)
toltal = diff + sofar

#timespent = datetime.fromtimestamp(diff)
print(dum)