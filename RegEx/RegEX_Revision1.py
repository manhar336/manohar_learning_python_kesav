#1. \A Returns a match if the specified characters are at the beginning of the string
import re
str = "We are one family and great one"
x = re.findall("\AWe",str)
print(x)

#2.\b Returns a match where the specified characters are at the beginning or at the end of a word
x1 = re.findall(r"\bWe",str)
print(x1)

x2 = re.findall(r"one\b",str)
print(x2)

x3= re.findall(r"\bWe|one\b",str)
print(x3)

#3.\B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
x4 = re.findall(r"\Bmily",str)
print(x4)
x5 = re.findall(r"rea\B",str)
print(x5)

#4.\d Returns a match where the string contains digits (numbers from 0-9)
str1 = "this is my number 749461 $"
x6 = re.findall("\d",str)
print(x6)
x7 = re.findall("\d",str1)
print(x7)

#5.\D Returns a match where the string DOES NOT contain digits
x8 = re.findall("\D",str)
print(x8)
x9 = re.findall("\D",str1)
print(x9)

#6.\s Returns a match where the string contains a white space character
x10 = re.findall("\s",str)
print(x10)
x11 = re.findall("\s",str1)
print(x11)

#7.\S Returns a match where the string DOES NOT contain a white space character
x12 = re.findall("\S",str)
print(x12)
x13 = re.findall("\S",str1)
print(x13)

#8. \w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
x14 = re.findall("\w",str)
print(x14)
x15 = re.findall("\w",str1)
print(x15)

#9.\W Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.)
x16 = re.findall("\W",str)
print(x16)
x17 = re.findall("\W",str1)
print(x17)

#10.\Z Returns a match if the specified characters are at the end of the string
x18 = re.findall("one\Z",str)
print(x18)

x19 = re.findall("$\Z",str1)
print(x19)
