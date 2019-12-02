# Labs/Iterators/Event.py
#

class Event:

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