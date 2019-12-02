#A decoration is a way to specify management or augmentation code for functions and classes
#A decorator is a callable that returns a callable.

#EXAMPLE 1: Wrapper spam wraps around the call to sing and prints "hellox10" 10xs
def spam( func) :
    def wrapper( *args, **kwargs) :     #args=regular arguments
        for i in range(10) :            #kwargs=keyword arguments
            func( *args, **kwargs)
    return wrapper

@spam                           #decorate metafunction
def sing1(line) :               # ==> func = spam(sign1)
    print (line + " ", end="")

sing1("hellox10")
print()

#EXAMPLE 2: Decorator with argument - Wrapper spam wraps around the call to sing and prints "howdyx20" 20xs
def spam2( repeats) :
    def decorator( func) :
        def wrapper( *args, **kwargs) :
            for i in range(repeats) :
                func( *args, **kwargs)
        return wrapper
    return decorator

@spam2(20)
def sing2(line) :
    print (line + " ", end="")

sing2("howdyx20")
print()

def myDecorator2( func ):
    def onCall( *args, **kwargs):
        print("myDecorator: before {}".format(func.__name__))
        rc = func( *args, **kwargs)
        print("myDecorator: after {}".format(func.__name__))
        return rc
    return onCall

@myDecorator2
def myFunction():
    print("inside myFunction()")

myFunction()
myFunction()