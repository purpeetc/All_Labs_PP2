from datetime import datetime, timedelta
import datetime

today = datetime.datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + 1

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)