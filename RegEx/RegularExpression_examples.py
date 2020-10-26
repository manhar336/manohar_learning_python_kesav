import re
#Example-1(print only name and age of the given string
Nameage = "Anshul is 10 ,Seby is 9,Rithvik is 24 and Dad is 70"
ages = re.findall(r"\d+",Nameage)
#print(ages)
names = re.findall(r"[A-Z][a-z]*",Nameage)
#print(names)

agedict = {}
i = 0
for eachname in names:
    agedict[eachname] = ages[i]
    i = i+1
print(agedict)
#Output:{'Anshul': '10', 'Seby': '9', 'Rithvik': '24', 'Dad': '70'}

#Example-2(Search for pattern)

if re.search("information","we need to give proper information to the trainer"):
    print("We got correct search information")
else:
    print("We dont get reult")
#Example-3(findall option in for loop)
string = "We need to provide latest information to new informatic users"
findallobj = re.findall("inform",string)
for obj in findallobj:
    print("Reult of findall object:",obj)
#Example-4(findout staring and ending of index for pattern using finditer)
str = "we need to inform latest information to him"

for i in re.finditer("inform",str):
    loctup = i.span()
    print(loctup)

#Example-5
str1 = "Sat mat cat rat"
findallobj1 = re.findall("[Smcr]at",str1)
findallobj2 = re.findall("[\w]at",str1)

for string1 in findallobj1:
    print(string1)
for string2 in findallobj2:
    print(string2)
#Example-6

str2 = "sat mat cat rat"
subobj = re.sub("mat","kat",str2)
print(subobj)

#Example-7(Use of raw string and escape backslash
str3 = "this is \\mattino"
findallobj3=re.findall(r"\\mattino",str3)
print(findallobj3)

#Example-8(removing spaces and put in one line
rawstring='''this is testing test line \n
this is other line for testing'''
randstr = re.sub("\n"," ",rawstring)
print(randstr)

#Example-9(it will print length of the string)
rawstring1 = "12345"
print("Matches:",len(re.findall("\d",rawstring1)))

#Example-10(it will give output which starts from 5 to 7
rawstring2 = "123 1234 12345 123456 12345678"
print("Matches1:",len(re.findall("\d{5,7}",rawstring2)))

#Example

