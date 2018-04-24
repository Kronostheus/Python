import datetime

# at first I considered brute force but then remembered there's probably a library for dates
def getSundays():
    total = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            # get weekday of the first day of the month, if it's Sunday update counter
            if datetime.date(year, month, 1).weekday() == 6: total += 1
    return total

print(getSundays())