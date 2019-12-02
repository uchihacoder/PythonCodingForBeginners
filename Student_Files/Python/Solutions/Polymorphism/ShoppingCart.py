# Solutions/Polymorphism/ShoppingCart.py
#

from Internet import *
from Cable import *
from Phone import *

class ShoppingCart:
    def __init__(self, name):
        self.__name = name
        self.__products = []

    def __str__(self):
        return "name={}, products={}".format( self.__name, self.__products)

    def addProduct(self, p):
        self.__products.append( p)

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
            #if ((type(p) is Cable) or (type(p) is Internet)):
            #    p.verify()
            p.verify()