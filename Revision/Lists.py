"""
a_list = [10,20,'manohar',"Anshul",(20,30,40)]
print(a_list,type(a_list),list(enumerate(a_list)))
list1,list2 = [10,20,30],['man','ram']
print(list1,list2)
a_list.append(list1)
print("printing append  method in a_list",type(a_list),len(a_list),list(enumerate(a_list)))
print("printing count method in list",a_list.count((20,30,40)))
a_list.extend(list2)
print("printing extend method in list",a_list,list(enumerate(a_list)))
a_list.insert(7,'sita')
a_list.insert(10,[1,2,3,4])
print("printing insert method in a list",a_list,list(enumerate(a_list)))
a_list.pop(9)
print("printing result of pop method",a_list,list(enumerate(a_list)))
a_list.remove(10)
print("printing result of remove method:",a_list,list(enumerate(a_list)))
list2.reverse()
print("printing result of reverse method:",list2,list(enumerate(list2)))
list2.sort()
print("printing result of sort method %s" %(list2))
print("printing result of index method",list2.index('ram'))
print("min value:",min(list1))
print("max value:",max(list1))
"""
list1 = [10,20,30,'Anshul']
list1.append('Manohar')
print("testing append method",list1)
list1.extend('Deepika')
print("testing extend method:",list1)
list1.insert(10,'Dad')
print("testing insert method:",list(enumerate(list1)))
list1.pop(11)
print("testing pop method:",list(enumerate(list1)))
list1.remove('a')
print("testing remove method",list1)
list1.reverse()
print("reverse method",list1)
list2 = [10,20,30]
list2.sort()
print("sort method:",list2)
list3 = []
list3.append(list2)
print(list3)