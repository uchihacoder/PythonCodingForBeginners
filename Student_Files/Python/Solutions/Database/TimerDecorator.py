import time
#timer = time.clock() if sys.platform[:3] == 'win' else time.time()

def TimerDecorator( func ):
    def onCall( *args, **kwargs):
        start = time.clock()
        rc = func( *args)
        elapsed = time.clock() - start
        print("TimerDecorator: elapsed time for {} is {:6.4f} seconds".format(func.__name__, elapsed))
        return rc
    return onCall
