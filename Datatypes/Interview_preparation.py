"""
print("This is part of interview preparation")
print('this is part of zoom preparation')
"""
firstname = "manohar"   #left operand = name of the variable and right operand = value of the variable
lastname = 'dharmala'
fullname = " Manohar Dharmala "
splitexample = "('python','python2','python3')"
atuple="tuple1","tuple2","tuple3"
alist=[1,2,3,"manohar"]
alist1 = [4,5,6,'dharmala']
alist2 = [1,2,3,4,0,7,6]
dict1 = {"name":"manohar","name1":"anshul"}
dict2 = {"name2":"deepu","name3":"dharmala"}
print(firstname)
print(lastname)
print("calling firstname",firstname)
print(firstname,"we have called firstname")
print("firstname",firstname,"lastname",lastname)
print("firstnme:%s and lastname:%s"%(firstname,lastname))
name = firstname + lastname
print("full name",name)
repetation= firstname*5
print("repeat",repetation)
print("slicing",lastname[5])
print("slicing2",lastname[0:5])
print("slicing3",lastname[:2])
print("slicing4",lastname[-6:-1])
print("slicing5",lastname[0:])
print("zerobased indexing",lastname[0::2])
print(".format method firstname:{},lastname:{}".format(firstname,lastname))
print(r"rawstring:c:/users/mdharmal")
print("string datatype",firstname,type(firstname),id(firstname))  #id prints memory
print("capitalize method:",firstname.capitalize())
print("count method:",firstname.count('a'))
print("find method:",firstname.find('a'))
print("strip method:",fullname.strip())
print("max method:",max(firstname))
print("split method:",splitexample.split(","))
print(type(atuple),id(atuple),len(atuple),tuple(enumerate(atuple)))
print("list method:",alist,type(alist),id(alist),list(enumerate(alist)))
alist.append('rao')
print("adding append in list method",alist,len(alist))
print("count method in list",alist.count('ra'))
alist.extend(alist1)
print("extend method in list",alist,len(alist))
alist.insert(0,'a')
print("insert method in list",alist)
print("count method in list",alist.count('a'))
print("pop method in list",alist.pop(0),alist,list(enumerate(alist)))
print("remove method in list",alist)
alist2.sort()
print("sorting method",alist2)
print("index method in list",alist2.index(7))
print("dictionary",dict1.values(),len(dict1),dict1['name'],dict1['name1'])
print("get in dictionary",dict1.get('name'))
dict1.update(dict2)
print("update in dictionary",dict1)
dict2["name2"] = "deep"
print(dict2)
print("manohar" in firstname or "tuple1" in atuple)