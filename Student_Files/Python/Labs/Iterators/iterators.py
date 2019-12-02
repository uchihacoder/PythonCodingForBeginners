# Labs/Iterators/iterators.py
#

import datetime
import json
from Event import Event
from RegistrationEvent import RegistrationEvent
from IllegalArgumentException import IllegalArgumentException

def getEvents():

    # Read event dates and descriptions into a dictionary of events.

    events = {}
    eventData = open("events.data", "r")

    for line in eventData:

        rawEvent = json.loads(line)
        event = None

        if "date" in rawEvent:
            rawEvent["date"] = datetime.datetime.strptime(rawEvent["date"], "%x").date()

        if "endDate" in rawEvent:
            rawEvent["endDate"] = datetime.datetime.strptime(rawEvent["endDate"], "%x").date()

            try:
                event = RegistrationEvent.mixin(rawEvent)

            except IllegalArgumentException as e:
                print(e)
        else:
            event = Event.mixin(rawEvent)

        if event != None:
            events[event.date] = event

    return events
