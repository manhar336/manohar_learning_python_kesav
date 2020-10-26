#Default argument: Default argument is an argument and assumes a value if value not provided  by function call argument
#if we prpvide values in caller in will accept otherwise it will take default values
#if we provide deafult value in function ,no need to call again
#Example:1
#Creating a function
def name1(firstname,middlename,lastname,age=30): #firstname,middlename,lastname are required argument and age is default
    print("Firstname:",firstname)
    print("Middlename:",middlename)
    print("Lastname:",lastname)
    print("age:",age)
    return
#Calling a function
name1('Guido','Van',"Rossum",50)
print("")

#Example:2
#Creating a function
def name1(firstname,middlename,lastname,age=30):
    print("Firstname:",firstname)
    print("Middlename:",middlename)
    print("Lastname:",lastname)
    print("age:",age)
    return
#Calling a function
name1('Guido','Van',"Rossum")
#name1('Guido','Van')  #TypeError: name1() missing 1 required positional argument: 'lastname'

#Example:3
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
