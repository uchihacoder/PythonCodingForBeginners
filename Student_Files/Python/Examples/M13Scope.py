#Built-in (Python):
#Names preassigned in the built-in module
#    Global (module):
#    Names assigned at the top-level of a module file or declared global
#    in a def within the file
#        Enclosing function locals
#        Names in the local sceope of any and all enclosing functions
#        (def or lamda), from inner to outer
#            Local (function)
#            Names assigned in any way within a function (def or lambda),
#            and not declared global in that function
print("-"*20 + " Names preassigned in the builtins are global " + "-"*20)
import builtins
print(dir(builtins))
print("-"*80)

globalVar1 = "globalVar1 is a global because it is declared at the top-level of a module file"

def foo() :
    localVar = "localVar is a local variable because it is declared within a function"
    global globalVar2
    globalVar2 = "globalVar2 is a global because it is declared global within the file"
    print(localVar)
    print(globalVar2)
    
foo()
#print(localVar)    #won't work
print(globalVar1)
print(globalVar2)


