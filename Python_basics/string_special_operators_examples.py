#!/usr/bin/python
firstname = """Guido"""
middlename = 'van'
lastname = "Rossum"

######concatenation#########
name = firstname + middlename + lastname
print("printing the string output using concatenation",name)

######Repetation#########
repetation = firstname * 2
print(repetation,"printing repetation output")

#####Slicing#############
print("printing left to right indexing",firstname[3])
print("printing right to left indexing",firstname[-1])

#####Range Slice########
#print("range slice",firstname[start index:end index] end index-1
print("printing range slice1",firstname[1:4])
print("printing range slice2",firstname[-5:])
print("printing range slice3",firstname[:5])

###Zero based indexing######
num1 = '102030405060'
print("zero based indexing method1",num1[0::2])  #print every second index
print("")
print("zero based indexing method2",num1[0::3])  #print every third index
print("")
print("zeo based indexing method3",num1[2::2])  #print starts from 2nd index and every second index

age = 30
#####formatting#######
print("firstname : %s , middlename : %s, lastname: %s, age: %i" %(firstname,middlename,lastname,age))  #% is called as remainder sign
print("firstname",firstname,"middlename",middlename)  #other way of calling variable

####.format method######
print("firstname : {} , middlename : {}, lastname: {}, age: {}" .format(firstname,middlename,lastname,age)) #{} called as place holders or curly brackets
print("firstname : {1} , middlename : {0}, lastname: {2}, age: {3}" .format(firstname,middlename,lastname,age))
#print based on indexing means if we call index value print respective variable
age = 35
print("My name is Manohar and age is {}" .format(age))
print("no of employees in webex is :{},cisco is:{},netapp is :{}" .format(300,400,500))
#Use the format() method to insert numbers into strings:
#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

#####Raw String: r/R r'expression' or R'expression'######
print(R"c:\\users\\mdharmal") #raw string means print complete path or escaping special chars
print(r"c:\\users\\mdharmal")
