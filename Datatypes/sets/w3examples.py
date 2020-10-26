thisset = {'banana','apple','mango'}
print(thisset,type(thisset))

for x in thisset:
    print(x)

print('banana' in thisset)
print('ban'  not in thisset)

thisset.update(['guava','fruit'])
print(thisset)
print(len(thisset))
print(set(('banana','apple','mango')),type(thisset)) # note the double round-brackets
