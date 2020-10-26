"""
1. Required Arguments
2. Default Arguments
3. Keyword Arguments
4. Variable-length Arguments
"""
#1. Required Argument
#Required Arguments which send correct positional order means function call and function definition should match exactly
def name(firstname,middlename,lastname):
    'Required Arguments'
    print("Firstname:",firstname)
    print("Middlename:",middlename)
    print("Lastname:",lastname,type(firstname))
    return
name("Atchuta","Narasimha","Manohar")
name(1,2,3)

#2. Keyword Argument ,caller identifies the function based on Keyword ,here we need to provide key and pair value
def keywordargument(firstname,middlename,lastname):
    'Keyword Arguments'
    print("Firstname:",firstname)
    print("Middlename:",middlename)
    print("Lastname:",lastname)

#Calling a function
keywordargument(firstname="Guido",middlename="Van",lastname="Rossum")
#keywordargument(Firstname="Guido",Middlename="Van",lastname="Rossum")  Need to give correect Argumentname when calling function

#3. Default Arguments
def defaultargument(firstname,middlename,lastname,age=40):
    'Default Arguments'
    print("Firstname:",firstname)
    print("Middlename:",middlename)
    print("Lastname:",lastname)
    print("Age",age)
defaultargument("Anshul","Venkata","Dharmala",age=50)
defaultargument("Anshul","Venkata","Dharmala")

#4. Variable length Arguments
def variablelengtharguments(arg1,*arg2):
    'Variable Length Arguments'
# * : Asterick is placed beforee the variable name
    print(arg1)
    for var in arg2:
        print(var)
    return
#calling a function
variablelengtharguments('aws',"azure","Devops")

#Example -2
def info(*arg3):
    for var1 in arg3:
        print(var1)
        print(type(var1))

#Creating a variable  
list1 = ["Aws","Azure","devops"]

#Calling a function
info(list1)



