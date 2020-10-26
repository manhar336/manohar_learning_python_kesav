#/usr/bin/python
"""
Min() method:
Max() method:
Concatenation

"""
tup1 = ("Guido",'van',"""Rossum""")
tup2 = (1,2,3,4,10)
tup3 = ("test1","test2",10,20)  #TypeError: '<' not supported between instances of 'int' and 'str' to get max or min element
print("max value element:",max(tup1))
print("min value element:",min(tup1))
print("")
print("max value element:",max(tup2))
print("min value element:",min(tup2))

#updating a tuple variable
tup01 = (10,20,30)
#tup01[3] = 40  #TypeError: 'tuple' object does not support item assignment because tuple is immutable data type
print(tup01)

#concatenation
tup02 = (10,20,30)
tup03 =  "test1","test2"
print(type(tup03))
tup04 = tup02 + tup03   #concatenation
print(tup04)