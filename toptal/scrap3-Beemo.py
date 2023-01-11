# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import calendar
from datetime import datetime as dt2, timedelta


def solution(Y, A, B, W):
    # Ends on the last day of the ending month
    # Plane departs on Monday and arrives on Sunday
    month = dt2.strptime(A, '%B').month
    # So given a day, the first, find the first monday
    first = dt2(Y, month, 1)
    # monday is 0
    # import calendar
    # calendar.day_name[first.weekday()]
    weekday = first.weekday()
    # Monday is 0 (same as 7), so add up to 7
    if weekday is not 0:
        days_away = 7 - weekday
    else:
        days_away = 0
    start = first + timedelta(days=days_away)
    month = dt2.strptime(B, '%B').month
    weekday, days_in_month = calendar.monthrange(Y, month)
    last = dt2(Y, month, days_in_month)
    # monday is 0
    # import calendar
    # calendar.day_name[first.weekday()]
    weekday = last.weekday()
    # Sunday is 6 (same as -1)
    if weekday is not 6:
        days_away = -1 - weekday
    else:
        days_away = 0
    end = last + timedelta(days=days_away)
    total_days = (end - start).days + 1
    weeks = total_days / 7
    print(weeks)
    return int(weeks)


# Question was something like
# Imagine you are planning a trip, find the exact date to leave and arrive on if you want to leave on the first monday
# of the month, and the last monday of the month

iis = [(2021, 'March', 'April', ''),
       (2001, 'March', 'April', ''),
       (2002, 'March', 'July', ''),
       (2003, 'January', 'July', ''),
       (2099, 'January', 'April', '')]

for i in iis:
    # Y, A, B, W = (2021, 'March', 'April', 'not used')
    answer = solution(*i)
    # assert answer
# print(answer)
