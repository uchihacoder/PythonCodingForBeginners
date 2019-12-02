'''
The documentation for parse is available at: https://pypi.python.org/pypi/parse
#Because parse is not a part of the core package you need to install it (e.g., using pip):
pip install parse

#In eclipse, if you can't 'from parse import *', then try:
Select Window - > Preferences -> PyDev -> Interpreter - Python
Select the python interpreter in the upper pane
Click on Remove
Click on Auto Config
Agree to everything.


#In eclipse, if you still can't find the import and you have multiple installations of
#python installed on your computer then check your path and confirm that the {python_install_directory}/Scripts
#matches the directory specified above in the "Interpreter - Python" on eclipse
'''

from parse import *

# Check to see if ssh is an accepted protocol

with open("iptables.txt") as f:
    for line in f:
#        result = search("ACCEPT{:s}{:w}{:s}{:w}{:s}{:w}{:s}{:w}{:s}{:w}{:s}dpt:{:w}", line)
        result = search("ACCEPT{:s}{protocol:w}{:s}--{:s}{source:w}{:s}{destination:w}{:s}{destination_port_protocol}{:s}dpt:{application_protocol:w}", line)
        if result:
            print(result)
            properties = result.named
            if (properties["application_protocol"] == "ssh"):
                print("ssh allowed!")