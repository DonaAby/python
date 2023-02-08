#Pgm to convert a string into tuple
# str1=input("Enter the string")
# print("The string is:",str1)
# tple=tuple(str1)
# print("The corresponding tuple is:",tple)
# print(type(tple))
#
# #Pgm to convert list to tuple
# list1=[1,2,3,4,5,6,]
# print("The list is:",list1)
# tple1=tuple(list1)
# print("The corresponding tuple is:",tple1)
# print(type(tple1))

#Pgm to find repeated items from  tuple
tup=(1,2,3,4,5,1)
c=set()
for i in tup:
    if tup.count(i)>1:
        c.add(i)
print("The repeated items are",tuple(c))


