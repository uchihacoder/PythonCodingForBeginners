# Labs/Exceptions/RegistrationEvent.py
#

from Event import Event

class RegistrationEvent(Event):

    def __init__(self, date, endDate, description):
        super(RegistrationEvent, self).__init__(date, description)
        self.endDate = endDate

    @property
    def endDate(self):
        return self.__endDate

    @endDate.setter
    def endDate(self, value):
        self.__endDate = value

    @endDate.deleter
    def endDate(self):
        del self.__endDate
