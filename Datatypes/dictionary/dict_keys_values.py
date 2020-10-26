#/usr/bin/python
languages = {"python":".py",'shell':'.sh',"java":".java"}
print(languages,type(languages),id(languages),dict(enumerate(languages)),len(languages))
print("")
print("printing only  keys:",languages.keys())
print("")
print("printing only values:",languages.values())
#print("calling only one key:",languages.keys("python")) #TypeError: keys() takes no arguments (1 given)
#print("printing specific value",languages.values(".py"))  #TypeError: values() takes no arguments (1 given)
print("getting value:",languages.get("python"))
print("")
#Item Method
print("Item method:",languages.items()) #print in tuple method  like [(),(),()]
