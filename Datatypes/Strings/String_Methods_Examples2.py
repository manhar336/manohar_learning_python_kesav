name = "Guido Van Rossum"
name1 = "version36"
name2 = "Python 36"
name3 = "100"
#Note: which we define inside "" is called as string

print("Isalnumeric method:",name.isalnum())  #condition fails because name does not have numeric value
print("Isalnumeric method1",name1.isalnum()) # condition should pass because name1 contains alpha and numeric
print("Isalnumeric method2:",name2.isalnum()) #condition fails because space(special chars) contains
print("")
print("Isnumeric method:%i" %(name3.isnumeric())) #condition pass because variable contains only integer value
print("Isnumeric method:%d" %(name.isnumeric()))  #condition fail because variable conatins only chars and special chars as well
print("")
print("Isdigit method:",name3.isdigit())  #condition pass because variable conatins integer value
print("")
print("Isdecimal method:",name3.isdecimal()) #isdigit and isdecimal both are similar
print("")
print("Islower method:",name.islower())  #condition is false because name contains upper case as well.
print("")
print("Isupper method:",name.isupper())  #condition is false because name conatins lower case as well
print("islower method:",name1.islower())  #condition is true because name contains lowercase
print("swap case method:",name.swapcase()) #changes swap the chars
print("")
name4 = "  "
print("Isspace method1:",name4.isspace(),len(name4),type(name4),id(name4)) #checks only if we have any empty space
print("Isspace method2:",name.isspace())  #condition fails because we have char plus space
print("")
print("Istitle method:",name.istitle())   #condition is pass because each word contains capital letter
print("Istitle method2:",name1.istitle()) #condition fails because starting word does not contain  capital letter
print("")
#print("Ljust method:",name.ljust(20,'test'))  #Error The fill character must be exactly one character long
print("Ljust method:",name.ljust(20,'m'))      #char m will fill 4 times on left hand side .
print("")
print("Rjust method : %s" %(name.rjust(20,'g')))  #char will fill 4 times on right hand side
strip_method = "      Guido Van Rossum       "
print("lstrip method:",strip_method.lstrip()) # will remove spaces by default  on left hand side.
print("rstrip method",strip_method.rstrip())  #will remove spaces by default on right hand side.
print("strip method:",strip_method.strip())   #will remove spaces by default on both sides
strip_method1 = "0000Guido####"
print("lstrip method:",strip_method1.lstrip('0'))  #will remove 0 in left hand side.
print("rstrip method:",strip_method1.rstrip('#'))   #will remove # in right hand side.
print("strip method:",strip_method1.strip('0'))
strip_method2 = "0$#Guido0$#"
print("lstrip method:",strip_method2.lstrip('0$'))  #will delete only from left to right and based on fill with chars
print("rstrip method:",strip_method2.rstrip("0$#"))  #will delete only 0$# on right hand side.
print("strip method:",strip_method2.strip('0$#'))    #will delete 0$# on both sides.
print("")
print("min value:",min(name))   # will print space as its min value
print("max value:",max(name))   # will print u as its nax value based on ASCII value
#Note:we can not use min and max functions for combination of string and integer
number = '0123456789'
print("min value:",min(number))
print("max value:",max(number))
print("replace text:",name.replace("V","H"))