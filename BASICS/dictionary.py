# dict1={}
# n=int(input("enter the no. of elements in dictionary:"))
# for i in range(n):
#     key=int(input("enter key:"))
#     value=input("enter value :")
#     dict1.update({key:value})
# print(dict1)

d={1:"green",2:"red"}
x=d.get(2)
print(x)

""""tuple"""
t=(100,200,300)
print(t)
print(t[2])

"""set"""
s={10,20,30,40}
print(s)
for i in s:
    print(i)