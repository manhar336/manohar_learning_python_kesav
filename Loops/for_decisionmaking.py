technologies = ("aws","devops","python","bigdata")
for tech in technologies:
    print(tech)              #first it will print aws,devops
    if tech == "python":     #condition is true
        print("welcome to python world")
    elif tech == "bigdata":
        print("weclome to bigdata")
print("Good Bye")
"""
Output
aws
devops
python
welcome to python world
bigdata
weclome to bigdata
Good Bye
"""
print("----------------------------")
for i in range(5):
    print(i)
else:
    print("completed")
"""
Output
0
1
2
3
4
completed
"""
#Nested for loop

"""
A nested loop is a loop inside  a loop
The "inner loop" will be executed one time for each iteration of the "outer loop"
"""
names = ("manohar","anshul","deepika")
surnames = ("dharmala","chinta","goparaju")
for name in names:        #outer loop
    for surname in surnames:  #inner loop
        print(name,surname)   #example manohar will be iterated with each surnames ,asnhul will be iterated with surnames etc
