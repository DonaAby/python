"""The map() function executes a specified function for each item in an iterable.
The item is sent to the function as a parameter."""

def myfunc(a,b):
    return a+b
x=map(myfunc,("apple","banana","cherry"),("orange","pineapple","mango"))
print(list(x))

#using lambda
list_a = [1, 2, 3]
list_b = [10, 20, 30]

d=map(lambda x, y: x + y, list_a, list_b)
print(list(d))
