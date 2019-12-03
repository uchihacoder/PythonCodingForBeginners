inStr = "12|23|72|238|55|7|23|12|2|23|73|56|23|33|6|7"

string_numbers = inStr.split("|")

numbers = []

for nbr in string_numbers:
    numbers.append(int(nbr))

print(f"numbers: {numbers}")

duplicates_removed = set(numbers)

print(f"set of numbers: {duplicates_removed}")
