import datetime
date = datetime.date.today()
print(date)
time = datetime.datetime.now()
print(time)
print(date.weekday())
delta_time = datetime.timedelta(days=1222)
print(date - delta_time)