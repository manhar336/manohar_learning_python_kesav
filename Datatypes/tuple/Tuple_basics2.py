#Iterate through the items and print the values:
thistuple = ("apple","mango","guava")
for x in thistuple:
    print(x)


#Check if item exists

thistuple = ("apple","mango","guava")
if "apple" in thistuple:
    print("yes,its exists")

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)