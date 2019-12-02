import os
#SET DIRECTORY
print ("Current directory:" + str(os.getcwd()))
os.chdir(r"C:\Student_Files\Python\Examples");
print ("New directory:" + str(os.getcwd()))

#WRITE
testFile = open("test.txt", "wb")
print(os.getcwd())
print(testFile.mode)
print(testFile.name)

testFile.write( bytes("output data\n", "UTF-8"))

testFile.close()

#READ
testFile = open("test.txt", "r")  #open read and write
data = testFile.read()
print("'" + data + "'")
print("'" + data + "'")
print("'" + data + "'")
print("'" + data + "'")
print("'" + data + "'")
print("'" + data + "'")
print("'" + data + "'")
testFile.close()






#DELETE FILE
os.remove("test.txt")

print( '*' * 80)
fp = open('iptables.txt', 'r')
while True:
    line = fp.readline()
    if not line:
        break
    print( line)

print( '*' * 80)
f = open('test.txt', 'w+')
f.write( 'first line\n')

l = [ ]
for i in range(10):
	l.append( 'number is ' + str(i) + '\n' )
f.writelines( l )
f.close()


with open('test.txt', 'r') as f:
	data = f.read()
f.closed
print( data )
