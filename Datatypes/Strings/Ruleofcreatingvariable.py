#!/usr/bin/python
"""
#Rule of creating variable in python

1. A-Z
2. a-z
3. 0-9
4. A-Za-z
5. A-Za-z0-9
6. _(underscore)
7. A-Za-z0-9_
Note : Numeric variable can not be initaited as variable name
"""

#creating variables in python
FIRSTNAME = "Guido"
middlename = "Van"
LastName = 'Rossum'
Version_3 = 3.7
#007  = "Jamesbon"   #we should not create variable starts with(prefix) numeric value and not valid varilable name
_007 = "Jamesbond"

#Calling Variables in python
print(FIRSTNAME,"calling",middlename)
print(FIRSTNAME,middlename,LastName,Version_3,_007)
