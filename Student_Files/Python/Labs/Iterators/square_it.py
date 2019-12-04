numbers = range(1, 51)

even_numbers = [number for number in numbers if number % 2 == 0]

print(f"even numbers: {even_numbers}")

# print(numbers)

# squares = [number ** 2 for number in numbers]

# for square in squares:
#     print(square, end=" ")

squared_even_numbers = [number ** 2 for number in even_numbers]

for se in squared_even_numbers:
    print(se, end=" ")
