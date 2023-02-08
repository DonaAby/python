"""WAP to find all the words in a string that are less than 4 letters using list comprehension"""
str1=input("enter the sentence")
words=str1.split()
print(words)
result=[x for x in words if len(x)<4]
print(result)