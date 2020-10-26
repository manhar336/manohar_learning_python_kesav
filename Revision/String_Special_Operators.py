#/usr/bin/python

firstname = "Atchuta"
middlename = "Manohar"
lastname = "Dharmala"
name = firstname + middlename

#Concatenation
print("concatenating 2 strings and can not different data types",name)
print("concatenating other way %s:" %name)

#Repetation
print("Repetation method :",name*2)

#Slicing
print("Slicing Method1",name[2])
print("Sliciing Method2",firstname[-1])

#Range Slicing
print("Range Slicing Method1",name[0:7])
print("Range Slicing methid2",name[0:-1])
print("Range slicing Method3",firstname[-8:-1])

#Zero Based indexing
print("Zerobased indexing",middlename[0::2])

#Formating Method % is called as remainder sign
print("Firstname:%s Middlename:%s Lastname:%s" %(firstname,middlename,lastname),"other string","name:%s" %(name))

# .format method
print("name : {},firstname: {}" .format(name,firstname))

#Raw string r"expression" and R"Expression
print(r"C:\\users\\mdharmal")
print(R"\\manohard")
