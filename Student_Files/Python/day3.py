from functools import reduce
nbrs = [ -1, 2, -3, 7, -8, 2, 15, -2, 5]
pnbrs = list(filter( lambda n : n > 0, nbrs))
print(pnbrs)

dnbrs = [n*2 for n in nbrs]
print(dnbrs)
dnbrs = list(map( lambda n: n*2, nbrs))
print(dnbrs)

total = reduce( lambda a, b: a+b, nbrs)
print(total)