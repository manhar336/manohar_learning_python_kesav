#/usr/bin/python
student = {"name":"manohar","age":35,"program":"python"}
print("value",student.get("name")) #we can call only keys to get the value of that key
print("keys",student.get("manohar")) #we can not call the values and will give output as NONE
print("value:%s" %(student.get("name")))
print("New Key and Value",student.get("programming","python")) #if key value does not exist it will create temporialrly and assign value
print(student)
print("New Value",student.get("program","java")) #If key already exist means it wont take new value and print old value only
print("")
print("New Value1",student.get("language")) #if key does not exist and does not provide value then it will give as NONE
#print("New Value2",student.get("program","java",".py")) #TypeError: get expected at most 2 arguments, got 3