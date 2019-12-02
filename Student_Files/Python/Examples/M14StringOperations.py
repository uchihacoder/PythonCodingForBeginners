
firstStr = "four score and seven years ago"
print( firstStr) #outputs 'four score and seven years ago'
print("'" + firstStr[0:4] + "'")  #outputs 'four'
print("'" + firstStr[-3:] + "'")  #outputs 'ago'
print("'" + firstStr[:-3] + "'")  #outputs 'four score and seven years '

secondStr = firstStr[0:4] + " " + firstStr[-3:]
print("'" + secondStr + "'")      #outputs 'Four ago'

#FORMATED STRING
print("letter='%c', string='%s', whole number=%d, float number=%.5f" % ('A', 'Hello There', 23, .14))

#UPPER CASE
print( firstStr.capitalize()) #outputs 'Four score and seven years ago'  FIRST LETTER ONLY
print( firstStr.upper())      #outputs 'FOUR SCORE AND SEVEN YEARS AGO'

#FIND
print( firstStr.find("years")) #outputs 21

#LENGTH
print( len(firstStr))    #outputs string length


#ISALPHA ISALNUM
thirdStr = "aBcDeFgHi"
fourthStr = "12345"
print(firstStr.isalpha())
print(thirdStr.isalpha())
print(fourthStr.isalnum())

#STRIP linefeeds
fifthStr = "aBcDeFgHi\n"
print("'" + fifthStr + "'")
print("'" + fifthStr.strip() + "'")   #removes linefeed

#REPLACE
print(firstStr.replace('years', 'YEARS'))

#SPLIT
strList = firstStr.split(" ")   #converts the string into an array using the space character as the separator
print(strList)                  #outputs ['four', 'score', 'and', 'seven', 'years', 'ago']


if (firstStr.isalpha()):
    print("all alpha characters")
elif (firstStr.isalnum()):
    print("alpha characters and numbers")



#Repetition
sixthStr = "Me " * 5            # equivalent of "Me " + "Me " + "Me " + "Me " + "Me "
print(sixthStr)
print('-'*40)


#indexing
s = "Hello There"
for x in s :
    print(x)

for i in range(0, len(s)):
    print(s[i], end=" ")
print()       
 
#slicing
print(s[0:len(s):2])        # outputs HloTee (skips 2 chars)

#String conversion tools
print( int("42") + 1)
print( "123" + str(4))

#formating
print( 'This %s is %s.' % ('spam', 'absolutely horrible'))
print( 'This %(food)s is %(adjective)s.' % dict(food='spam', adjective='absolutely horrible'))
print( 'This {0} is {1}.'.format('spam', 'absolutely horrible'))
print( 'This {} is {}.'.format('spam', 'absolutely horrible'))
print( 'This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))