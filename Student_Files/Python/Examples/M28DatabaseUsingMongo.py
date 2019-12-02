'''
#The documentation for PyMongo is available at: https://api.mongodb.org/python/3.1/index.html
#and https://docs.mongodb.org/getting-started/python/
#Because parse is not a part of the core package you need to install it (e.g., using pip):

pip install pymongo
OR
python -m pip install pymongo

In Visual Studio Code, if you get ModuleNotFoundError: No module named 'pymongo',
then:
From within VS Code, select a Python 3 interpreter by opening 
the Command Palette (Ctrl+Shift+P), start typing the 
Python: Select Interpreter command to search, then select the 
command. You can also use the Select Python Environment option 
on the Status Bar if available

#In eclipse, if you can't 'from parse import *', then try:
Select Window - > Preferences -> PyDev -> Interpreter - Python
Select the python interpreter in the upper pane
Click on Remove
Click on Auto Config
Agree to everything.


#In eclipse, if you still can't find the import and you have multiple installations of
#python installed on your computer then check your path and confirm that the {python_install_directory}/Scripts
#matches the directory specified above in the "Interpreter - Python" on eclipse

#Create a database and table, and insert rows, using the Mongo daemon and shell
#from a command shell, start the Mongo daemon (note that by default the Mongo daemon utilizes port 27017):
mongod

#DONT PERFORM THESE BELOW STEPS but the Python program is the equivalent of performing the following in Mongo shell:
#mongo
# use studentDB
# db.students.drop
# db.students.insert( {'first_name' : 'Dan', 'last_name' : 'Hancock' });
# db.students.insert( {'first_name' : 'Steve', 'last_name' : 'Rogers' });
# db.students.insert( {'first_name' : 'Bucky', 'last_name' : 'Barnes' });
# db.students.insert( {'first_name' : 'Bruce', 'last_name' : 'Banner' });
# db.students.insert( {'first_name' : 'Tony', 'last_name' : 'Stark' });
# db.students.find()

#use eclipse to connect to a database "studentDB", drop any existing "students" collection, insert documents into
#the "students" collection, and then query and output the documents in the "students" collection:
'''
from pymongo import MongoClient

client = MongoClient()

#db = client.ebi
# same as "use studentDB" (this is the database name)
db = client.studentDB

#drop the students collection if it exists
#db.students.drop()

#insert documents into the students collection
# db.students.insert( {'first_name' : 'Dan', 'last_name' : 'Hancock' });
# db.students.insert( {'first_name' : 'Steve', 'last_name' : 'Rogers' });
# db.students.insert( {'first_name' : 'Bucky', 'last_name' : 'Barnes' });
# db.students.insert( {'first_name' : 'Bruce', 'last_name' : 'Banner' });
# db.students.insert( {'first_name' : 'Tony', 'last_name' : 'Stark' });

# #query the documents in the students collection and output
# cursor = db.students.find({},{ '_id' : 0})
# #cursor = db.students.find()
# for document in cursor:
#     print(type(document))
#     print('first_name is ', document['first_name'], 
#     'last_name is ', document['last_name'])
client = MongoClient()
db = client.flightDB
# cursor = db.flight.find()
# for document in cursor:
#     print('flightno='+str(document['flightno'])+
#     ',orig='+str(document['orig'])+
#     ',dest='+str(document['dest']))
document = db.flight.findOne({'flightno':'1000'})
print('flightno='+str(document['flightno'])+
',orig='+str(document['orig'])+
',dest='+str(document['dest']))
