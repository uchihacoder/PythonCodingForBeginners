# Solutions/Exceptions/Internet.py
#

from Product import *
class Internet (Product):
    def __init__(self, prodNo, price, desc, speed):
        self.setProdNo( prodNo)
        self.setPrice( price)
        self.__desc = desc
        self.__speed = speed

    def __str__(self):
        return "{}: price={}, desc={}, package={}".format( self.getProdNo(),
                self.getPrice(), self.__desc, self.__speed)

    def verify(self):
        print("Verifying the speed is : {} Mbs".format(self.__speed))