# def alpha(number):
#     if not isinstance(number, int):
#         print(f"The argument was not an integer!")
#         return

#     print(f"alpha function was called!  {number}")


# alpha(5)
# alpha("hello")


# def loopit(message, max_count=2):
#     for i in range(max_count):
#         print(message)


# loopit(max_count=5, message="there")


# def var_func(required_arg, *args, **kw_args):
#     print(f"required_arg: {required_arg}")

#     if args:
#         print(f"args: {args}")

#     if kw_args:
#         print(f"keyword args: {kw_args}")


# var_func(1, 2, 3.2, saying="hello")

# def scope_example():
#     x = 23
#     print(f"Inside scope_example.  x: {x}")


# x = 22

# print(f"main before. x: {x}")

# scope_example()

# print(f"main after. x: {x}")

def no_arg_func(message):
    print(message)


def yet_another_func(message):
    print(message)


# def another_func(message, another_message, yet_another_func):
#     print(f"My message: {message}, another message: {another_message}")
#     yet_another_func


# def main_func(another_func):
#     print(f"Inside main_func")
#     another_func


# main_func(another_func("hello", "there", yet_another_func("test message")))

# def call_it(f):
#     f


# call_it(no_arg_func("test"))

# mechanism for defining a "private" function -- a function that can use variables, etc. defined in the wrapping function
# similar to an IIFE in JavaScript
# def outer_func():
#     x = 100
#     print(f"outer function")

#     def inner_func():
#         print(f"inner function. x: {x}")
#     inner_func()


# outer_func()

# def square_it(a):
#     return a * a


# print(square_it(5))

# sqr_lambda = lambda a: a * a

# print(sqr_lambda(7))

numbers = [1, 2, 3, 4, 5]

for n in numbers:
    if n % 2 == 0:
        print(f"in the for loop: {n}")


# def is_even(n): return n % 2 == 0


even_numbers = list(filter(lambda n: n % 2 == 0, numbers))

odd_numbers = list(filter(lambda n: n % 2 == 1, numbers))

square_numbers = list(map(lambda n: n * n, numbers))

for n in even_numbers:
    print(f"even numbers {n}")

for n in odd_numbers:
    print(f"odd numbers {n}")

for n in square_numbers:
    print(f"square numbers {n}")
