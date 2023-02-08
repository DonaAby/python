"""2 types:-Compile time(eg: fn overloading) & Run time(eg: fn overriding)"""

"""Function overloading(but it python won't support it)"""
# class A:
#     def sum(self,a):
#         print("sum is ",a+a)
#     def sum(self,a,b):
#         print("sum is ",a+b)
# ob=A()
# #ob.sum(10)
# ob.sum(10,20)
#
# class A:
#     def display(self,name=None):
#         if name==None:
#             print("hello")
#         else:
#             print("hello"+name)
# ob=A()
# ob.display()
# ob.display("anu")

"""Function overriding(diff. class,diff fn,same fn name &same signatures)"""
class rectangle:
    def Area(self,l,b):
        print("Area of rectangle is ",l*b)
class square(rectangle):
    def Area(self,l,b):
        print("area of square is ",l*b)
ob=square()
ob.Area(10,20)

