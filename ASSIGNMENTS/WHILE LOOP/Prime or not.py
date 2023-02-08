n=int(input("enter the no."))
count=0
i=2
if (n==0 or n==1 or n==2):
    print(n,"is neither prime nor composite")
while i<n:
    if n%i==0:
        count=1
        print(n,"is not a prime number")
    i=i+1
    if count==0:
        print(n,"is a prime number")