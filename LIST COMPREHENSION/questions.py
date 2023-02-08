"""" take even and odd nos from list"""

# list1=[x for x in range(101) if x%2==0]
# print(list1)
# list2=[x for x in range(100) if x%2==1]
# print(list2)
#
# newlist=[y for y in range(100) if y%2==0 if y%5==0]
# print(newlist)

"""" sum of 1st 10 nos"""
# sumlist=sum([x for x in range(11)])
# print(sumlist)
# sumlist=sum([x for x in range(1,int(input("enter the range")+1)])
# print(sumlist)
print((n*(n+1)/2) for n in range(1,int(input("enter no."))+1))