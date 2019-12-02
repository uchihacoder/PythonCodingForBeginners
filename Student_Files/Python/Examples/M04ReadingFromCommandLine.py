import sys

#EXAMPLE using readline
print("-"*20 + " Example Using readline " + "-"*20)

print('What is your first name>')

fnameIn = sys.stdin.readline()
#Remove the line break character at the end
#fnameOut = namefIn[:-1]   #all characters except the last character which in this case is a "\n"
fnameOut=fnameIn.rstrip()

print("nameIn='" + fnameIn + "'")
print("nameOut='" + fnameOut + "'")

#EXAMPLE using input (note that you don't have to remove a newline at the end)
print("-"*20 + " Example Using input " + "-"*20)
lname = input('What is your last name>')
print("lname='" + lname + "'")
