# Solutions/Regex/regex.py
#

import re

file = open("./aboutpython.txt", "r")

for line in file:
    line = re.sub('Py', 'Python', line)
    print(line)