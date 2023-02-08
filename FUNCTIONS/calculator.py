######CALCULATOR################
def addition(a,b):
    print("Sum is:",a+b)
def substraction(a,b):
    print("Difference is:",a-b)
def multiplication(a,b):
    print("Product is:",a*b)
def division(a,b):
    print("Quotient is:",a/b)

n1=int(input("Enter the 1st number"))
n2=int(input("Enter the 2nd number"))
opt=int(input("1.ADDITION\n 2.SUBSTRATION\n 3.MULTIPLICATION\n 4.DIVISION\n ENTER OPTION"))
if opt==1:
    addition(n1,n2)
elif opt==2:
    substraction(n1,n2)
elif opt==3:
    multiplication(n1,n2)
elif opt==4:
    division(n1,n2)
else:
    print("INVALID OPTION")

