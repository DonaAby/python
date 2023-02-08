""" SET
1.IMMUTABLE
2.UNORDERED
3.UNINDEXED
4.DON'T ALLOW DUPLICATES
5.Allows different data types
6.Set items are unchangeable,but u can remove items and add items
"""
set1={1,2,3,4,5,6,7}
print(set1)
set1.add(8)
print(set1)
set1.remove(3)
print(set1)
set1={1,3,"hai",(4,5,6)}
print(set1)
a=set([9,10,11])
print(type(a))