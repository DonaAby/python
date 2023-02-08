#Largest number
a=int(input("Enter 1st No.:"))
b=int(input("Enter 2nd No.:"))
c=int(input("Enter 3rd No.:"))
if a>b and a>c:
    print("Largest No. is",a)
elif b>a and b>c:
    print("Largest No. is",b)
else:
    print("Largest No. is",c)