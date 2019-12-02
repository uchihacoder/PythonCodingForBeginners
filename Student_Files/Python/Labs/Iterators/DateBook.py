# Labs/Iterators/DateBook.py
#

import datetime
import time

class DateBook:

    def __init__(self, monthDate, events):
        self.monthDate = monthDate
        self.events = events
        self.__viewStartDate = self.__getFirstViewDate()
        self.__viewEndDate = self.__getLastViewDate()

    @property
    def events(self):
        return self.__events

    @events.setter
    def events(self, value):
        self.__events = value

    @events.deleter
    def events(self):
        del self.__events

    @property
    def monthDate(self):
        return self.__monthDate

    @monthDate.setter
    def monthDate(self, value):
        self.__monthDate = value

    @monthDate.deleter
    def monthDate(self):
        del self.__monthDate

    def __getFirstViewDate(self):

        # Determine the first date to display. Get the first day of the month, and then move backward
        # to the Sunday.

        monthStartDate = datetime.date(self.monthDate.year, self.monthDate.month, 1)
        return monthStartDate - datetime.timedelta(monthStartDate.isoweekday() % 7)

    def __getLastViewDate(self):

        # Find the last day of the month to display by getting the first day of the next month and backing up one day.

        month = self.monthDate.month % 12 + 1;
        if (month == 1):
            year = self.monthDate.year + 1
        else:
            year = self.monthDate.year

        monthEndDate = datetime.date(year, month, 1) - datetime.timedelta(1)

        # Get the last date to display.

        return monthEndDate + datetime.timedelta(6 - (monthEndDate.isoweekday() % 7))

    def renderCalendarView(self):

        # Add all of the days in the view to a list.

        currentDate = self.__viewStartDate
        today = datetime.date.today()
        oneDay = datetime.timedelta(1)

        print("\033[0;37m")

        while (currentDate <= self.__viewEndDate):
            for d in range(0, 7):
                if currentDate.month == self.monthDate.month and currentDate.day == 1:
                    print("\033[0m", end="")
                if currentDate == today:
                    print("\033[1m", end="")
                print("{:>2d}".format(currentDate.day), end="")
                if currentDate == today:
                    print("\033[0m", end="")
                if self.events.get(currentDate) != None and self.events.get(currentDate).date == currentDate:
                    print("* ", end="")
                else:
                    print("  ", end="")
                currentDate = currentDate + oneDay
                if currentDate.month != self.monthDate.month and currentDate.day == 1:
                    print("\033[0;37m", end="")
            print("")
        print("\033[0m")
