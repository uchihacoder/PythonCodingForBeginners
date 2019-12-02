import sys, timer

reps = 10000
repsList = list(range(reps))

def forLoop():
    res = []
    for x in repsList:
        res.append(abs(x))
    return res

def listComp():
    return [abs(x) for x in repsList]

def mapCall():
    return list( map( abs, repsList))   # 3.x
    #return map(abs, repsList)          #2.5+

def genExpr():
    return list(abs(x) for x in repsList)

def genFunc():
    def gen():
        for x in repsList:
            yield abs(x)
    return list(gen())

print(sys.version)

for test in (forLoop, listComp, mapCall, genExpr, genFunc):
        (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
        print ('%-9s: %.5f ==> [%s...%s]' % 
               ( test.__name__, bestof, result[0], result[-1]))