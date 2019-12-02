import datetime
#print(help(dir(datetime)))

# Get today's date
today1 = datetime.datetime.today()
print( today1)

today2 = datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
print (today2)

firstDay = today2 - datetime.timedelta(today2.day - 1)
print (firstDay)

############### More ###################
# Get today's date

today = datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
print (today)

# Calculate the first day of the month

firstDay = today - datetime.timedelta(today.day - 1)
print (firstDay)

# Calculate the first Sunday on the calendar; this could be in the previous month.

firstSunday = firstDay - datetime.timedelta((0 if (firstDay.weekday() == 6) else (firstDay.weekday() + 1)))
print (firstSunday)

# Calculate the last day of the month using calendar

import calendar

lastDay = firstDay + datetime.timedelta(calendar.monthrange(firstDay.year,
                                                             firstDay.month)[1] - 1)
print (lastDay)

# Adjust to the last Saturday of the calendar.

lastSaturday = lastDay + datetime.timedelta(6 if (lastDay.weekday() == 6) else (5 - lastDay.weekday()))
print (lastSaturday)

# Print out each day of the calendar.

currentDay = datetime.datetime(firstSunday.year, firstSunday.month, firstSunday.day)

while (currentDay <= lastSaturday):
    print(" {:2d}".format(currentDay.day), end=" ")
    if (currentDay.weekday() == 5):
        print ('')
    currentDay = currentDay + datetime.timedelta(days=1)

# What would have happened to firstSunday if we just assigned firstSunday to currentDay?

