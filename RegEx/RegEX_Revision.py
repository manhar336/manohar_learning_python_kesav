#1.Set Of Characters[]
import re
course = "Python world"
str = re.findall("[a-n]",course)
print(str)

#2. Signals Special sequence (can also be use of escape chars)

course1 = "Python world in 59 $ market mar tooo"
str1 = re.findall("\$",course1)  #find all $
str2 = re.findall("\d",course1)  #findall digiit characters
print(str1,str2)

#3. Any character (except new line character)

str3 = re.findall("Py...n",course1)
print(str3)

#4. ^ Starts with(check if the string starts with)

str4 = re.findall("^Python",course1)
print(str4)

#5. $ ends with (check if the string ends with)

str5 = re.findall("world$",course)
print(str5)

#6. * Zero or more occurrences #Check if the string contains "mar" followed by 0 or more "x" characters
str6 = re.findall("mar*",course1)
print(str6)

#7. + One or more occurrences
str7 = re.findall("ma+",course1)
print(str7)

#8.{} Exactly the specified number of occurrences Check if the string contains "t" followed by exactly 3 "o" characters and 4 means not exist
str8 = re.findall("to{3}",course1)
print(str8)

#9.Either or Check if the string contains either "Python" or "market"
str9 = re.findall("Python|market",course1)
print(str9)


