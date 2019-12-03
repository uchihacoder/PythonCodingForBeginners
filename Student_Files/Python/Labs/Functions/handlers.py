handler_functions = []


def handlerOne():
    print("handlerOne called")


def handlerTwo():
    print("handlerTwo called")


def handlerThree():
    print("handlerThree called")


def handlerFour():
    print("handlerFour called")


def register(*handler_funcs):
    handler_functions.extend(handler_funcs)


def notify():
    for handler in handler_functions:
        handler()


register(handlerOne, handlerTwo, handlerThree)

notify()
