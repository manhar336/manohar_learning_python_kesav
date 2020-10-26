"""
#Loop controls: break and continue
technologies = ("aws","devops","python","bigdata")
for tech in technologies:
    print(tech)
    if tech == "python":
        print("welcome to python world")
        break    #Break means it will terminate the program and dont go next step
    if tech == "bigdata":
        print("welcome to bigdata")

print("---------------------------------")
courses = ("c#","java","devops","hadoop")
for cour in courses:
    print(cour)
    if cour == "c#":
        print("welcome to C#")
        continue    #continue means program will continue till last value of the variable
    if cour == "hadoop":
        print("welcome to hadoop")
print("---------------------------------")
fruits = ("mango","banana","grapes")
for fruit in fruits:
    if fruit == "banana":
        print("I am banana")
        continue
"""
tech = "AWS","DevOps","python"
for tec in tech:
    if tec == 'DevOps':
        print("you are good")
        continue
    else:
        print("you too good")