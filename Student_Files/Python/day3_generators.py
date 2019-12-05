# generator function
def generate_squares(number):
    for i in range(number):
        yield i ** 2


gen_squares_func = generate_squares(10)

print("func:\n")

for sqr in gen_squares_func:
    print(sqr, end=" ")

print("\n")

# generator expression
gen_squares_exp = (number ** 2 for number in range(10))

print("exp:\n")

for sqr in gen_squares_exp:
    print(sqr, end=" ")
