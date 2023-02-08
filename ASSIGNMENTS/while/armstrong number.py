n=int(input("enter the number"))
st=len(str(n))
sum=0
temp=n
while temp>0:
    a=temp%10
    sum=sum+(a**st)
    temp=temp//10
if sum==n:
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")
