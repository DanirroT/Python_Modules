from datetime import datetime, date

# Current date + time
now = datetime.now()
print(now, now.__class__)  # 2026-02-28 19:34:12.123456

# Current date only
today = date.today()
print(today, today.__class__)  # 2026-02-28

print()

"""
Code    Meaning
%Y      Full year       (2026)
%y      minimized year  (26)
%m      Month           (01 to 12)
%d      Day
%H      Hour            (24h)
%M      Minute
%S      Second
"""

# formating
print(now.strftime("%-%m-%d"))
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%H:%M:%S"))

print(now.strftime("%d/%m/%Y %H:%M"))

print()

# number of seconds since epoc (01-01-1970)
timestamp = now.timestamp()
print(timestamp)
timestamp_int = int(now.timestamp())
print(timestamp_int)

print()

# date to int
date_int = int(now.strftime("%Y%m%d"))
print(date_int)

# number of days since 01/01/0001 (ordinal)
ordinal = today.toordinal()
print(ordinal)

print()

# convert timestamp to time
dt = datetime.fromtimestamp(timestamp)
print(dt)

# convert format_int to time
date_int = 20260228
dt = datetime.strptime(str(date_int), "%Y%m%d")
print(dt)

# convert ordinal to time
d = date.fromordinal(ordinal)
print(d)

# convert inputs to time
dt = datetime(2026, 2, 28, 19, 30)
print(dt)

# convert format_str to time
date_str = "10/03/2026 21:30"
dt = datetime.strptime(date_str, "%d/%m/%Y %H:%M")

print()

# time comparason
if dt > datetime.now():
    print("Future date")

# all works thesame with date
day = date(2026, 2, 28)
print(day)
