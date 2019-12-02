# Solutions/Functions/handlers1.py
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

def register( f):
    handlers.append( f)

def notify():
    for f in handlers:
        f()

register( handlerOne)
register( handlerTwo)
register( handlerThree)
register( handlerFour)

notify()
