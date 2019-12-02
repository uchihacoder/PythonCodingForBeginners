# Solutions/Polymorphism/Client.py
#

from ShoppingCart import *
from Internet import *
from Cable import *
from Phone import *
from Product import *
from ProductFactory import ProductFactory

cart = ShoppingCart('Tony Stark')
products = ProductFactory.getProducts()

for p in products:
    cart.addProduct( p)

# list the Employees
print('\nList Products:')
cart.listProducts()

# Calulate the total Price
print('\nTotal Price: {}'.format( cart.getTotal()))


# verify the Products
print('\nVerify Products:')
cart.verifyProducts()