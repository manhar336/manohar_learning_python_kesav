"""
#Creating a Function
def os(name):
    print(name)
    return

#Creating a variable
#version = os('redhat')
version = 'redhat'
list1 = [1,2,3,4]
list1.append('test')
tup1 = (10,20,30,40)
dict1 = {'name':"manohar",'lastname':'dharmala'}

#Accessing/calling a function
os('centos')
os(version)
os(list1)
os(tup1)
os(dict1.get('name'))
"""
def manohar(name):
    print(name)
    return

list=[1,2,3]
manohar('dharmala')
manohar(list)

def os(name,*name2):
    print("firstargument",name)
    for x in name2:
        print(x)
    return
os('red','blue','yellow','white')
