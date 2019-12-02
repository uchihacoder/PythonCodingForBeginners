# Solutions/Logic/logic.py
#

print("Odd numbers: ", end="")
for i in range(1, 11):
    if i % 2 != 0:
        print("{:d} ".format(i), end="")
print()

# Alternative loop.

print("Odd numbers: ", end="")
for i in range(1, 11, 2):
    print("{:d} ".format(i), end="")
print()

print("Even numbers: ", end="")
for i in range(1, 11):
    if i % 2 == 0:
        print("{:d} ".format(i), end="")
print()

# Alternative loop.

print("Even numbers: ", end="")
for i in range(2, 11, 2):
    print("{:d} ".format(i), end="")
print()


