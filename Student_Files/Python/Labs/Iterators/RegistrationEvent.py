# Labs/Iterators/RegistrationEvent.py
#

from Event import Event
from IllegalArgumentException import IllegalArgumentException

class RegistrationEvent(Event):

    def __init__(self):
        pass

    @classmethod
    def mixin(cls, obj):
        self = cls()
        for name in obj:
            if (name.startswith("_") == False):
                setattr(self, name, obj[name])
        return self

    @property
    def endDate(self):
        return self.__endDate

    @endDate.setter
    def endDate(self, value):
        self.__endDate = value

    @endDate.deleter
    def endDate(self):
        del self.__endDate
