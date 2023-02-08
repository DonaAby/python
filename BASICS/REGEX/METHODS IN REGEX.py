"""FINDALL()"""
import re
# str1="rose is a beautiful and colourful flower"
# s=re.findall("ful",str1)
# print(s)
# s1=re.findall("full",str1)
# print(s1)

# d="cat mat pat rat sat"
# a=re.findall('[scr]a',d)
# print(a)
#
# d="cat mat pat rat sat"
# a=re.findall('[^scr]',d)
# print(a)

# d="cat mat pat rat sat 99988 999"
# a=re.findall('\d{3}',d)
# print(a)
#
# d="cat mat pat rat sat 99988 999 6666"
# a=re.findall('\d{1,4}',d)
# print(a)
#
# d="cat mat pat rat sat 99988 999 6666"
# a=re.findall(r"\b\d{4}\b",d)
# print(a)

"""SEARCH()"""
# str1="class will start at 10 am"
# s=re.search("\s",str1)
# print(s)
# print(s.start())
#
# s1=re.search("\d",str1)
# print(s1.start())
#
# s2=re.search('python',str1)
# print(s2)

# str1="class will start at 10 am"
# s=re.search("^class.*10am$",str1)
# if s:
#     print("Find")
# else:
#     print("not find")

"""SPLIT()"""
# str1="class will start at 10 am"
# s=re.split(" ",str1)
# print(s)
#
# s1=re.split("a",str1)
# print(s1)
#
# s2=re.split(" ",str1,2)
# print(s2)

"""FULLMATCH()"""
str1="python is a lang"
b=re.fullmatch(str1,"python is a lang")
print(b)

"""SUB()"""
# input="rose and jasmine are flowers"
# g=re.sub(" ","*",input)
# print(g)
#
# g=re.sub(" ","*",input,3)
# print(g)

