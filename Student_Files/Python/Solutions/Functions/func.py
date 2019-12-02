# Solutions/Functions/func.py
#

def repeatIt( output, number=5):
    for i in range(0, number):
        print(output, end=' ')
    print()

repeatIt( "hello", 6)
repeatIt( "newman")
print('-'*50)
repeatIt( number=23, output="howdy")


def secured_access( userType):
    def innerFunc():
        print('You have access')
    if (userType.upper() == 'ADMIN'):
        innerFunc()
        return True
    return False

rc = secured_access( "student")
print( "student: " + str(rc))
rc = secured_access( "Admin")
print( "Admin: " + str(rc))