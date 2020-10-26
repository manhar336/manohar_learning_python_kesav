"""
#loop through a dictionary
student = {"name":"manohar","age":35,"course":"python"}
for x,y in student.items():
    print("printing all keys %s and values %s " %(x,y))
#check if key is exist or not
student = {"name":"manohar","age":35,"course":"python"}
if "name" in student:
    print("student name is exist")
#check if key is exist or not and do item assignment
if "name" in student:
    student["name"] = "Anshul"
    print(student)
#Removing items
student.pop("name") #removing items
print(student)

"""
student = {"name":"manohar","age":38}
for x,y in student.items():
     student["name"]="anshul"
     print(student)