# Solutions/Exceptions/Client.py
#

from ShoppingCart import *
from Internet import *
from Cable import *
from Phone import *
from Product import *
from ProductFactory_BONUS import ProductFactory

carts = ProductFactory.getCartAndProducts()
for c in carts:
    print('-'*60)
    cartName = c[0]
    products = c[1]
    cart = ShoppingCart(cartName)

    for p in products:
        try:
            cart.addProduct( p)
        except IllegalArgumentException as e:
            print("Recieved IllegalArgumentException exception: " + str(e))

    # list the Employees
    print('\n{} - Products:'.format(cartName))
    cart.listProducts()

    # Calulate the total Price
    print('\n{} - Total Price: {}'.format( cartName, cart.getTotal()))

    # verify the Products
    print('\n{} - Verify Products:'.format(cartName))
    cart.verifyProducts()