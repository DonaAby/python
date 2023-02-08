""" wap to check if a no is positive,negative or zero"""
#
# a=int(input("enter the no"))
# if a>0:
#     print("Number is postive")
# elif a<0:
#     print("Number is negative")
# else:
#     print("Number is zero")


"""" largest of 3 nos using nested if"""
a=int(input("enter the 1st no"))
b=int(input("enter 2nd no"))
c=int(input("enter 3rd no"))
if a>b:
    if a>c:
        print("largest no is",a)
    else:
            print("largest no is ",c)
elif b>c:
        print("largest no is ",b)
else:
    print("largest no is ",c)