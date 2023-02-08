#LIST COMPREHENSION
#Syntax:list=[expression for item in list if condition]
# l=[x+3 for x in [1,2,3]]
# print(l)


""" WAP to print all even nos below 25 using list compreshension"""
# l=[x for x in range(25) if x%2==0]
# print(l)
#
# """WAP TO return all vowels in  a string using list comprehension"""
# str1=input("enter the string")
# v=["a","e","i","o","u"]
# l=[x for x in str1 if x in v ]
# print(l)
#
# ####or
#
# l=[x for x in str1 if x in ["a","e","i","o","u"] ]
# print(l)
#
# """WAP to return the first char of each word in the string entered using list comprehension"""
# str2="hai how are you"
# words=str2.split()
# firstletter=[i[0] for i in words]
# print(firstletter)
#
# """WAP  to return the elements from the colours that have "e" in it"""
# colours=["red","white","green","pink"]
# ret=[x for x in colours if "e" in x]
# print(ret)
#
# """WAP to print all colours except "green" in given list """
# colours=["red","white","green","pink"]
# ret=[x for x in colours if x!="green"]
# print(ret)
#
# """WAP to convert all elements to uppercase"""
# colours=["red","white","green","pink"]
# ret=[x.upper() for x in colours ]
# print(ret)
#
# """WAP to replace all elements with a new word"""
# colours=["red","white","green","pink"]
# ret=["hello" for x in colours]
# print(ret)
#
# """ if else condition"""
# colours=["red","black","pink","green"]
# newlist=[x if x!="pink" else "blue" for x in colours]
# print(newlist)

words="hai how are you"
answer={word:len(word) for word in words}
print(answer)