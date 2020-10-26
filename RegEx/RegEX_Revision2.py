#1.Check if the string has any a, r, or n characters:
import re
test = "The man has more money"
str = re.findall("[arn]",test)
print(str)
#2.Check if the string has any chanracters between a and n
str1 = re.findall("[a-n]",test)
print("characters between a and n",str1)
#3.check if the string has any other characters except a,r and n
str2 = re.findall("[^arn]",test)
print(str2)
#4. check if the string has 0,1,2,3 digits
test1 = "this is at the age of 036,22,99 AMMMMM +++"
str3 = re.findall("[0123]",test1)
print(str3)
#check if the string has 0-6 digits
str4 = re.findall("[0-6]",test1)
print(str4)
#check if the string has 2 digit numbers
str5 = re.findall("[0-5][0-9]",test1)
print(str5)
#Check if the string has a-z lowercase and upper case
str6 = re.findall("[a-zA-Z]",test1)
print(str6)
#Check if the string has any + characters
str7 = re.findall("[+]",test1)
print(str7)