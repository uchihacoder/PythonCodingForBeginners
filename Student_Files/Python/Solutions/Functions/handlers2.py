# Solutions/Functions/handlers2.py
#

def handlerOne():
    print("handlerOne called")

def handlerTwo():
    print("handlerTwo called")

def handlerThree():
    print("handlerThree called")

def handlerFour():
    print("handlerFour called")

handlers = []

def register( *args):
    if (args):
        for f in args:
            handlers.append( f)

def notify():
    for f in handlers:
        f()

register( handlerOne, handlerTwo, handlerThree)
register( handlerFour, handlerThree)
register( handlerTwo)

notify()
