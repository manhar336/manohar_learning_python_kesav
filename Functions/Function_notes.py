"""
Function is a block of organise reusable code,that is used to perform single action for multiple times
Functions provide better modularity for our application and using .
Function is nothing but reuse the code for no of times.
Built in functions like print,len,tuple,string etc.
Apart from that we can create user defined functions

def : keyword and stands for documentation string or docs string

Syntax:

#Creating a function
   def functionname(parameters/arguments):
          statements
          return expression/parameters   #indcicates function ended

#calling a function
variablename = value
print(variablename)
"""
#Example1

def course(parameters):
    print(parameters)
    return

a = course('python')
print(a)
"""
Output
python
None
"""
print("\n")
#Example2
def course1(parameters):
    print(parameters)
    return parameters

course_offered = course1('Aws')
print(course_offered)
print("")

#Example 3 (calling from one function to another)
def name(parameters):
    print(course('Linux'))
    return parameters

coursename = name('Devops')
print(coursename)