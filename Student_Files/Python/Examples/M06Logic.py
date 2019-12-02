import sys
import os

# if else elif == != > >= < <= and or not
age = 21
if age > 22 :
    print("age is greater than 22")
    print("another line")
elif age >= 16 :
    print("age is greater than or equal to 16")
    print("another line")
else : print("age is not greater 16 or equal to AND not greater than 22")

if ((age >= 1) and (age <= 18)):
    print ("minor");
elif not(age == 19) and not(age == 20):
    print ("not 19 and not 20")
elif (age == 21) or (age > 21) :
    print("adult");

name = "karl"
if name == "karl" :
    print("name is karl")
else :
    print("name isn't karl")