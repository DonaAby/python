"""Reverse of a no."""
n=int(input("enter the number"))
rev=0
while n>0:
    r=n%10
    rev=(rev*10)+r
    n=n//10
print("reverse is ",rev)

""""Product of each nos in a number"""
# n=int(input("enter no"))
# p=1
# rev=0
# while n>0:
#     r=n%10
#     rev=(rev*10)+r
#     p=p*r
#     n=n//10
# print("the pdt is ",p)

"""" Sum of each nos in a number"""
n=int(input("enter no"))
sum=0
rev=0
temp=n
while temp>0:
    r=temp%10
    rev=(rev*10)+r
    sum=sum+r
    temp=temp//10
print(f'the sum of digits of {n} is ',sum)
