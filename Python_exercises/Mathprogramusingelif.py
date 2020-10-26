"""
operators = {"addition":"1","subtraction:":"2","Multiplication":"3","Division":"4"}
print("Please select which operation do you want to do in Maths:",operators)
selection = input("select operation which you wanted to do:")

num1 = int(input("Enter first number:"))
num2 = int(input("enter second number:"))

if selection in operators.values():
    if selection == "1" :
        print("addition of 2 numbers",num1 + num2)
    elif selection == "2":
        print("subtraction of 2 numbers:",num1 - num2)
    elif selection == "3":
        print("Multiplication of 2 numbers: ", num1 * num2)
    elif selection == "4":
        print("Division of 2 numbers:",num1 / num2)
else:
    print("selection does not exist and please try correct option")
"""
operators = {"addition":"1","subtraction":"2","multiplication":"3","division":"4"}
print("select one operation",operators)
selection = input("select one operation")
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
if selection in operators.values():
    if selection == "1":
        print("addition",num1 + num2)
    elif selection == "2":
        print("subtraction:",num1 - num2)
else:
    print("you are done")