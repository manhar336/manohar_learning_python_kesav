"""
Data Structures: Sets

A set is an unordered collection without duplicates.
A set is eliminating duplicate values

set is not part of data type and used data type
When printed, iterated upon, or converted into a sequence,
its elements will appear in an arbitrary, implementation-dependent order.
"""
"""
1	Convert Iterable into Set 					=		set()
2	Set Union  									=		a_set.union()
3	Set Intersection   							=		a_set.intersection()
4	Set Difference 								=		a_set.difference()
5	Set Symmetric Difference 					=		a_set.symmetric_difference()
6	Set Union with Mutation  					=		a_set.update()
7	Set Intersection with Mutation 				=		a_set.intersection_update()
8	Set Difference with Mutation 				=		a_set.difference_update()
9	Set Symmetric Difference with Mutation      =		a_set.symmetric_difference_update()
10	Add Element into Set                        =		a_set.add()
11	Remove Specified Element from Set           =		a_set.remove(), a_set.discard()
12	Remove Arbitrary Element from Set           =       a_set.pop()
13	Test for Subset                             =		a_set.issubset()
14	Test for Superset                           =		a_set.issuperset()
15	Copy Set                                    =		a_set.copy()
"""

print(set("abcdefabc"))   #it will print only uniq values {'c', 'a', 'b', 'd', 'f', 'e'} example of string
print(set(["abc","def","abc"])) # it will print as {'def', 'abc'} example of list
print(set(("abc","def","abc")))  #it will print as {'def', 'abc'} example of tuple
print(set({1:10,2:20,3:30,2:10})) # it will eliminate duplicate keys  {1, 2, 3}
print(set(enumerate(["abc","def","abc"])))