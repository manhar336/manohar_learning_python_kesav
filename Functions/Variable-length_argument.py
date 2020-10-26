"""
4.Variable-length Argument: If we want to process more than 1 argument we will use variable lenth argument

* : Asterisk is placed before the variable name and going to handle more than 1 argument
"""
#Example 1
def language(arg1,*vartuple):
    'Variable-length argument'
    print(arg1)
    for var,var1 in list(enumerate(vartuple)):
        print(var,var1)

    return
language(0,1,2,3,4)
print("")

#Example2
def info(*languages):
    'Variable-length arguments'
    for lang in languages:
        print(lang)
    return
info('aws','azure','devops')
print("")

#Example 3
def family(*kids):
    print("The Youngest kid is ",kids[1])

family('ram','lakshman','sita')