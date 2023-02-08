my_list=[1,2,3,4,"welcome"]
my_list.append("home")
print(my_list)
my_list.remove('home')
print(my_list)
my_list.insert(2,"dona")
print(my_list)
myis=['a','b','c','d']
myis.extend(my_list)
print(myis)
#pop()
a=[1,2,33]
a.pop(2)
print(a)

#clear()
a.clear()
print(a)
#index()
list1=['f','h','i','h','o','w']
print("the count of h is,",list1.index('h'))

#count()
lst=[1,2,3,4,5,4,3,2,1,3,2]
print("count of 4 is:",lst.count(4))

#sort()
list2=[1,5,6,8,9,5,4,2,3]
print("Original list",list2)
list2.sort()
print('sorted list ascending order:',list2)
list2.sort(reverse=True)
print('sorted list',list2)

#reverse()
list3=[1,3,4,7,8,5,2,0]
print('Original list',list3)
list3.reverse()
print('reversed list:',list3)
#copy()
list4=[1,2,3,4]
new_list=list4
new_list.append('a')
print("new list",new_list)
print("old list",list4)
new_list=list4[:]
new_list.append(5)
print("old list:",list4)
print("new list:",new_list)










































































































































#clear

