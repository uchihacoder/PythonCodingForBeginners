'''
#Download MySQL Community Server 8 - Full Version with Legacy Authentication
https://dev.mysql.com/downloads/mysql/
#remember you username and password that you setup during installation of MySQL - you will need
#it to connect to the database in your Python module.  I'm using a username of root and a password 
#of password, but I'd imagine you'd define something more secure.

pip install mysql-connector-python

#In eclipse, if you can't find the import mysql.connector try:
Select Window - > Preferences -> PyDev -> Interpreter - Python
Select the python interpreter in the upper pane
Click on Remove
Click on Auto Config
Agree to everything.

#In eclipse, if you still can't find the import and you have multiple installations of
#python installed on your computer then check your path and confirm that the {python_install_directory}/Scripts
#matches the directory specified above in the "Interpreter - Python" on eclipse

#Create a database and table, and insert rows, using the Mysql Workbench
CREATE DATABASE studentDB;
use studentDB;
CREATE TABLE students (student_no int(11) NOT NULL AUTO_INCREMENT, first_name varchar(14) NOT NULL, last_name varchar(16) NOT NULL,  PRIMARY KEY (student_no));
INSERT INTO students (first_name, last_name) VALUES ('Dan', 'Hancock');
INSERT INTO students (first_name, last_name) VALUES ('Steve', 'Rogers');
INSERT INTO students (first_name, last_name) VALUES ('Bucky', 'Barnes');
INSERT INTO students (first_name, last_name) VALUES ('Bruce', 'Banner');
INSERT INTO students (first_name, last_name) VALUES ('Tony', 'Stark');
SELECT * FROM students;

#use eclipse to add a python module to query the database (e.g., MySQL.py) and add the following data to it:
'''
import mysql.connector
from mysql.connector import errorcode
cnx = None
try:
    cnx = mysql.connector.connect(user='root', \
                                password='password', \
                                host='127.0.0.1', \
                                database='studentDB')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor = cnx.cursor()

    query = ("SELECT first_name, last_name FROM students ")

    cursor.execute(query);
    for (first_name, last_name) in cursor:
        print("{}, {}".format(last_name, first_name))

    cursor.close()
    cnx.close()