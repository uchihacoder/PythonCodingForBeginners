# Solutions/Generators/SquareIt.py
#
print("\nshow squares")
nbrs = (n**2 for n in range(0,50))
for n in nbrs:
    print(n, end=' ')
print()

print("\nshow squares of even numbers")
nbrs = (n**2 for n in range(0,50) if (n%2==0))
for n in nbrs:
    print(n, end=' ')
print()