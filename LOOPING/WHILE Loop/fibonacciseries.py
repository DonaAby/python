n = int(input("enter the number"))
n1 = 0
n2 = 1
# sum = 0
#
# while n1<=n:
#     sum = n1 + n2
#     print(n1)
#     n1 = n2
#     n2 = sum
print(n1,n2)
for i in range(2,n):
    sum=n1+n2
    print(sum)
    n1,n2=n2,sum