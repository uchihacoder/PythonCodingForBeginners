# Labs/Regex/regex.py
#

import re

file = open("./aboutpython.txt", "r")

for line in file:

    revised_line = re.sub("Py", "Python", line)

    print(revised_line)
