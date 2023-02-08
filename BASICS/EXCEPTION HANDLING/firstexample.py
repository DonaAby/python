try:
    a=int(input("enter 1st no. "))
    b=int(input("enter 2nd no. "))
    c=a/b
    print("quotient is ",c)
# except ZeroDivisionError as er:
#     print(er)
# except ValueError as er:
#     print(er)

#if we don't know the errors that will occur,"Exception" will handle all the other errors
except Exception as ex:
    print(ex)