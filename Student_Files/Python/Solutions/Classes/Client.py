# Solutions/Classes/Client.py
#

from ShoppingCart import *
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