#EXAMPLE 1
print("-"*20 + " Example 1 " + "-"*20)
def my_generator():
     print("Inside my generator")
     yield 'a'
     yield 'b'
     yield 'c'

for char in my_generator():
    print(char)
    print(char)
    
#EXAMPLE 2
print("-"*20 + " Example 2 " + "-"*20)
def infinite_generator(start=0):
    while True:
        yield start
        start += 1

for num in infinite_generator(4):
    print(num, end=' ')
    if num > 20:
        break