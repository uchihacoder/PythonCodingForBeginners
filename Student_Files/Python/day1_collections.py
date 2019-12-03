def print_info(numbers):
    print(id(numbers), type(numbers), numbers)


# list -- ordered, mutable; allows duplicates
a = [12, 23, 74, 92, 12, 74, 74]
print_info(a)

# tuple -- ordered, read-only -- immutable; good way to prevent it from being overwritten
b = tuple(a)
print_info(b)

# set -- unordered, mutable; removes duplicates
c = set(a)
print_info(c)

# dictionary -- unordered, mutable; key value pairs
d = {"FL": "Florida", "WA": "Washington", "NY": "New York"}
print(f"states: {d}")
print(f"states keys: {d.keys()}")
print(f"states values: {d.values()}")
