"""
#Method-1
#creating a function
def course(parameters):
    print(parameters)  #part of course function
    return parameters  #No argument in return means NONE

#calling a function
a=course('python')
print(a)

#Method-2
def name(firstname):
    print(firstname)
name('manohar')
"""
#Method-3
#Creating a function
def name1(name):
    print(name)
    return
#Creating a variable
firstname = "Manohar Dharmala"

#Calling a function
a = name1('Anshul Dharmala')
name1(firstname)

def mykids(*kids):
    print("My son is :",kids[2])
mykids("ram","krishna","Anshul")


def my_function(**wifes):
    print("My wife is:",wifes["lname"])
my_function(fname = "Deepu",lname="Deepika")

def my_country(country = "India"):
    print("My country name is :" + country)
my_country("US")
my_country("England")
my_country()