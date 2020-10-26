'''--------------------------------------------------------------'''
# 7. Identity Operators :
'''--------------------------------------------------------------'''

'''
is and is not are the identity operators in Python.

They are used to check if two values (or variables) are located on the same part of the memory.

Two variables that are equal does not imply that they are identical.

# Identity operators compare the memory locations of two objects.

1. is           = x is y, here is results in 1 if id(x) equals id(y).
2. is not       = x is not y, here is not results in 1 if id(x) is not equal to id(y).
'''
'''--------------------- Examples ----------------------------'''
# Example : Identity operators in Python
x= "manohar"
y="manohar"

a=[1,2,3,4]
b=[1,2,3,4]

X={"name":"ra","age":39}
Y={"name":"ra","age":39}

print(x is y)  #Here memory location of a and b is same
print(id(x),id(y),type(x),type(y))
print(x is not y) #Here condition is false
print("")
print(a is b)  #list is immutable datatype and memory location also different if same value as well so condition is false
print(id(a),id(b),type(a),type(b))
print("")
print(X is Y)   #dictionary  is immutable datatype and memory location also different if same value as well so condition is false
print(id(X),id(Y),type(X),type(Y))
