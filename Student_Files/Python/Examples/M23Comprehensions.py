# a list comprehension expression is a way to process structures

#extract the second column of a matrix
M = [[1,2,3],
     [4,5,6],
     [7,8,9],
     [10,11,12],
     [13,14,15]]

col2 = [row[1] for row in M]
print(col2)

#filter out odd values
evenCols = [row[1] for row in M if row[1] % 2 == 0]
print(evenCols)