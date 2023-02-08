"""Check if 2 lists have common elements"""
l1=[3,2,4,5,6,10,12]
l2=[1,2,3,4,5,9,13]
print("list1 is : ",l1)
print("list2 is : ",l2)
l3=[]
for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i]==l2[j]:
            l3.append(l1[i])
if len(l3)==0:
    print("no common elements")
else:
    print("list of common elements : ",l3)
