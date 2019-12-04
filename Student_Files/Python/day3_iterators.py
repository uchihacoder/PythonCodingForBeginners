numbers = range(-5, 6)

# for number in numbers:
#     print(number, end=" ")

iterator = iter(numbers)

# first item from the list:  -5
item = next(iterator)
print(item)

# second item from the list:  -4
item = next(iterator)
print(item)
