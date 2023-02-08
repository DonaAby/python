"""1.	Remove empty strings from a list of strings
Str1 = [“John”, “ ”,“Jack”,”Emma”,” ”,”Jins”,”Lina”]
o/p: Str1 = [“John”,“Jack”,”Emma”,”Jins”,”Lina”]
"""

# Str1 =["John"," ","Jack","Emma"," ","Jins","Lina"]
# print("original string is",Str1)
# while(" " in Str1):
#     Str1.remove(" ")
# print("New string is",Str1)

""""
2.	Write a python code to remove all the repeating letters from each words of a given sentence.
Eg:
   			i/p:Let’s google the pineapple
 			o/p:Let’s gole the pineal
 			"""
#
# str1="Let's google the pineapple"
# str2=str1.split()
# print(str2)
# str3=[]
# for i in str2:
#     l=" "
#     for j in i:
#         if j in l:
#
#              continue
#          else:
#              l=l+j
#     str3.append(l)
# print(" ".join(str3))

#3.	Replace each special symbol with # in the following string
 #  str1 = '/*Jon is @developer & musician!!'
 # o/p:    ##Jon is #developer # musician##


# str1='/*Jon is @developer & musician!!'
# spc=["/","*","@","&","!"]
# for i in str1:
#     for j in spc:
#         if j==i:
#             str1=str1.replace(i,"#")
# print(str1)



# nstr=str1.replace('/','#')
# #print(nstr)
# nstr1=nstr.replace('*','#')
# #print(nstr1)
# nstr2=nstr1.replace('@','#')
# #print(nstr2)
# nstr3=nstr2.replace('&','#')
# #print(nstr3)
# nstr4=nstr3.replace('!','#')
# print(nstr4)


# Reverse a list in python
# list1=[100,200,300,400,500]
#
# list1=[100,200,300,400,500]
# rev=list1[::-1]
# print("Reversed list is",rev)


# extend nested list by adding sublist
 #list1 = ["a","b",["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sublist=["h","i","j"]

# list1=["a","b",["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sublist=["h","i","j"]
# #print(list1[2][1][2])
# list1[2][1][2].extend(sublist)
# print("new list is",list1)

