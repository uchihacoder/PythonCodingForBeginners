# Solutions/Exceptions/Cable.py
#

from Product import *
class Cable (Product):
    def __init__(self, prodNo, price, desc, packages):
        self.setProdNo( prodNo)
        self.setPrice( price)
        self.__desc = desc
        self.__packages = packages

    def __str__(self):
        return "{}: price={}, desc={}, packages={}".format( self.getProdNo(),
                self.getPrice(), self.__desc, self.__packages)

    def verify(self):
        print("Verifying the following packages: ", end=" ")
        for package in self.__packages:
            print("'" + package + "'", end=" ")
        print()