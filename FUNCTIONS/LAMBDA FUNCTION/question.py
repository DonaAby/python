# """"wap to create a fn that takes one arguement and that arguement will be multiplied with an unknown given no."""
# def mul(n):
#     return lambda a:a*n
# pdt=mul(2)
# print(pdt(5))
#
# """"wap to filter even nos from  a list of integers using lambda
# hint: use filter function in lambda"""
# def filter1():
#     num=[1,2,3,4,5,6,7,8,9]
#     even=list(filter(lambda a:a%2==0,num))
#     print(even)
# filter1()
#
# """"wap to filter odd nos from a list using lambda"""
# num1=[1,2,3,4,5,6,7,8,9]
# odd=list(filter(lambda a:a%2!=0,num1))
# print(odd)
#
# """"lambda with if else condition"""
# maxi=lambda a,b:a if(a>b) else b
# print(maxi(4,9))
#
# maxi=lambda a,b,c:max(a,b,c)
# print(maxi(3,5,8))

maxi1=lambda a,b,c: a if(a>b and a>c)else b if (b>a and b>c) else c
print(maxi1(3,5,7))