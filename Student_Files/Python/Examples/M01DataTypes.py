def foo():
    None;
class MyClass:
    None;
v0 = None;          # NoneType
v1 = 25;            # int
v2 = 2.6;           # float
v3 = True;          # bool
v4 = "hello";       # str
v5 = [];            # list
v6 = ();            # tuple
v7 = {1};           # set
v8 = {};            # dict
v9 = range(10);     # range
v10 = foo;          # function
v11 = MyClass();    # class
print("v0 is " + str(type(v0)))
print("v1 is " + str(type(v1)))
print("v2 is " + str(type(v2)))
print("v3 is " + str(type(v3)))
print("v4 is " + str(type(v4)))
print("v5 is " + str(type(v5)))
print("v6 is " + str(type(v6)))
print("v7 is " + str(type(v7)))
print("v8 is " + str(type(v8)))
print("v9 is " + str(type(v9)))
print("v10 is " + str(type(v10)))
print("v11 is " + str(type(v11)))