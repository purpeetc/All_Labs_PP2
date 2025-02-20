from datetime import datetime
import datetime

x = datetime.datetime.now()
drop = x.replace(microsecond = 0)
print("Date and time without microseconds: ", drop)