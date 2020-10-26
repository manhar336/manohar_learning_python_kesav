#!/usr/bin/python

name = "guido van Rossum"
print("Capitalize method:",name.capitalize())  #Converts first letter to capital and if its alerady capital letter no changes
print("")
print(type(name),len(name),id(name))  #Here type,len and id are built in functions
print("Center Method:",name.center(22,'$'))  # Here name varilable len is 16 and fill with chars 22 ,so 22-16 =6 chars
print("Center Method:",name.center(22))      # If we dont input any fill with chars ,its takes as space
print("")
print("Count Method1:",name.count('m',0,17))  #It will count how many time m(sub string) occured and 0=start index and 17=end index
print("Count Method2:",name.count('o',0))
print("Count Method3:",name.count('guido'))    # No need to give start and end index also
check = 'o'
print("Count Method4:",name.count(check))    #Here check is variable name
print("")
print("Starts with method 1:",name.startswith('Guido',0,20))  #condition is false because Guido
print("starts with method 2:",name.startswith('guido'))      #condition is true
print("starts with method 3:",name.startswith('van',0))      #condition is false
print("")
print("Ends with method 1",name.endswith('rossum'))   #condition is false
print("Ends with method 2:",name.endswith('Rossum'))  #condition is true
print("")
print("Find method1:",name.find('van'))    #print index value of van
print("Find Method2:",name.find('Guido',0,17))  #print value as -1 as Guido not exist
print("")
print("Index method1:",name.index('guido'))   #print index value
#print("Index method2:",name.index("VAN"))     # it will give exception error
