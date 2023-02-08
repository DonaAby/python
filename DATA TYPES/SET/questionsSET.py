"""
1.add a list of elements to a set
2.get only unique items from 2 sets
3.check if 2 sets have any elements in common.if yes,display the common elements
4.remove items from set1 that are not common to both set1 and set2
"""
# add a list of elements to a set
set1={7,8,9,10}
list1=[1,2,3,4]
set1.update(list1)
print(set1)
print(type(set1))

#unique items from 2 sets
set1={1,2,3,4}
set2={4,5,6,7,2}
print("Unique",set1|set2)
print(set1.union(set2))

#elements in common
set1={1,2,3,4,5}
set2={5,4,7,8,9}
if set1.isdisjoint(set2):
    print("2 sets have no common items")
else:
    print("2 sets have common items")
print("common items are",set1&set2)

 # remove not common
set1={1,2,3,4,5}
set2={3,4,6,7,8}
print("Items",set1&set2)
print(set1.intersection(set2))