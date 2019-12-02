import sys
import os
import random

#BASIC FUNCTION - They must be defined before they can be called
def callMe():
    print("callMe function called")

def addNumber( x, y) :
    sumNum = x + y
    return sumNum

def foo() :
    print("entered foo()")
    randomNum = random.randrange(0,100)
    return randomNum

#FUNCTION WITH DEFAULT PARAMETERS
def fum( x, y=123, z=foo()) :
    print("entered fum( " + str(x) + ", " + str(y) + ", " +  str(z) + " )")
    return

#FUNCTION WITH INTERNAL FUNCTION
def fee( x) :
    print("entered fee( " + str(x)  + " )")
    def inner_fee( y=23, z=x):
        print("entered inner_fee( " + str(y) + ", " +  str(z) + " )")
    return inner_fee()   #parenthesis is optional

print( addNumber(1, 4))
#print(sumNum) wont work (out of scope) sumNum is a local variable to function

nbr = addNumber(5,3)
print (nbr)


fum( 1, 2, 3)
fum( 4)
fee( 5)

#functions can be deleted
del fee
#fee(5) #this won't work

def callMe1( x, y):
    z = 33;
    print("callMe1: x={0}, y={1}, z={2}".format(x,y,z))
    def callMe2():
        z = 44;
        print("callMe2: x={0}, y={1}, z={2}".format(x,y,z))

    callMe2();
    print("callMe1: x={0},y={1},z={2}".format(x,y,z))

callMe1( 11, 22)
