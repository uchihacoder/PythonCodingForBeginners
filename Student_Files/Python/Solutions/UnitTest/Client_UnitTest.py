# Solutions/Exceptions/Client.py
#

from ShoppingCart import *
from Internet import *
from Cable import *
from Phone import *
from Product import *
from ProductFactory import ProductFactory
import unittest

cart = ShoppingCart('Tony Stark')
ProductFactory.insertDBProducts()
products = ProductFactory.queryDBProducts()
#products = ProductFactory.getProducts()
print('='*10)
print(len(products));
print('='*10)

for p in products:
    try:
        cart.addProduct( p)
    except IllegalArgumentException as e:
        print("Recieved IllegalArgumentException exception: " + str(e))

# list the Employees
#print('\nList Products:')
cart.listProducts()

# Calulate the total Price
print('\nTotal Price: {}'.format( cart.getTotal()))

# verify the Products
print('\nVerify Products:')
cart.verifyProducts()

class ClientTest( unittest.TestCase ):
    def testProductLen( self ):
        self.assertEqual( len(products), 5)
    def testTotal( self ):
        self.assertEqual( cart.getTotal(), 325.5 )

if __name__ == '__main__':
    unittest.main()