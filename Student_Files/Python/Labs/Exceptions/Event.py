# Labs/Exceptions/Event.py
#

class Event:

    def __init__(self, date, description):
        self.date = date
        self.description = description

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        self.__date = value

    @date.deleter
    def date(self):
        del self.__date

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @description.deleter
    def description(self):
        del self.__description