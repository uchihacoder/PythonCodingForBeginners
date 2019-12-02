# Solutions/Classes/ShoppingCart.py
#

from Product import *

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