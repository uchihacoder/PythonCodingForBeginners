import time
from time import perf_counter
#timer = time.clock() if sys.platform[:3] == 'win' else time.time()

def TimerDecorator( func ):
    def onCall( *args, **kwargs):
        start = perf_counter()
        rc = func( *args)
        elapsed = perf_counter() - start
        print("TimerDecorator: elapsed time for {} is {:6.4f} seconds".format(func.__name__, elapsed))
        return rc
    return onCall
