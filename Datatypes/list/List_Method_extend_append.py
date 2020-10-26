#/usr/bin/python
"""
a_list = [1,2,3]
print(a_list,type(a_list),id(a_list),len(a_list),list(enumerate(a_list)))
print("")

a_list.append(4)  #item assignment is allowed in list and appending numeric value
print(a_list,type(a_list),id(a_list),len(a_list),list(enumerate(a_list)))
print("")

a_list.append((5,6,7))    #appending tuple
print(a_list,type(a_list),id(a_list),len(a_list),list(enumerate(a_list)))
print("")
a_list.append([5,6,7])    #appending list
print(a_list,type(a_list),id(a_list),len(a_list),list(enumerate(a_list)))
print("")
a_list.append("Guido")    #appending string
print(a_list,type(a_list),id(a_list),len(a_list),list(enumerate(a_list)))

a_list = ["python","linux",100,200]
print(a_list)

del a_list[0]   #item assignment deletion is possible in list but not possible in strings and tuple
print(a_list)

del a_list    #we can delete total variable also
"""
acoollist = ["superman","spiderman","Spiderman","man"]
onemorelist = [10,20,30,10,50]
print(acoollist.count('superman'))   #takes case sensitive
print(acoollist.count('ma'))         #if element not exist print as 0
print(onemorelist.count(10))

acoollist.extend(onemorelist)   #extend means joining them together
acoollist.append("test2")
print(acoollist)