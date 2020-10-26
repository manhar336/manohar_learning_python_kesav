"""
1. Global Variables: A variable can be accessed anywhere
2. Local Variables: If we create varibale inside the function that is local variable and accesed only that variable
and we can not accessed outside of the function and if we want to call we need to call function as well.

"""

#!/usr/bin/python

total = 0 #This is global variable

#function of definition is here
def sum(arg1,arg2):
    "Add both parameters and return  them "
    total = arg1 + arg2    #Here total is local variable
    print("Inside the function local variable",total)
    return total

#Now we can call sum function
sum(10,20)

print("Outside the global function",total)