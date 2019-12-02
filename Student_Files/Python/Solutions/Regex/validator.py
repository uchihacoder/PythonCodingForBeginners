# Solutions/Regex/validator.py
#

import re

while True:
    password = input("Enter a candidate password: ")
    if password == '':
        break

    print("Valid password:", re.search('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W)(.{8,})$', password) != None)
