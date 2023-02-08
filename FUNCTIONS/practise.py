# def square(n):
#     a=n*n
#     return a
# print("square is",square(9))

# str2=input("enter the string")
# def length():
#
#     lenth=len(str2)
#     return lenth
# print("length is",length())

# n1=int(input("enter the 1st no"))
# n2=int(input("enter 2 no"))
# n3=int(input("enter 3 nos"))
# def maxi(n1,n2,n3):
#     d = max(n1,n2,n3)
#
#
#     print("max is",d)
# maxi(n1,n2,n3)

# def sumlist(l):
#     s=0
#     for i in l:
#         s=s+i
#         i=i+1
#     return s
#
# print("sum is ",sumlist([1,2,3,4,5]))
# def mul(l):
#     m=1
#     for i in l:
#         m=m*i
#         i=i+1
#     return m
# print("pdt is",mul([1,2,3,4,5]))

# def addition(a,b):
#     print("sum is",a+b)
# def subtr(a,b):
#     print("dif",a-b)
# def mul(a,b):
#     print("pdt",a*b)
# def div(a,b):
#     print("quo",a/b)
#
# n1=int(input("enter 1 no"))
# n2=int(input("enter 2 no"))
# ch=int(input("1.add 2.sub 3.mul 4.div \n enter opt"))
# if ch==1:
#     addition(n1,n2)
# elif ch==2:
#     subtr(n1,n2)
# elif ch==3:
#     mul(n1,n2)
# elif ch==4:
#     div(n1,n2)
# else:
#     print("enter valid option")

# def mul(l):
#     m=1
#     for i in l:
#         m=m*i
#         i=i+1
#     return m
# print("pdt is",mul([1,2,3,4]))

# str1=input("enter the str")
# def rev():
#     r=str1[::-1]
#     return r
# print("rev str is",rev())
#
# def fact(n):
#    f=1
#    for i in range(1,n+1):
#        f=f*i
#        i=i+1
#    return f
# print("factorial is",fact(5))

# def prime(n):
#     if n==1:
#         print("1 is neithr prime nor composite")
#     else:
#         flag=1
#         for i in range(2,n):
#             if n%i==0:
#                 flag=0
#                 break
#             else:
#                 continue
#         if flag==0:
#             print("not prime")
#         else:
#             print(" prime")
# prime(11)
#
# s=int(input("enter start"))
# e=int(input("enter stop"))
# # def evn(a,b):
#     v=[]
#     for i in range(a,b+1,2):
#         v.append(i)
#     print(v)
# evn(s,e)

# def outerfn(a,b):
#     def innerfn():
#         e=a+b
#         return e
#     print(innerfn())
# outerfn(5,6)

# def square(n):
#     l=[]
#
#     for i in range(1,n+1):
#         sq=i*i
#
#         # return sq
#
#
#         l.append(sq)
#     print(l)
# square(30)

# def sum(a,b):
#     s=a+b
#     return s
# print("sum is",sum(4,5))

# def list1(n1,n2):
#     l=[n1,n2]
#     return l
# print(list1(2,3))
#
# def tple(a,b,c,d):
#     t=(a,b,c,d)
#     return t
# print(tple(1,2,3,4))
#
# def opt(a,b):
#     print("sum",a+b)
#     print("dif",a-b)
#     print("pdt",a*b)
# opt(3,4)
#
# def con():
#     str1 = input("enter string")
#     ch=['a','e','i','o','u']
#     c=0
#     v=0
#     str2=str1.lower()
#     for i in str2:
#         if i in ch:
#             v=v+1
#         else:
#             c=c+1
#     print("cons",c)
#     print("vow",v)
# con()

# def odd(n):
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")
# odd(87)
#
# def maxi(a,b,c):
#     return max(a,b,c)
# print(maxi(2,3,4))

# n=int(input("enter the row"))
# for i in range(n):
#     for j in range(n):
#         if j==0 or i==n-1 or i==j:
#             print(" *",end=" ")
#         else:
#             print(end="   ")
#     print()

# n=int(input("enter the row"))
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==n-1 or i==j:
#             print("*",end="  ")
#         else:
#             print(end="   ")
#     print()

# for i in range(0,4):
#     for j in range(0,7):
#         if i==3 or j+i==3 or j-i==3:
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()
# n=int(input("enter the rows"))
# #m=int(input("enter rows"))
# for i in range(2,n):
#     for s in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("* ",end=" ")
#
#     for b in range(n - i - 1):
#         print("  ", end=" ")
#     for a in range(i+1):
#         print("* ",end=" ")
#
#     print()

# for i in range(m):
#     for s in range(i):
#         print(" ",end=" ")
#     for j in range(m-i):
#         print("* ",end=" ")
#
#     print()

for i in range(7):
    for j in range(5):
        if j==0 or (j==4 and i!=0 and i!=6) or (i==0 and j!=4) or (i==6 and j!=4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()