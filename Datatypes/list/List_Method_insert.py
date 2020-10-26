#/usr/bin/python
acoollist = ["superman","spiderman","man",10,20]
onemorelist = [10,20,30,40,50]

print("printing list information",acoollist,type(acoollist),id(acoollist),list(enumerate(acoollist)))
acoollist.insert(4,"hero")
print("")
print("printing list after appending element",acoollist,type(acoollist),id(acoollist),list(enumerate(acoollist)))
print("")
onemorelist.insert(0,[1,2,3,4])  #inserting a list
print(onemorelist)
onemorelist.insert(1,(20,30,40))
print("printing list after appending list",onemorelist)