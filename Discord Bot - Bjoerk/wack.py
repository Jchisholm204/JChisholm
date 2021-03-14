from datetime import datetime

first = datetime.fromtimestamp(1615676456.085404)
second = datetime.fromtimestamp(1615676459.795775)
diff = second - first
sofarts = 1545730073
sofar = datetime.fromtimestamp(sofarts)
toltal = diff + sofar

#timespent = datetime.fromtimestamp(diff)
print(toltal)