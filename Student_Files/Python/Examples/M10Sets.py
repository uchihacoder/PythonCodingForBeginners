import os
import sys
#a set is like a list but no duplicates and immutable
firstSet = {3,1,4,1,5,9}

print(firstSet)        #outputs {9, 1, 3, 4, 5}
#firstSet.sort()       # won't work
firstList = list(firstSet)    # converts set to list
firstList.sort()
print(firstList)       #outputs [1, 3, 4, 5, 9]

secondSet = set(firstSet)
print(secondSet)       #outputs {9, 1, 3, 4, 5}

print("length=%s" % len(secondSet))     #outputs length=6  LENGTH
print("max=%s" % max(secondSet))        #outputs max=9     MAX
print("min=%s" % min(secondSet))        #outputs min=1     MIN