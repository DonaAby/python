# sum of n nos
n=int(input("enter the number"))
sum=0
# i=1
# while (i<=n):
#     sum=sum+i
#     i=i+1
# print("the sum is ",sum)

for i in range(n+1):
    sum=sum+i
print(sum)