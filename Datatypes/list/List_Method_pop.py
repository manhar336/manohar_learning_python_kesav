#/usr/bin/python
acoollist = ["superman","spiderman","man",10,20]
onemorelist = [10,20,30,40,50]

print("deleting  index element  by using pop method:",acoollist.pop(3))
print(acoollist)
print("deleting element without using index value:",onemorelist.pop())
print(onemorelist) #if no index value is specified it will delete last item in the list
#print("deleting index element by using pop method:",acoollist.pop(5)) #IndexError: pop index out of range