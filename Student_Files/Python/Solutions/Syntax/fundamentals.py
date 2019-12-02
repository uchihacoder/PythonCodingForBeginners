# Solutions/Syntax/fundamentals.py
# This is program needs to be repaired in order to function.
#

x = 6
y = "7"
z = x * y

print("z = ", z)

if z == 42:
    z = z / 3
    print("z = " + z)

x = input("Enter a new value for x: ")
y = input("Enter a new value for y: ")

z = float(x) * float(y)
print("z = ", z)

# Import the datetime module

import datetime

today = datetime.date.today()

print("Today is ", today)
print("The day of the month is ", today.day)
print("The month of the year is ", today.month)
print("The year is ", today.year)
print("The day of the week is ", today.weekday())
