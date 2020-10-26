firstname = "Guido"
middlename = "Van"
check = "van"
name = "    Guido Van Rossum   "
name1 = "Guido1985"
print("Capitilaize method:",firstname.capitalize(),middlename.capitalize())
print("Center Method:",firstname.center(10,'&'),middlename.center(6,'$'))
print("Count Method:",firstname.count('o',0,10),middlename.count('z'))
print("Startswith Method:",firstname.startswith('Guido'),middlename.startswith('van'))
print("Endswith Method:",firstname.endswith('Guido'),middlename.endswith(check))
print("Find Method:",firstname.find('o'),middlename.find('v',0,20))
'''print("Index Method:",firstname.index('u',0,20),middlename.index('v'))'''
print("isalphanumeric method:",name1.isalnum(),"and",name.isalnum())
print("isalpha method:",name.isalpha(),firstname.isalpha())
print("isnumeric method:",name.isnumeric())
print("isdecimal method:",name.isdecimal())
print("isupper method:",name.isupper())
print("islower method:",check.islower())
print("isswapcase method:",name.swapcase())
print("isspace method:",name.isspace())
print("istitle method:",name.istitle(),check.istitle())
print("leftjustification",name.ljust(20,'&'))
print("right justiification",middlename.rjust(20,'#'))
print("strip method:",name.strip())
print("rstrip method:",name.rstrip())
print("max value:",max(name))
print("min value",min(name1))
print("find method:",name.find('Guido'))
print("rfind method:",name1.rfind('5'))
print("index method:",name1.rindex('5'))
fruits = "Apple,mango,banana,grapes"
chars = "$$$$$name$$$$"
print("split method2:",name.split("  "))
print("Split method3:",chars.split('$$$$'))
fruits_split = fruits.split(',')
for sp in fruits_split:
    print(sp)
print("split lines method:",name.splitlines(4))