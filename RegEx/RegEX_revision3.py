import re
str = "we are staying in Bangalore,karnataka 08"
test = re.findall("Bangalore",str)
print(test)

#search
test1 = re.search("\d",str) #If no matches are found,then it will return as None
print(test1)

#split the string at every white-space character:
test2 = re.split("\s",str)
print(test2)

#split the string at every characters including letters and no's
test3 = re.split("\W",str)
print(test3)

#We can control the number of occurances by specifying maxsplit parameter
test4 = re.split("\s",str,2)  #It will split 2 occurances
print(test4)

#The sub() function replaces the matches with the text of your choice
#Replaces the whitespace characters with digit 8.
test5 = re.sub("\s","8",str)
print(test5)

test6 = re.sub("we","Dharmala's",str)
print(test6)

#We can control the number of replacements by specifying the count parameter
test7 = re.sub("a","d",str,5)  #Replace the first 5 occurrences:
print(test7)

#span() returns a tuple containing the start- and end positions of the match.
test8 = re.search(r"\bB\w+",str)
print(test8.span())

##string() --The string property returns the search string
test9 = re.search(r"\bB\w+",str)
print(test9.string)

#group()--Print the part of the string where there was a match
test10 = re.search(r"\bB\w+",str)
print(test10.group())