import random
import sys
import os

#FOR LOOP
for x in range(0, 10):
    print(x)

for x in range(0, 10):
    print(x, " ",end="")        #outputs 0 1 2 3 4 5 6 7 8 9
print("\n")

firstList = ['A', 'B', 'C', 'D', 'E']
for y in firstList :
    print(y)

for x in [2,4,6,8,10]:
    print(x)

numList=[[1,2,3],[4,5,6],[7,8,9]]
for x in range(0,3):
        for y in range (0,3):
            print(numList[x][y], " ", end="")
        print("")  #prints a line break

squares = []
for x in [1,2,3,4,5] :
    squares.append( x ** 2)
print( squares)


#WHILE LOOP
randomNum = random.randrange(0,100)
while (randomNum > 5) :
        print("randomNum=%s", randomNum)
        randomNum = random.randrange(0,100)
print("exited loop, randomNum=%s", randomNum)

i = 0;
while (i< 30):
    if (i==10) :
        i+=1
        continue  # note that must have increment above - wont get to line 41
    if (i==20) :
        break
    print(i)
    i+=1