import os
import sys
#a Tuple is like a list but can't be modified (i.e.,final)
firstTuple = (3,1,4,1,5,9)

print(firstTuple)       #outputs (3,1,4,1,5,9)
#firstTuple.sort()       # won't work
firstList = list(firstTuple)    # converts tuple to list
firstList.sort()
print(firstList)       #outputs [1, 1, 3, 4, 5, 9]

secondTuple = tuple(firstList)
print(secondTuple)       #outputs (1, 1, 3, 4, 5, 9)


print("length=%s" % len(secondTuple))     #outputs length=6  LENGTH
print("max=%s" % max(secondTuple))        #outputs max=9     MAX
print("min=%s" % min(secondTuple))        #outputs min=1     MIN