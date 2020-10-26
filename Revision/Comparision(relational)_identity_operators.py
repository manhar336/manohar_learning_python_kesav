x = [1,2,3,4]
y =  [1,2,3,4]

a = {"name":"manohar","sonname":"Anshul"}
b = {"name":"manohar","sonname":"Anshul"}

A = 10
B = 20

name = "manohar"
name1 = "manohar"
print("x is equal to y:",(a==b),id(a),id(b))
print("x is not equal to y:",(a!=b))
print("x is greater than y:",(x>y))
print("A is greater than B",(A >B))
print("x is less than y",(x>y))
print("A is less than B",(A < B))
print("A is not equal to B:",(A!=B))

print("x is y by checking identity operators",x is y)
print("x is not equal to y by checking identity operators:", x is not y)

print("A is not B",A is not B)
print("name is name1",name is name1)
