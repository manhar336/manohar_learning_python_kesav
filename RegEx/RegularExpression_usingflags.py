"""
Regular Expressions:
Module:re
Raw string : r'expression' or R'expression'

import re
####   RE Methos|Functions###

re.match(): This function attempts to match RE pattern to string with optional flags
syntax : re.match(pattern,string,flags)
          pattern : what we are searching or RE expression to be matched
          string : where we are searching or which would be matched the pattern at the beginning of the string
          Flags: We Can specify different flags using bitwise OR (|)
re.match function returns a Match Object if its success and NONE if failure.

We use group(num) or groups function of match object to get match expression

group() : Returns entire match or specific sub group num.
groups(num) : Reurns all matching subgroups in a tuple output.
"""
"""
string = "Python is programming language and python is interesting language"
>>> rawstring = re.match(r'python',string,re.M|re.I)
>>> print(rawstring)
<re.Match object; span=(0, 6), match='Python'>
>>> 

>>> rawstring = re.findall(r'python',string,re.M|re.I)
>>> print(rawstring)
['Python', 'python']
>>> 

>>> rawstring = re.search(r'python',string,re.M|re.I)
>>> 
>>> print(rawstring)
<re.Match object; span=(0, 6), match='Python'>
>>> 
"""
"""
import re
rawinformation = "Python is programming and scripting language " #match only check at the beginning only
matchObj = re.match(r'is',rawinformation,re.M|re.I)  #M means will check multi lines and I means ignorecase
if matchObj:
    print("Match function:yes there is match",matchObj.group)
else:
    print("No match found")

import re
rawinformation1 = "Python is programming and scripting language "
findallobj = re.search(r'is',rawinformation,re.M|re.I)
if findallobj:
    print("Match function:yes there is match",findallobj.group)
else:
    print ("No match found")

matchObj1 = re.match(r"Python",rawinformation,re.MULTILINE|re.IGNORECASE)
if matchObj1:
    print("Match function:yes there is a match",matchObj1.group())
else:
    print("No match found")


matchObj2 = re.match(r'(.*)is',rawinformation,re.M|re.I) # Here . means current line and * means till the end and searched by is

if matchObj2:
    print("Match function:yes there is a match",matchObj2.group())
    print("Match function:yes there is a match",matchObj2.groups())  #groups means it will print except matching in tuple format
else:
    print("No match found")

matchObj3 = re.match(r'(.*)is(.*)',rawinformation,re.M|re.I)

if matchObj3:
    print("Match function:yes there is a match",matchObj3.group())
    print("Match function:yes there is a match",matchObj3.groups())  #groups means it will print before and after match(wont print matching word)  in tuple format
else:
    print("No match found")
"""

#Search Method
import re
rawinformation4 = "Python is programming and scripting language "
searchobject = re.search("and",rawinformation4,re.MULTILINE|re.I)
if searchobject:
    print("There is search in string",searchobject.group())
    print("There is search in string",searchobject.groups())  #groups means it wont print searching word
else:
    print("There is no match")

searchobject1 = re.search("(.*) and (.*)",rawinformation4,re.I|re.MULTILINE)
if searchobject1:
    print("There is match",searchobject1.group())            #group means after searching its printing
    print("There is search object",searchobject1.groups())  #groups means it will print before and after match(wont print matching word)  in tuple format
else:
    print("there is no search")
