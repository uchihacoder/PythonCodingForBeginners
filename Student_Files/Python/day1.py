import something
import sys

print(something.n)

something.foo()

print(f"sys.path: {sys.path}")

# int
x = 1
# float
y = 1.1
# str
z = "Hello"
# list
a = []
# dict
b = {}
# set
# c = set()
c = {1}
# tuple
d = ()
# bool
e = True


def foo():
    """
    This is a comment for the function foo
    """
    return "Howdy"


# print(help(foo))

print(f"type of the function foo: {type(foo)}")

f = foo()

print(f"type of the return type from foo: {type(f)}")

print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# prints out the documentation for x -- in this case a list
# print(help(dir(x)))

s = "Hello THERE how Are yOu DoIng"

# print(s.capitalize())

# print(s.title())

# slice -- second value is the index minus 1
# e.g. returns Hello
print(s[0:5])
