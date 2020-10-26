import re
str = "This is the path of the file"

"check if the string starts with This"
x = re.findall("\AThis",str)
print(x)
if (x):
    print("Yes,you have a matching word")
else:
    print("you dont have word")
"""\b Returns a match where the specified characters are at the beginning or at the end of a word"""

#Check if "This" is present at the beginning of a WORD:
y = re.findall(r"\bThis",str)
print(y)
z= re.findall(r"file\b",str)    #if it does not match it will create empty dict
print(z)

"""\B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word"""

#Check if "is" is present, but NOT at the beginning of a word:
a = re.findall("\Bis",str)
print(a)

b = re.findall("ath\B",str)
print(b)

#\d	Returns a match where the string contains digits (numbers from 0-9)
str1 = "This is my number 11 !"
#Check if the string contains any digits (numbers from 0-9):
c = re.findall("\d",str1)
print(c)
d = re.findall("\d",str)   #
print(d)

#\D	Returns a match where the string DOES NOT contain digits
d = re.findall("\D",str)
print(d)
#Return a match at every no-digit character:
e = re.findall("\D",str1)
print(e)

#\s	Returns a match where the string contains a white space character
f = re.findall("\s",str)
print(f)
#Return a match at every white-space character:
g = re.findall("\s",str1)
print(g)

#\S	Returns a match where the string DOES NOT contain a white space character

h = re.findall("\S",str)
print(h)

#Return a match at every NON white-space character:
i = re.findall("\S",str1)
print(i)

#\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)

j = re.findall("\w",str)
print(j)
#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
k = re.findall("\w",str1)
print(k)

#\W	Returns a match where the string DOES NOT contain any word characters
l = re.findall("\W",str)
print(l)

#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
m = re.findall("\W",str1)
print(m)

#\Z	Returns a match if the specified characters are at the end of the string
n = re.findall("file\Z",str)
print(n)

##Check if the string ends with "Spain":
o = re.findall("!\Z",str1)
print(o)