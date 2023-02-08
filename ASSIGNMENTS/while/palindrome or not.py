#str1=input("enter the string")
# rev=str1[::-1]
# if rev==str1:
#     print(str1 + " is Palindrome")
# else:
#     print(str1 + " is not Palindrome")
#
##  OR
n=int(input("enter the number"))
temp=n
s=0
while temp>0:
    a=temp%10
    s=(s*10)+a
    temp=temp//10
if s==n:
    print("p")
else:
    print("np")

