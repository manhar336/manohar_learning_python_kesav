#!/usr/bin/python
"""
#Strings in python

1. ''
2. ""
3. """ """
4.''' '''

#Values in strings
1. A-Z
2. a-z
3. A-z
4. 0-nth
5. special chars like $@%
6 _

left operand = name of the variable
right operand = value of the variable
"""
firstname = 'Guido'
middlename = "van"
lastname = """Rossum"""
age = 26
name = "Guido van Rossum"
print('\033[1m' + firstname)
print(type(firstname),type(age))  #type is built in function to check type of the datatype
print(id(firstname),id(age))      #id is built in function to check memory location

number = int(age)
print(number,type(number))
