#try/except - catch and recover from exceptions
#try/finally - perform cleanup actions exception or not
#raise - Trigger an exception manually
#assert - conditionally triger an exception
#with/as - implement context managers
#
#except:                         catch all exception types
#except name:                    catch a specific exception
#except name as value:           catch a specific exception and assign instance
#except (name1, name2):          catch any of the exceptions
#except (name1, name2) as value: catch any of the exceptions and assign instance
#else:                           run if no exceptions
#finally:                        always run

#Python Exceptions
try:
    i = 7/0     # divide by zero
    print("i will never get here")
except ZeroDivisionErrorz
    print("handling ZeroDivisionError exception")

l = []
try:
    i = l[1]     # indexing error
except IndexError:
    print("handling IndexError exception")

#User-Defined exceptions
class BadColor( Exception): pass

class AdvBadColor( Exception): 
    pass
    '''
    __msg = None
    def __init__(self, msg):
        self.__msg = msg
    def toString(self):
        return self.__msg
    '''

def setColor( color):
    if color == "orange":
        raise AdvBadColor("color '" + color + "' is invalid")
    if color in ["red","blue","green"]:
        print(color + " valid")
    else:
        raise BadColor();
try:
    setColor("blue")
    setColor("purple")
except BadColor:
    print("Bad color provided")
else:
    print("only do this if no exception")
finally:
    print("always do this")
    
try:
    setColor("orange")
except AdvBadColor as e:
    print(str(e))
    
    
#LOOPING EXAMPLE
def setColor2( color):
    if color in ["red","blue","green"]:
        print(color + " valid")
    else:
        raise AdvBadColor("color '" + color + "' is invalid")
eList = []
for c in ["red","magenta", "cyan", "blue","green","purple"]:
    try:
        setColor2(c)
    except AdvBadColor as e:
        eList.append(e)

for e in eList:
    print(str(e));
