print("print union method:",set((10,20,30)))

a = (1,2,3,4,5)
b = (4,5,6,7,8)
print("union method:",set(a).union(set(b)))
print("intersection method:",set(a).intersection(set(b)))
print("difference method:",set(a).difference(set(b)))
print("symmetric differnce:",set(a).symmetric_difference(set(b)))

set1 = set((10,20,30))
set1.remove(30)
print("removing element",set1)

set1.discard(10)
print("discard element:",set1)