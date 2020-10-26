student = {"Name":"Anshul","Age":8,"class":"4th"}
print("student name:",student["Name"])
print("student age:",student["Age"])
print("Student class:",student["class"])

del student["Name"]  #deleting entry using key "Name"
print(student)
#del student["Anshul"]   #We can not delete by using value
student.clear()  #remove all entries in dictionary
print(student)
del student      #delete entire dictionary
#print(student)

#Copy Method
dict1 = {"name":"GuidoVanRossum"}
dict2=dict1.copy()
print("copy nethod:",dict2)