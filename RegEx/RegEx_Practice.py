#####A set of characters[] ###########
import re
str = "The rain in Spain"
x  = re.findall("[a-z]",str)
print(x,len(x))

# \	Signals a special sequence (can also be used to escape special characters)
str1 = "this will be 59 dollars"
x1 = re.findall("\d",str1)     #find all digit chars
print(x1)

#. Any character (except newline character)
str2 = "hello world"
x2 = re.findall("h...o",str2)
print(x2)

str10 = "hello world"
x10 = re.findall("he...o",str10)    #if its does not match it will give as empty 
print("string10",x10)

# ^ starts with
str3 = "Hello World"
x3 = re.findall("^Hello",str3)
if x3:
    print("Yes,This string starts with 'hello ")
else:
    print("No Match")

# $ Ends with
str4 = "Hello World Python"
x4 = re.findall("Python$",str4)
print(x4)

# * Zero or more occurrences

str5 = "This is Manohar and he is very good"
x5 = re.findall("is*",str5)
if x5:
    print("Yes,there is a match")
else:
    print("There is no match")

# + one or more occurances

str6 = "This is Manohar and engineer"
x6 = re.findall("is+",str6)
if x6:
    print("There is at least one match")
else:
    print("There is no match")

#{}Exactly the specified number of occurrences
str7 = "The rain in Spain falls mainly in the plain!"
#Check if the string contains "a" followed by exactly two "l" characters:
x7 = re.findall("a1{}",str7)
if x7:
    print("Yes,There is at least one match")
else:
    print("No Matches")

# | either or

str8 = "The rain in Spain falls mainly in the plain!"
x8 = re.findall("Falls|stays",str8)
if x8:
    print("one word matching")
else:
    print("No matches found in one word")