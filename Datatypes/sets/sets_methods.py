#Union Method
print("union method1:",set([1,2,3,4,5]).union(set((6,7,8,9))))  #it will combine 2 sets {1, 2, 3, 4, 5, 6, 7, 8, 9}
a=(10,20,30,40)
b=(40,50,60)
print("union method2:",set(a).union(set(b)))

#Intersection
x=(10,20,30,40)
y=(40,50,60)
print("Intersection method",set(x).intersection(set(y)))   #it will give common number
#Difference
print("Difference method:",set(x).difference(set(y)))  #it will print only uniq values of set x,it will do difference and print only x which not exitst in y

c=[1,2,3,4,5]
d=[1,2,3,4,5,6,7]
print("printing difference value",set(c).difference(set(d)))
#Symmetric difference
print("symmetric difference method",set(x).symmetric_difference(y)) #It will print uniq values of set x and uniq values of set  y
#Note:in difference print only uniq values of x and in symmetric difference print uniq value of x and uniq value of y
#Update Method
s1 = set([1,2,3,4,5])
s1.update(set([5,6,7]))
print("update method",s1)
#Intersection_update
s2 = set([1,2,3,4,5])
s2.intersection_update([5,6,7])
print("intersection update",s2)
#Note intersection update and intersection both are same
#Different update
s3=set([1,2,3,4,5])
s3.difference_update([5,6,7])
print("difference_update",s3)
#Note in difference update it will print only uniq values
#Symmetric difference update
s4=set([1,2,3,4,5])
s4.symmetric_difference_update([5,6,7])
print("symmetric difference_update",s4)

#Note in symmetric difference update it will print uniq values of 2 sets
#add method
s5 = set([1,2,3,4])
s5.add('test')
print("add method",s5)

#Remove method
s6 = set([1,2,3,4])
s6.remove(4)
print("remove method",s6)

#if you want to remove element if its does not exist it will throw exception

#Discard method
s7 = set([1,2,3,4,5])
s7.discard(5)
print("discard ",s7)
s7.discard(8)
print("discard ",s7)
#Note in discard method if element does not exist it wont throw any exception but in remove method it will give type error

#pop() method
s8 = set([1,2,3,4,5])
s8.pop()  #in set pop method it will delete 1st element but in list method it will delete last element
print(s8)  #in set pop method we can not pass argument if we pass it will thrpugh exception

#issubset method()
s9 = set([1,2,3,4])
print("is subset method:",s9.issubset(s9))  #Here condition is same means both sets have same value
s10 = set([10,20,30])
s11 = set([6,7,8,9])
print("is subset method1:",s10.issubset(s9)) #Here 2 sets are different means values are not same ,so condition is false
print("is subset method2:",s9.issubset(s11))  #Here condition is false
s12 = set([10,20,30,40,50])
print("is subset method3:",s10.issubset(s12))  #Here condition is True

#Issuperset method()
s13 = set([1,2,3,4,5])
print("is superset method1",s13.issuperset([1,2,3,4,5]))  #Here condition is True because both sets are mathcing

s14 = set([1,2,3,4,5])
s15=  set([1,2,3,4,5,6,7])
print("is superset method2:",s14.issuperset(s15))  ##Here condition is false because s14 set is not mathcing with s15

s16 = set([1,2,3,4,5,6,7])
s17=  set([1,2,3,4])
print("is superset method3:",s16.issuperset(s17))  #Here condition is True because s16 elements are matching with s17

#Copy() method

s18 = set([1,2,3,4,5,6,7])
s19 = s18.copy()
print(s18,id(s18),type(s18))
print(s19,id(s19),type(s19))
print(s18 is s19)  #condition is false because both have different id's

