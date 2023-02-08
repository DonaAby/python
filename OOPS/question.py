"""WAP to find factorial of a no using class with fn arguement and return statement"""
# class Number:
#     def fact(self,a):
#         f=1
#         for i in range(1,a+1):
#             f=f*i
#         return f
# obj=Number()
# a=int(input("enter the no."))
# s=obj.fact(a)
# print("factorial is ",s)

###using recursion
class Number:
    def fact(self,x):
        if x==1:
            return 1
        else:
            return x*self.fact(x-1)
obj=Number()
n=int(input("enter the number"))
print("factorial is : ",obj.fact(n))