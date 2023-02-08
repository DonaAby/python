#
# t1=(1,2,3,4,5)
# print("Length is",len(t1))
# print(all(t1))
# print("Max is",max(t1))
# print("Min is ",min(t1))
# print(sorted(t1))
# print("Sum is ",sum(t1))
# #
# x=("python","java","express")
# y=enumerate(x)
# print(tuple(y))
#
# names=["mukish","rony","charls"]
# age=[12,34,56]
# for i,(names,age) in enumerate(zip(names,age)):
#     print(i,names,age)

#Enumerate
# letter=[('a','A'),('b','B')]
# for i,letter in enumerate(letter):
#     #print(i,letter)
#     print("Letter %d is %s/%s" %(i,letter[0],letter[1]))

#Mapping
l=['sat','bat','cat','mat']
#map() can listify the list of strings individually
#test=list(map(tuple,l))
test=list(map(list,l))
print(test)