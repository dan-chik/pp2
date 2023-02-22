from datetime import datetime, time

def diff_in_sec(d1, d2):
    timedelta = d2 - d1
    return timedelta.days*24*60*60 + timedelta.seconds

d1 = datetime.strptime('2023-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')
d2 = datetime.strptime('2023-02-16 01:00:00', '%Y-%m-%d %H:%M:%S')

print()
print(diff_in_sec(d1, d2))
print()