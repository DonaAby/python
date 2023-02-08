"""WAP to extract numbers from a string using list comprehension"""
str1=input("enter the string")
new=[x for x in str1 if x.isdigit()]
print(new)