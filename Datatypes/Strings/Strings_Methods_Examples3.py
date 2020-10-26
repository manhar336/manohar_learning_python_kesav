"""
name = "Guido Van Rossum"
print("Lower method:",name.lower())  #convert all chars in lower case.
print("")
print("Upper case method:",name.upper())  #conevrts all cahrs in upper case
print()
print("Replace method:",name.replace("Van","Ben"))  #replace with other chars
print()
print("Split method:",name.split(","))

"""
name1 = "aws azure and aws openstack"
print ("find method:",name1.find('aws'))   #searching substring left to right
print("rfind method:",name1.rfind('aws'),len(name1))  #Finding substring right to left
print("index method:",name1.index("azure"))
print("right index method:",name1.rindex("azure"))
print("split method1:",name1.split())  #it will split elements and string converts into list
name2 = name1.split()
print(type(name2))
print("split method2:",name1.split(" "))  #it will split based on spaces and based on parameters
name3 = "ram site @@@lakshman @@@ravana"
print("split method3:",name3.split("@@@")) #it will based on parameter(@@@)
print("split method4:",name1.split(" ",2))  #it will spilt into 2 maximum splits by using space parameter
print("split lines:",name1.splitlines())  #it will print as one element
name4 = "aws\nazure\naws"
print("split lines:",name4.splitlines())  #It will take as 3 elements
pyworld = """
aws
azure
openstack
vmware
"""
print("split lines:",pyworld.splitlines())   #no need to provide \n for next line in triple quotes

pyworld1 = "aws \
            devops \
           vmware \
           openstack"
print("split lines1",pyworld1.splitlines())   #need to provide \ for next line in double quotes

