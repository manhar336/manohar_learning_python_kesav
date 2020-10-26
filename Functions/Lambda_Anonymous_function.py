"""
Lambda is fall under Anonymous function and is just keyword
lambda : Keyword

we can create custom function using lamda in place of def keyword as well
lambda function takes various arguments as input and print as only one output

syntax: lambda arg1 + arg2 : expression
Syntax:lambda arguments : expression

"""
#Example1
sum1 = lambda arg1,arg2,arg3,arg4:  arg1 + arg2
print(sum1(10,20,30,40))
print("")

#Example2
product = lambda pro1,pro2,pro3,pro4: pro1 * pro2 * pro3 * pro4   #arg1 * arg2 is called as expression
print(product(10,10,5,2))

#Example3
x = lambda a, b : a * b
print(x(5, 6))

print("")
mul = lambda a,b: a * b
print(mul(10,20))