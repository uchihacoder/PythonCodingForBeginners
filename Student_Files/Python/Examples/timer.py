import time
#timer = time.clock() if sys.platform[:3] == 'win' else time.time()

def total(reps, func, *pargs, **kargs):
    repsList = list(range(reps))
    #start = timer()
    #start = time.time()
    start = time.clock()
    for i in repsList:
        ret = func(*pargs, **kargs)
    #elapsed = time.time() - start
    elapsed = time.clock() - start
    return (elapsed, ret)

def bestof(reps, func, *pargs, **kargs):
    best = 2 ** 32
    for i in range(reps):
        #start = time.time()
        start = time.clock()
        ret = func(*pargs, **kargs)
        #elapsed = time.time() - start
        elapsed = time.clock() - start
        if elapsed < best: best = elapsed
    return (best, ret)

def bestoftotal( reps1, reps2, func, *pargs, **kargs):
    return bestof( reps1, total, reps2, func, *pargs, **kargs)