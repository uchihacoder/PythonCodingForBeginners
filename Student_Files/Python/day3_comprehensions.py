numbers = [1, 3, 5, 8, 13, 20, 40, 100]

double_numbers = [number * 2 for number in numbers]

print(double_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# filtered list comprehension -- if is the filter
even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)

# nesting a comprehension within another comprehension
double_even_numbers = [number * 2 for number in even_numbers]

print(double_even_numbers)

# similar to JavaScript destructuring -- you can map the individual values to a tuple
number_pairs = [[10.0, 2.0], [30.0, .4], [500.0, 6.0]]

first_number_in_pair = [f for (f, s) in number_pairs]
second_number_in_pair = [s for (f, s) in number_pairs]

print(first_number_in_pair)
print(second_number_in_pair)

convert_to_tuples = [(x, y) for (x, y) in number_pairs]

print(convert_to_tuples)

convert_to_dictionaries = [
    {"price": format(x, ".2f"), "tax": format(y, ".2f")} for (x, y) in number_pairs]

print(convert_to_dictionaries)
