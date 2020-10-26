#!/usr/bin/python
var_1 = 100
if var_1>200:    #Here condition is not corrent means not True(pass)  it wont  execute statements after suite(:)
    print("you are in first statement")
    print("you are in IF block")
else:            #suppose if condition does not pass,else condition will execute
    print("you are in second statement")
    print("you are in else BLOCK")
print("outside of the if--else statement")
print("------------------------------------")

if var_1<200:    #Here condition True(pass) means it will execute statements after suite(:)
    print("you are in first statement")
    print("you are in IF block")
else:            #suppose if condition does not pass,else condition will execute
    print("you are in second statement")
    print("you are in else BLOCK")
print("outside of the if--else statement")

#Note :if we want to check True or False condition need to go for If-else condition
print("------------------------------------")
tech = input("enter your couse name:")
if tech == "python":print("python course")
