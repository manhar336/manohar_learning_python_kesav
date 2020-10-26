"""
Decision Making(conditional statements) or we can say control flows


1. if
2. if else
3. elif
4.nested elif
"""
'''
1. simple if statement (if is keyword)
if "expresession":      #(:is suite then it will go to indentation ,indentation means 1 tab or 4 spaces)
    statements          #statements could be print function or others
'''
#1. simple if statement (if is keyword)
course_name = "python"
if course_name:
    print("course name:%s" %(course_name)) #Here statements are multilines
    print("this is part of course") #if condition starts from line no 17 and ends with 19
print("outside of if condition")#outside of if condition and not part of if condition and if we can give 1 or 2 spaces it will through exception

#2.Calling statements with simple if condition followed with indentation
#1. Method-1
value = 100
if value==100:print("Yes,condition is met")  #value==100 is expresssion and single line format
print("Goodbye")  #this is out of if condition

#Method-2(used open and closed parenthisis)
print("")
if (value==100):print("Yes,condition is met")
print("Goodbye")
print("")
#Method-3(used open and closed brackets) dont use square brackets(list) and it will give wrong result
if [value==100]:print("Yes,condition is met")
print("Goodbye---------------------")
print("")
#Method-4(use dictionaries)
if {value==100}:   #dont use dictionary also for definining expresssion
    print(type(value))


var1 = 50
value = 100
if value==var1:  #Note :if condition does not match then it wont go inside the suite means program will terminate
    print("Yes,condition is met")
    print("Goodbye")