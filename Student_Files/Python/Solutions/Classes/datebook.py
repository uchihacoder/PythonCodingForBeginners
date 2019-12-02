# Solutions/Classes/datebook.py
#

import datetime
import time

def getEvents():

    # Read event dates and descriptions into a dictionary of events.

    events = {}

    while True:
        eventDateString = input("Please enter a date for the event in the form MM/DD/YY: ")
        if eventDateString == "":
            break;
        eventDescription = input("Please enter a description for the event: ")
        eventDate = datetime.datetime.strptime(eventDateString, "%x").date()
        events[eventDate] = eventDescription

    return events

def buildCalendar(monthDate, events):
    viewStartDate = getFirstViewDate(monthDate)
    viewEndDate = getLastViewDate(monthDate)
    print(viewStartDate, viewEndDate, monthDate)
    renderCalendarView(viewStartDate, viewEndDate, monthDate, events)

def getFirstViewDate(monthDate):

    # Determine the first date to display. Get the first day of the month, and then move backward
    # to the Sunday.

    monthStartDate = datetime.date(monthDate.year, monthDate.month, 1)
    return monthStartDate - datetime.timedelta(monthStartDate.isoweekday() % 7)

def getLastViewDate(monthDate):

    # Find the last day of the month to display by getting the first day of the next month and backing up one day.

    month = monthDate.month % 12 + 1;
    if (month == 1):
        year = monthDate.year + 1
    else:
        year = monthDate.year

    monthEndDate = datetime.date(year, month, 1) - datetime.timedelta(1)

    # Get the last date to display.

    return monthEndDate + datetime.timedelta(6 - (monthEndDate.isoweekday() % 7))

def renderCalendarView(viewStartDate, viewEndDate, monthDate, events):

    # Add all of the days in the view to a list.

    currentDate = viewStartDate
    today = datetime.date.today()
    oneDay = datetime.timedelta(1)

    print("\033[0;37m")

    while (currentDate <= viewEndDate):
        for d in range(0, 7):
            if currentDate.month == monthDate.month and currentDate.day == 1:
                print("\033[0m", end="")
            if currentDate == today:
                print("\033[1m", end="")
            print("{:>2d}".format(currentDate.day), end="")
            if currentDate == today:
                print("\033[0m", end="")
            if (events.get(currentDate) != None):
                print("* ", end="")
            else:
                print("  ", end="")
            currentDate = currentDate + oneDay
            if currentDate.month != monthDate.month and currentDate.day == 1:
                print("\033[0;37m", end="")
        print("")
    print("\033[0m")

# Ask the user for a date.

while True:

    displayDate = input("Please enter a date in the form MM/DD/YY: ")

    if displayDate == "":
        break;

    monthDate = datetime.datetime.strptime(displayDate, "%x").date()

    events = getEvents()
    buildCalendar(monthDate, events)
