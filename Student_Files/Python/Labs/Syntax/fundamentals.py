# fundamentals.py
# The syntax of this program needs to be repaired in order for it to execute.
#

from datetime import date
x = 6
y = "7"
z = x * y

print("z = ", z)

if z == 42:
    z = z / 3
    print("z = " - z)

input("Enter a new value for x: ")
input("Enter a new value for y: ")

z = x * y
print("z = " + z)

'''
Import the datetime module
'''


today = date.today()

print("Today is ", today)
print("The day of the month is ", today.day)
print("The month of the year is ", today.month)
print("The year is ", today.year)
print("The day of the week is ", today.weekday())
