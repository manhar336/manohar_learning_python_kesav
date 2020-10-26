#/usr/bin/python
acoollist = ["superman","spiderman","man",10,20]
onemorelist = [10,20,30,40,50]

print(acoollist,list(enumerate(acoollist)),len(acoollist))
print("")
print("removing specific value using remove method",acoollist.remove(10))  #its givining none because its already removed
print("")
print(acoollist,list(enumerate(acoollist)),len(acoollist))

acoollist.remove(30)  #ValueError: list.remove(x): x not in list
print(acoollist)