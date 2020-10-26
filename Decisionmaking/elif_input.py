"""
#!/usr/bin/python
number=int(input("enter first number:"))
value=int(input("enter second number:"))
if (number==value):
    #New Block starts here
    print("both number and value are same")
    #New Block ends here
elif (number>value):
    #Another Block
    print("number is greater than the value")
else:   #else is not mandatory in elif condition
    print("number is less than the value")
print("you are done")
#This is the last statement is always executed after the if statement is executed
print("--------------------------------")
"""
"""
course = "python"
if course == "devops":
    print("you are doing Devops course")
elif course=="java":
    print("you are doing Java course")
"""
course = input(str("enter course nane:"))
if course == 'Linux':
    print("you are part of linux administration",course)
elif course=='java':
    print("this is java course")
else:
    print("you are good")

