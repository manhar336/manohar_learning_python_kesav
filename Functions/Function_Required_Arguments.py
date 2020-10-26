"""
1. Required Arguments

2. Keyword Arguments

3. Default Arguments

4. Variable-length Arguments
"""
"""
Required Arguments are the arguments passed by the function with correct positional order 
No of arguments call should match with functiin definition 

"""
#Example1
def name(firstname):
    'This is Required Argument'
    print(firstname)
    return
name('Guido')

#Example2
#Creating a function
def name1(firstname,middlename,lastname):
    print("Firstname:",firstname)
    print("Middlename:",middlename)
    print("Lastname:",lastname)
    return
#Calling a function     
name1('Guido','Van',"Rossum")
