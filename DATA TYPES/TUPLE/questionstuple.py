#reverse a tuple
# tup=(1,2,3,4,5)
# a=tup[::-1]
# print(a)
#
# #Access 20 from given tuple
# tple=(1,2,40,30,20)
# tple1=(1,2,40,[10,2,39],(30,20,10),40)
# x=tple[4]
# print(x)
# y=tple1[4][1]
# print(y)

# Remove repeated elements from nested tuple
# tple1=(1,2,40,40,5,7,7,9)
# list1=list(tple1)
# print("original list",list1)
# for i in list1:
#     x=list1.count(i)
#     if x>1:
#         list1.remove(i)
# print("new list is ",list1)
# # a=[]
# for i in list1:
#     if i not in a:
#         a.append(i)
# print(tuple(a))



#check if all items in a tuple are same
# tup=(2,2,2,22,33,4)
# f=1
# for i in tup:
#     for j in range(i,len(tup)-1):
#         if tup[i]!=tup[j+1]:
#             f=0
#             break
# if f==1:
#         print("all items are same")
# else:
#
#         print("all items are not same")
#
tple=(1,1,1,1)
tple=set(tple)
if len(tple)==1:
    print("elements are same")
else:
    print("elements are not same")



#copy specific elements from one tuple to a new tuple
# t1=(1,2,3,4,5,6,7)
# print("given tuple is",t1)
# t2=t1[1:6]
# print("new tuple is",t2)
#swap 2 tuples in python
# t1=(10,20,30,40)
# t2=(22,33,44,55)
# print("Before swaping,1st tuple is :",t1)
# print("Before swaping,2nd tuple is  :",t2)
# t1,t2=t2,t1
# print("After swaping 1st tuple is :",t1)
# print("After swaping 2nd tuple is :",t2)