choice=input("Enter your choice: +,-,*,/")

a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
if choice=='+':
    print("Sum is:", a+b)
elif choice=='-':
    print("Difference is:",a-b)
elif choice=='*':
    print("Product is:",a*b)
elif choice=="/":
    print("Qoutient is :",a/b)
else:
    print("INVALID")