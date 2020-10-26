#Access items in list
thislist = ["apple","mango","banana"]
print(thislist[1])
print("")
#change item value
thislist[1]="grapes"
print(thislist)
print("")
#loop through a list
for x in thislist:
    print(x)
print("")
#check if item exists
if "apple" in thislist:
    print("yes,apple is there in the list")
#Add items
thislist.append("rawbanana")
print(thislist)
#To add an item in specified index
thislist.insert(0,"bananas")
print(thislist)
#To remove the specified item
thislist.remove("banana")
print(thislist)
#pop method removes based on index
thislist.pop(0)
print(thislist)
#clear method in list
#thislist.clear()
#print(thislist)
#copy method
acoollist = thislist.copy()  #copy list into another list
print(acoollist)
#Make a copy of a list with the list() method
acoollist1= list(thislist)
print(acoollist1)
#The List() constructor
thislist = list(("apple","banana"))  #double round brackets
print(thislist)