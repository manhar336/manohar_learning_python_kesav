"""
#########If condition ######
courses_offered = ['aws','python','devops','openstack']

if "aws" in courses_offered:
    print("we are providing training:")

courses_notoffering = input("Please select which you dont want to do:").lower().strip()


if  courses_notoffering:
   print("we are not providing selected course")
"""
"""
#######If else condtion######
num1 = input("enter first number:\n").strip()
print(type(num1))
num2 = input("enter second number:").strip()
print(type(num2),num2)
if num1 == num2:
    print("you entered same number")
else:
    print("Both are different numbers")
"""
###else if condition######
num1 = input("enter first number:").strip()
num2 = input("enter second number:").strip()
num3 = input("enter third number:").strip()

if num1 > num2:
    if num1 > num3:
        maximum = num1
    else:
        maximum = num3
else:
    if num2 > num3:
        maximum = num2
    else:
        maximum = num3


print("maximum number is :",maximum)