
#/usr/bin/python

tup1 = ("dharmala","""manohar""",1982,2010,19.5)  #we can use combination of strings and numbers

tup2 = 10,20,30,40,50       #need to use comma separator for tuple

print(tup1,tuple(enumerate(tup1)),type(tup1),id(tup1))
print("\n")
print(tup2,tuple(enumerate(tup2)),type(tup2),id(tup2))
print("\n")
print(tup1[-3],tup1[0:4])  #printing using slicing and range index
tup3 = ("manohar","""dharmala""",[1.2,3,4])
print(tup3,type(tup3))

#del tup1    # deleted tup1 and delete is built in function
#del tup1[0]   #Typeerror:tuple object doesn't support item deletion and can't delete only element
print(tup1) #we can not get variable

list1 = [1,2,3,4]
print(list1,type(list1),list(enumerate(list1)))

tup4 = tuple(list1)   #converting list into tuple
print(tup4,type(tup4),tuple(enumerate(tup4)))

tup5,tup6 = ("ram","sita","lakshman"),(1,2,3,4,5)  #other way of defining tuple
print(tup5,tuple(enumerate(tup5)))
print(tup6,tuple(enumerate(tup6)))
