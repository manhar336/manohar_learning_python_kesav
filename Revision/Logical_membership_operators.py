x = True
y = False
print("and Logical operator: ",x and y)
print("or logical operator:",x or y)
print("not logical operator:",not x or not y)

a = "Anshul".lower()
b = 10
c = (10,20,30,40)
d = [1,2,3,4]
e = {"name":"ram","name1":"sita"}

print("in memmbership operator using string:","a" in a)
print("not in membership operator using string:","A" not in a)
print("in membership operator using tuple",(10  in c))
print("not in membership operator using tuple: ",(00 not in c))
print("in membership operator using list:",(10 in d))
print("not in membership operator using list ",(10 not in d))
print("in membership operators:",("name" in e))
print("not in membership operator:","nam" not in e)