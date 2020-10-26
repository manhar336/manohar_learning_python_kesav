#From keys method
tup_01 = ("name","age","address")   #Tuple Variable
list_01 = ['python','java','c']
dict_01 = dict.fromkeys(tup_01)  #part of Built-in function i.e dict() calling tuple variable
dict_02 = dict.fromkeys(list_01)  #part of built in function i.e dict() calling list variable
print("New dictionary coverts from tuple:%s" %(dict_01))   #it will convert as dictionary from tuple and print values as NONE
print("")
print("New dictionary coverts from list:%s" %(dict_02))   #it will convert as dictionary from list  and print values as NONE
print("")
dict_02 = dict.fromkeys(tup_01,"pyworld")  #Here passing pyworld as value for all keys
print(dict_02)
#dict_03 = dict.fromkeys(tup_01,"py","py1") #Here we can not pass 2 keys TypeError: fromkeys expected at most 2 arguments, got 3
#Update Method
pystudents = {"name":"Guido","middlename":"Van","lastname":"Rossum"}
javastudents = {"name1":"manaohar","lastname1":"dharamala"}
pystudents.update(javastudents)  #It will Join 2 dictionaries
print("update method:%s" %(pystudents))
print("")
#setdefault method
print("Setdefault method:",pystudents.setdefault("name",'manohar')) #Here we can not change values alerady exist keys
print("setdefault method1:",pystudents.setdefault("course","python")) # Hered we can create new key and assign value


