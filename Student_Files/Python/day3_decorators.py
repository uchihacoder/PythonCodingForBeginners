# facilitates aspect oriented programming (AOP); limited ability to implement decorator pattern


class my_decorator(object):
    """decorator class."""
    # required -- must take in the function -- only called once, regardless of how many times we call decorated func

    def __init__(self, function):
        print("__init__ called\n")
        self.__function = function

    # required -- necessary to allow us to "wrap" functionality around (before and/or after) the function call
    def __call__(self):
        print("my_decorator: before my_function()")
        self.__function()
        print("my_decorator: after my_function()")


class another_decorator(object):
    """ a second decorator class"""

    def __init__(self, function):
        print("__init__ called\n")
        self.__function = function

    def __call__(self):
        print("another_decorator: before my_function()")
        self.__function()
        print("another_decorator: after my_function()")


@my_decorator
@another_decorator
def my_function():
    print("Inside my_function")


my_function()

my_function()
