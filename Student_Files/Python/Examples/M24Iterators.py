
it = iter( range(10))
print(it)               #outputs <range_iterator object at 0x01B153B0>
for item in it:
    print(str(item) +  " ", end="")
print("")
tupleList = zip( it, it)

print(tupleList)        #outputs <zip object at 0x01B41B20>