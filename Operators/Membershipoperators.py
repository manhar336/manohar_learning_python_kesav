'''--------------------------------------------------------------'''
# 6. Membership Operators :
'''--------------------------------------------------------------'''

'''
in and not in are the membership operators in Python. 

They are used to test whether a value or variable is found in a sequence
(string, list, tuple, set and dictionary).

# Membership operators test for membership in a sequence, such as
# strings, lists, or tuples.

1. in	    = x in y, here in results in a 1 if x is a member of sequence y.
2. not in   = x not in y, here not in results in a 1 if x is not a member of sequence y.
'''
'''--------------------- Examples ----------------------------'''
#Example #5: Membership operators in Python
"""
x = 'Hello world'
y = {1:'a',2:'b'}

# Output: True
print('H' in x)

# Output: True
print('hello' not in x)

# Output: True
print(1 in y)

# Output: False
print('a' in y)
"""
a = "python world"
b = {"name":"manohar","age":36}
c= [1,2,3,4]
print("python" in a)  # here condition is true
print("python" not in a) # Here condition is false

print("name" in b)  #Here condition is True
print("manohar" in b)  #Here we can not call values in dictionary and we can call only keys

print(type(c),"10" in c)
print("20" not in c)