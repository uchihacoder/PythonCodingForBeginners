# Solutions/Exceptions/ShoppingCart.py
#

from Internet import *
from Cable import *
from Phone import *
from IllegalArgumentException import *

class ShoppingCart:
    def __init__(self, name):
        self.__name = name
        self.__products = []

    def __str__(self):
        return "name={}, products={}".format( self.__name, self.__products)

    def addProduct(self, p):
        if (self.isValid(p)):
            self.__products.append( p)
        else:
            errMsg = "{} is not allowed to call this method".format(type(p))
            raise IllegalArgumentException( errMsg )

    def removeProduct(self, p):
        self.__products.remove( p)

    def listProducts(self):
        for p in self.__products:
            print(p)

    def getTotal(self):
        total = 0.00
        for p in self.__products:
            total += p.getPrice()
        return total

    def verifyProducts(self):
        for p in self.__products:
            p.verify()

    def isValid(self, p):
        validType = [Cable, Internet, Phone]
        for v in validType:
            if (type(p) is v):
                return True
        return False