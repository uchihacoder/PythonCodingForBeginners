# Solutions/Classes/Client.py
#

from ShoppingCart import ShoppingCart
from Product import Product
from ProductFactory import ProductFactory
from IllegalArgumentException import IllegalArgumentException

cart = ShoppingCart('Tony Stark')
# products = ProductFactory.getProducts()
products = ProductFactory.queryDBProducts()

for p in products:
    try:
        cart.addProduct(p)
    except IllegalArgumentException as e:
        print(f"Received IllegalArgumentException exception: {str(e)}")

# list the Employees
print('\nList Products:')
cart.listProducts()

# Calulate the total Price
print('\nTotal Price: {}'.format(cart.getTotal()))
