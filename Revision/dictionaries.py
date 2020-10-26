dict1 = {}
dict1['name'] = 'manohar'
dict1['age'] = 38
print(dict1,type(dict1),dict(enumerate(dict1)),id(dict1))
dict1['name'] = 'Anshul'
dict1['age'] = 8
print(dict1,type(dict1),id(dict1),len(dict1))
del dict1['age']
print("clearing dictonary",dict1,type(dict1),id(dict1),len(dict1))
dict1.clear()
print("clearing dictionary",dict1,type(dict1),id(dict1),len(dict1))
dict2 = dict1.copy()
print("copying dictionary",dict2,type(dict2),id(dict2),len(dict2))
dict3 = {"python":".py",'Devops':'dev','Java':'.java'}
print("New dictionary",dict3,type(dict3))
print("Getting values using get method1:",dict3.get('python'))
print("Getting values using get method2:",dict3.get('cloud','aws'),dict3)
print("Getting keys in dict",dict3.keys())
print("Getting values in dict3",dict3.values())
print("Using Items method in dict",dict3.items())
for x,y in dict3.items():
    print("keys:{} and values:{}" .format(x,y))
if "python" in dict3:
    print("Getting value",dict3.get('python'))
tup1=(1,2,3,4)
dict4 = dict.fromkeys(tup1)
print("Using fromkeys method:",dict3.fromkeys('Java','Ja'))
print("Using fromkeys method1:",dict4.fromkeys(tup1,'numbers'))
dict5 = {"name":"manohar"}
dict5.update(dict3)
print("combing 2 dict",dict5)
print("set default method:",dict5.setdefault('name1','Anshul'),dict5)