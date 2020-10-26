# A for loop is used for iterating a seqeunce i.e a list,a tuple,a dict,a string,numbers and a set
"""
for = keyword
: = suit
in = operator

Synatax of for loop:

for variable_expression operator variable_name suit
    statements
"""
technologies = ["cloud","DevOps","BigData"]

for tech in technologies:   #example of iterated to variable
    print(tech)
for tup in (10,20,30,40,50):  #example of iterated to tuple
    print(tup)
for lists in [1,2,3,4,5]:  #example of iterated to list
    print(lists)
for string in ["test","test1","test2"]:  #example of iterated to  string
    print(string)
for dictionary in {"name":"manohar","course":"python"}: #example of iterated to  dictionary
    print(dictionary)

for i in range(1,10):   #start element and end element-1 :10-1=9
    print(i)