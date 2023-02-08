# tple=(1,2,3,4,5,"dona",2.5)
# print(tple)
# tple1=[1,2,3,4,"abd",5.7]
# print(tuple(tple1))
# print(len(tple1))
# #
# NESTED TUPLE
t1=(1,2,(4,5,4),"abc",5,6)
# print(t1)
# #ACCESSING ELEMENT
# print(tple[0])
# print(tple[-1])
# print(t1[1:3])
# print(t1[::-1])
# print(t1[:-3])
# print(t1[-4:-1])

# #UPDATING
#1 to dona
# y=list(t1)  #converting tuple to list
# y[0]="dona"  #updation
# t1=tuple(y)   #convert list to tuple
# print(t1)

# Check if item exists
# tple = ("apple", "banana", "cherry")
# if "apple" in tple:
#   print("Yes, 'apple' is in the fruits tuple")
#
# # #append
#t2=(1,4,6,8,9,0)
# u=list(t2) #tuple to list
# u.append(6)
# print(u)
# t2=tuple(u) #list to tuple
# print(t2)

#  #addition of 2 tuples or combining without function
# tple1=("pappu","appa")
# t2+=tple1
# print(t2)

# # #remove
# # t=list(t2)
# # t.remove("appa")
# # t2=tuple(t)
# # print(t2)
# #
# # #del
# # newtple=(1,2,3,45,6)
# # print(newtple)
# # del newtple
# # print(newtple)
#
# #Packing (assigning values to variables)
# fruit=("apple","banana","cherry")
# print(fruit)
#
# #Unpacking a tuple
# fruit=("apple","banana","cherry")
# (green,yellow,red)=fruit
# print(green)
# print(yellow)
# print(red)
#
# #Using Asterisk*
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
#
# (green, yellow, *red) = fruits # no:of variables less than values.So adding * to variables
#
# print(green)
# print(yellow)
# print(red)
#
#
# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
#
# (green, *tropic, red) = fruits
#
# print(green)
# print(tropic)
# print(red)
#
# #for loop
# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x)
#
# ### iteration using len() and range
# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#   print(thistuple[i])
#
# #Print all items, using a WHILE LOOP to go through all the index numbers
# thistuple = ("apple", "banana", "cherry")
# i = 0
# while i < len(thistuple):
#   print(thistuple[i])
#   i = i + 1

#
#
# #Nested tuple indexing
# ntple=("DONA",[1,2,3],(8,4,2))
# print(ntple)
# print(ntple[0][3])
# ntple[1][2]=45
# print(ntple)
# #
# #Concatenation
#
#print((1,2,3) + (4,5,6))
#
# #Repeat
#print(("Repeat",)*3)

#
# #Count()
tple=("a","p","p","l","e")
print("the total count of element p is:",tple.count('p'))
#Index()
print("index of l is",tple.index('l'))
