# Pgm to print all unique values in a dictionary

# listofdict=[{"V":"SOO1"},{"V":"S002"},{"VI":"SOO1"},{"VI":"S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
# setof_values=set()# set won't allow duplicates
# for i in listofdict:
#     for j in i.values():
#        setof_values.add(j)
# print(setof_values)

#                      OR
# dic=[{"V":"SOO1"},{"V":"S002"},{"VI":"SOO1"},{"VI":"S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
# ul=[]
# for i in dic:
#     ul.extend(list(i.values()))
# ul=set(ul)
# print(ul)

#Pgm to combine values in python list of dictionaries
dict1=[{"item":"item1","amount":400},{"item":"item2","amount":300},{"item":"item1","amount":750}]
print("the given dictionary is:",dict1)
lst={}
for i in dict1:
    if i['item'] not in lst:
        lst[i["item"]]=i["amount"]
    else:
        lst[i["item"]]+=i["amount"]
print(lst)
# newdict={}
# list1=[]
# for d in dict1:
#     p=list(d.values())
#     list1.append(p[0])
#     list1.append(p[1])
#     print(list1)
# for i in range(0,len(list1),2):
#     if list1[i] in newdict:
#         rep = list1[i]
#         index = list1.index(rep)
#         list1[index+1]=list1[index+1]+ list1[i+1]
#         newdict[list1[i]]=list1[index+1]
#     else:
#         newdict.setdefault(list1[i],list1[i+1])
# print("the combined dictionary is:",newdict)

#Pgm to create a dictionary from string

# str1=input("enter the string")
# print("the given string is ",str1)
# dict1={}
# for index in range(1,len(str1)+1):
#     dict1.setdefault(index,str1[index-1])
# print("the corresponding dictionary of the given string is : ",dict1)

#Pgm to print a dictionary in table format
#
# dict1={"MATHS":87,"SCIENCE":90,"ENGLISH":95,"MALAYALAM":100}
# print("SUBJECT\t\t\t\t\tMARKS\n****************************")
# for key,value in dict1.items():
#     if key == "MATHS":
#         print(key,"\t\t\t\t\t\t",value)
#     else:
#         print(key,"\t\t\t\t\t",value)

#Pgm to print a dictionary line by line

# dict1={"MATHS":87,"SCIENCE":89,"ENGLISH":95,"MALAYALAM":99}
# name="HAVILLAH"
# print("Student name: ",name)
# for key,value in dict1.items():
#     print("The student scored ", value, "marks in subject ",key)

#Pgm to sort(ascending and descending) a dictionary by value
#
# dict1={1:2, 3:4, 4:3, 2:1, 0:0 }
# print("the given dictionary is :",dict1,"\n")
# val=list(dict1.items())
# print(val)
# newval=[]
# newvalf=[]
#
# for i in val:
#     irev=i[::-1] # interchange keys and values
#     newval.append(irev)
# #print(newval)
# val.clear()
# newval.sort()
# print("newval sorted based on key",newval) # sorting based on values
#
# for i in newval:
#     irevf=i[::-1]
#     val.append(irevf)
# print("val-sorted based on value",val)
#
#
# for i in (newval[::-1]):
#     i=i[::-1]
#     newvalf.append(i)
# print("newvalf",newvalf)
#
# print("the dictionary in ascending order by value is :",dict(val),"\n")
# print("the dictionary in descending order by value is :",dict(newvalf))

#Pgm to concatenate 2 dictionaries to create a new one

# dict1={"Name":"Dona","Age":28, "Place":"Kochi"}
# dict2={"Institution":"Luminar","Qualification":"B.Tech,MBA"}
# print("The first dictionary is :",dict1)
# print("The 2nd dictionary is :",dict2)
# dict1.update(dict2)
# print("The concatenated dictionary is:",dict1)

#Pgm to sort by values
#
# dict1={1:2, 3:4, 4:3, 2:1, 0:0 }
# print("the given dictionary is:",dict1,"\n")
# val=list(dict1.values())
# print(val)
# val.sort()
# print(val)
# rev=[]
# for i in val:
#
#     revval=i[::-1]
#     rev.append(revval)
#     print(revval)