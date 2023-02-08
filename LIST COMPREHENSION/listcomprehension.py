""""List comprehension offers a shorter syntax when you want to create a new list based on the
values of an existing list.
The Syntax
newlist = [expression for item in iterable if condition == True]
The return value is a new list, leaving the old list unchanged.

"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
#
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
#
# print(newlist)
# #############list comprehension
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#
# newlist = [x for x in fruits if "a" in x]
#
# print(newlist)

#Return "orange" instead of "banana":
newlist=[x if x!="banana" else "orange" for x in fruits]
print(newlist)