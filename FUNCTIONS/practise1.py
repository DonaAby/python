"""" WAP to receive 3 integers from user and get their sum and pdt calculated through a user defined fn cal_sum_prod"""
# def cal_sum_prod():
#     a=int(input("enter 1st no"))
#     b=int(input("enter 2nd no"))
#     c=int(input("enter 3rd no"))
#     print("sum is",a+b+c)
#     print("pdt is",a*b*c)
# cal_sum_prod()

""""Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, 
otherwise return False."""
def leapyear():
    y=int(input("enter the year"))
    if (y%4==0 and y%100!=0 or y%400 ==0):
        print("True")
    else:
        print("False")
leapyear()
