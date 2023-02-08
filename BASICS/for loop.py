"""to print fibonacci series using for use range"""
# n=int(input("enter the no"))
# n1 = 0
# n2 = 1
# sum = 0
# for i in range(n):
#     sum = n1 + n2
#     print(n1)
#     n1 = n2
#     n2 = sum

# n = int(input("enter the no"))
# n1 = 0
# n2 = 1
# print("fibonacci series")
# print(n1)
# print(n2)
# for i in range(2,n):
#         sum = n1 + n2
#         print(sum)
#         n1,n2=n2,sum

""" prime no"""
# n=int(input("enter no"))
# f=0
# if n==1:
#     print("not defined")
# else:
#     for i in range(1,n+1):
#         if n%i==0:
#             f=f+1
#     if f==2:
#         print("prime")
#     else:
#         print("not prime")
#
 """for else """
# for i in "python":
#     print(i)
# else:
#     print("completed")
#
"""break"""
# l=[10,20,30,50,100,40,70,80]
# for i in l:
#     print(i)
#     if i==100:
#        break


"""continue"""




# l=[10,20,30,50,100,40,70,80]
# for i in l:
#     if i==100:
#        continue
#     print(i)

""""pass"""
#append elements to an empty list
l=[]
n=int(input("enter the length of list"))

for i in range(n):
    num = int(input("enter the elements"))
    l.append(num)
print(l)