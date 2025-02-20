from datetime import datetime
time1 = datetime(2007, 4, 3, 10, 0, 0)
time2 = datetime(2007, 4, 3, 10, 6, 40)
difference = time2 - time1
seconds = difference.total_seconds() 
print(seconds)