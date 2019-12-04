def generate_squares(number):
    for i in range(number):
        yield i ** 2


gen_sqrs = generate_squares(10)

for sqr in gen_sqrs:
    print(sqr, end=" ")
