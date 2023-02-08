#FILTER,MAP,REDUCE can be done from a collection of sequence data
#Filter
l=[10,2,3,4,50,77,11]
lst=list(filter(lambda x:x%2==0,l))
print(lst)

#Map
l=[10,2,3,4,50,77,11]
lst1=list(map(lambda x:x>10,l))
print(lst1)

#Reduce
from functools import reduce
l=[1,2,3,4,5]
pdt=reduce(lambda x,y:x*y,l)
print(pdt)
