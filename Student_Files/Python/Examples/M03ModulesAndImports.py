'''
A module is merely a file with a .py extension.  Python code in one module gains 
access to the code in another module by the process of importing it.  This is 
true for built-in Python modules and user-defined custom modules.  The import 
statement is the most common way of invoking the import machinery, but it is not 
the only way. Functions such as importlib.import_module() and built-in __import__()
can also be used to invoke the import machinery.  See also reload and exec.

The import statement combines two operations; it searches for the named module, then
it binds the results of that search to a name in the local scope. The search operation
of the import statement is defined as a call to the __import__() function, with the
appropriate arguments. The return value of __import__() is used to perform the name 
binding operation of the import statement.
'''

#using built-in module
print("-"*20 + " Example of using Built-in Python modules " + "-"*20)
import sys

print (sys.platform)
print("-"*20 + " Output available functions and attributes " + "-"*20)
print (dir(sys))                            #output available functions and attributes
print("-"*20 + " Output help on available functions and attributes " + "-"*20)
print (help(dir(sys)))                      #output help on available functions and attributes

#loading custom module
print("-"*20 + " Example of using custom modules " + "-"*20)
import SimpleModule                         #import the entire module
print (SimpleModule.title)                  #access its attributes

from SimpleModule import a, b               #import attributes so they can be accessed without prefix SimpleModule
#NOTE you could also use "from SimpleModule import *" which make everything in the module available without need 
#for prefixing it with SimpleModule
print("a="+a+",b="+b)                       
                                            
import os
print(os.getcwd())

#loading custom module in another package
from MyPackage import MyModule
print (MyModule.foo())

#RELOAD
#You can only import a module once per session by default.  After the first import,
#later imports do nothing, even if you change and save the module's source file again.
#This is by design because imports are too expensive an operation to repeat more than
#once per file, per program run.  If you really want to force Python to run the file
#again in the same session without stopping and restarting the session, you need to 
#instead call the reload function, which is in the imp standard library in 3.x.
print("-"*20 + " Example of using import " + "-"*20)
SimpleModule.title = "something different"      #The SimpleModule.py contains title = "hello there"
print("before import:SimpleModule.title='"+SimpleModule.title+"'")
import SimpleModule                             #ignored
print("after import:SimpleModule.title='"+SimpleModule.title+"'")

print("-"*20 + " Example of using reload " + "-"*20)
SimpleModule.title = "something different"      #The SimpleModule.py contains title = "hello there"
print("before reload:SimpleModule.title='"+SimpleModule.title+"'")
#from imp import reload                         $ note that imp has been deprecated with importimp
from importlib import reload
reload(SimpleModule)
print("after reload:SimpleModule.title='"+SimpleModule.title+"'")

#EXEC
#The exec(open('module.py').read()) built-in function call is another way to launch
#files without having to import and later reload
print("-"*20 + " Example of using exec " + "-"*20)
title = "something different"                   #The SimpleModule.py contains title = "hello there"
print("before exec:title='"+title+"'")
exec(open('SimpleModule.py').read())
print("after exec:title='"+title+"'")
