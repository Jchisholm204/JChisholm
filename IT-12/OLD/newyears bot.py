#new years countdown bot
#Author: jChisholm204
#Date: 2021-05-17
from datetime import datetime
from datetime import timedelta

now   = datetime.now()
futdate = datetime.fromtimestamp(1641024001)
leftOver = futdate - now
print (leftOver)