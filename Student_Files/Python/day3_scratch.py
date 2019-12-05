import os

# print(os.environ["HOME"])

arguments = [1, 2, 3, "hello", "there"]

stringified_arguments = [str(item) for item in arguments]

str_args = ", ".join(stringified_arguments)

print(str_args)
