import datetime

ts = datetime.datetime.now().replace(
    microsecond=0,
    second=0
)
print(ts) 