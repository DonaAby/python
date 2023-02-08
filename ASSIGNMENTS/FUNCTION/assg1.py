#reverse a string
#1234abcd => dcba4321

# str1=input("enter the string")
# def reve(str1):
#     reverse=str1[::-1]
#     print("reverse is",reverse)
# reve(str1)

#factorial
# num=int(input("enter the number"))
# def fact(num):
#     fact=1
#     for i in range(1,num+1):
#         fact=fact*i
#     print("factorial is",fact)
# fact(num)

""""
create outer fn passes parameter a,b
inner fn to add a+b
return a+b add5"""
# def func(a,b):
#     def sum():
#         c=a+b
#         return c
#     return sum()+5
#
# print("sum is",func(2,3))

# prime number
n=int(input("enter the number"))
def prime(n):
    if(n==1):
        print("1 is neither prime nor composite")
    elif(n<1):
        print("enter the positive value")
    elif n==2:
        print("2 is a prime no")
    else:
        flag=1
        for j in range(2,n):
            if n%j==0:
                flag=0
                break
            else:
                continue
        if flag==0:
            print(f"the number{n} is not prime")
        else:
            print(f"the no. {n} is prime")
prime(n)

##python list to generate even nos btw 2 nos
# strt=int(input("enter the starting number"))
# stop=int(input("enter the finishing number"))
# def evnnos(a,b):
#     v=[]
#     for i in range(a,b+1,2):
#         v.append(i)
#     return v
# print("even nos are",evnnos(strt,stop))

