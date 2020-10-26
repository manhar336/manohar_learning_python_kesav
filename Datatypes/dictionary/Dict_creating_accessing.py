"""

dict1 = {"name":"manohar","age":35,"employee":"cisco"}
print(dict1,type(dict1),id(dict1),len(dict1),dict(enumerate(dict1)))
#note name,age and employee are keys and manohar,35,cisco are values .
#Here we have 3 elements like "name":"manohar", "age":35 and "employee":"cisco"

#item assignment
dict1["age"]= 32  # update existing value
print(dict1)
print("")
dict1['home'] = 'ulsoor' #creating new keys and values
print(dict1)

print("getting age:",dict1["age"])
print("getting address:",dict1["home"])

"""
"""
dict2 = {}
print(dict2,type(dict2),id(dict2))
dict2["firstname"] = "manohar"
dict2["lastname"]  = "dharmala"
print(dict2,type(dict2),id(dict2),dict(enumerate(dict2)))
"""
dict1 = {}
dict1['first'] = 'manohar'
dict1['last'] = 'dharmala'
print(dict1)