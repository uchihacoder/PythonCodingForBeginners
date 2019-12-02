import os
import sys

#dictionary {key:value} pairs - similar to list except can't use + to append
firstDictionary = { 'TX' : 'Texas', 'NJ' : 'New Jersey', 'AL' : 'Alabama', 'CO' : 'Colorado'}

print(firstDictionary)          #outputs {'CO': 'Colorado', 'TX': 'Texas', 'AL': 'Alabama', 'NJ': 'New Jersey'}
print(firstDictionary['TX'])    #outputs 'Texas'

#GET
print("GET:" + firstDictionary.get('TX'))    #outputs 'Texas'

#KEYS
print("KEYS:" + str(firstDictionary.keys()))    #outputs dict_keys(['CO', 'TX', 'NJ', 'AL'])

#VALUES
print("VALUES:" + str(firstDictionary.values()))    #outputs dict_values(['Colorado', 'Texas', 'New Jersey', 'Alabama']

#ITEMS
print("ITEMS:" + str(firstDictionary.items()))    #outputs dict_values(['Colorado', 'Texas', 'New Jersey', 'Alabama']


#DELETE
del firstDictionary['CO']       #deletes the 'CO' : 'Colorado'
#del firstDictionary[0]         #wont work
print(firstDictionary)          #outputs {'TX': 'Texas', 'AL': 'Alabama', 'NJ': 'New Jersey'}

#REPLACE
firstDictionary['TX'] = 'TEXAS'
print(firstDictionary)          #outputs {'TX': 'TEXAS', 'AL': 'Alabama', 'NJ': 'New Jersey'}

#LEN/MIN/MAX
print("length=%s" % len(firstDictionary))           #outputs length=3  LENGTH
print("length=%s" % len(firstDictionary['TX']))     #outputs length=5  LENGTH
print("max=%s" % max(firstDictionary))              #outputs max=TX    MAX
print("min=%s" % min(firstDictionary))              #outputs min=AL    MIN

#MISSING ITEMS
if not 'LA' in firstDictionary:
    print("LA MISSING")
else :
    print("LA FOUND")