#!/usr/bin/python

#Number data types

#1. Interger
Data = 10      #Int 0 to 9(positive) and -0 to -9(Negative integer)

"""
Binary      : 0b or 0B(representation of Binary numbers) = base value is 2
Octal       : 0o or 0O(representation of Octal numbers)  = base value is 8
Hexa decimal: 0x or 0X                                   = base value is 16
"""

#Built in functions: int()      converts value into integer
#2. Float(Floating Point Numbers)
Datapoint = 10.25 #Float Value
#Built in functions: float()    converts value into float
#converting string into Integer and float value

num = "123456"
num1 = int(num)    #converting into integer
print(num1,type(num1),id(num1))
num2 = float(num)   #converting into float
print(num2,type(num2),id(num2))

#3. Complex values
"""
 a + bj
 a is aerial value or real value
 bj or bJ is imaginary value
"""
#Built in functions: complex()    converts value into complex

num3 = complex(num)   #converts value into complex
print(num3)
