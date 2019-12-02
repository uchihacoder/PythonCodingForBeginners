# Labs/Exceptions/app.py
#

import datetime
from DateBook import DateBook
from Event import Event
from RegistrationEvent import RegistrationEvent

def getEvents():

    # Read event dates and descriptions into a dictionary of events.

    events = {}

    while True:
        eventDateString = input("Enter a date for the event in the form MM/DD/YY (empty to end): ")
        if eventDateString == "":
            break

        eventEndDateString = input("Enter an end date for the event (empty for none): ")
        eventDescription = input("Enter a description for the event: ")
        eventDate = datetime.datetime.strptime(eventDateString, "%x").date()

        if eventEndDateString != '':
            eventEndDate = datetime.datetime.strptime(eventEndDateString, "%x").date()
            event = RegistrationEvent(eventDate, eventEndDate, eventDescription)
        else:
            event = Event(eventDate, eventDescription)

        events[eventDate] = event

    return events

# Ask the user for a date.

while True:

    displayDate = input("Please enter a date in the form MM/DD/YY: ")

    if displayDate == "":
        break;

    monthDate = datetime.datetime.strptime(displayDate, "%x").date()
    events = getEvents()

    dateBook = DateBook(monthDate, events)
    dateBook.renderCalendarView()
