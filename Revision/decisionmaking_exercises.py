"""
Simple if condition
"""
"""
name = ("Manohar","Anshul","Deepika")

if "manohar" in name:
    print("you are in correct tuple")
list1 = ['abt1','abt2','abt3']

if 'abt1' in list1:
    list1.append('abt4')
    print(list1)

dict1 = {"name":"manohar","lastname":"Dharmala"}

if "name" in dict1:
    print("dictvalues",dict1.items())

name1 = input("enter your name:")

if "Manohar" in name1:
    print("you entered correct name as %s" %(name1))
#If-else statement
"""

'''
course_name = input("enter course name which you wanted to do:").strip().lower()

if course_name== "python":
    print("You entered python course")
elif course_name == "devops":
    print("you are doing Devops")
else:
    print("%s course enntered  by you is not available. Currently , only Python and DevOps available.. "%(course_name))
#list_of_c = ['python','devops','cloud','big data','machine learning']

dict_of_courses = {'1' : 'python','2' : 'devops' , '3' : 'Machine learning'}
print ("following courses are available : " ,dict_of_courses)

course_id = input("\n enter course ID  which you wanted to do:").strip().lower()

if course_id in dict_of_courses :
    print("\n you select course : %s"% dict_of_courses[course_id])
else :
    print("\n Not present")
'''

course_details = {"1":"Python","2":"Devops","3":"Aws"}

print("Courses available in Naresh technoligies are:",course_details)

course_id = input("select course id which you want to do ").lower().strip()
print(course_id)
if course_id in course_details:
    print("you selected %s in Naresh" %course_details[course_id])
    print("you selected one of the best course is:",course_details.get(course_id))
else:
    print("We are on the way to start new course which you selected:")




