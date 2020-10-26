#/usr/bin/python
acoollist = ["superman","spiderman","man",10,20,"spiderman"]
onemorelist = [10,20,30,40,50,20,20]
morelist = [(10,20,30,40),(10,20,30,40)]

print(acoollist.index("man"))  #it will chcek if element or value exist or not
print(acoollist.index(10,0)) #it will chcek if element or value exist or not starts from 0
#print(onemorelist.index("man"))  #If value does not exist it will exception as ValueError