import sys
import os

firstList = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
secondList = ['one', 'two', 'three', 'four']

print (firstList)     #outputs ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print (firstList[0])  #outputs A
print (firstList[1:3]) #outputs 'B', 'C' !!!NOTE!!!! that 3rd element does NOT get printed (n-1)


combList = [ firstList, secondList]
print(combList)       #outputs [['A', 'B', 'C', 'D', 'E', 'F', 'G'], ['one', 'two', 'three', 'four']]
print(combList[1][1]) #outputs 'two'

#APPEND
firstList.append('H')
print(firstList)    #outputs ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

#INSERT
firstList.insert(1, 'AA')
print(firstList)    #outputs ['A', 'AA', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

#REVERSE
firstList.reverse();
print(firstList)    #outputs ['H', 'G', 'F', 'E', 'D', 'C', 'B', 'AA', 'A']

#SORT
firstList.sort();
print(firstList)    #outputs ['A', 'AA', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

#DELETE
del firstList[1]
print(firstList)    #outputs ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
