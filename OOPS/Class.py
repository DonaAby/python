# class Emp:
#     def display(self):
#         print("simple function")
# obj=Emp()
# obj.display()
#
#
# ######displaying value
# class Emp:
#     x=100
#     def display(self):
#         print("simple function")
# obj=Emp()
# obj.display
# print()
#
# #### WITHOUT SELF ARGUEMENT
# class Emp:
#     def display():
#         print("WITHOUT SELF ARGUEMENT")
# ob=Emp
# ob.display()
#
# ####SUM
# class Emp:
#     def sum(self):
#         print("sum is ",30+20)
# obj=Emp()
# obj.sum()
#
# class Emp:
#     def sum(self,a,b):
#         print("sum is ",a+b)
# obj=Emp()
# obj.sum(30,20)

# class Emp:
#     def sum(self,a,b):
#         print("sum is ",a+b)
#     def pdt(se,a,b):
#         print("pdt is ",a*b)
# obj=Emp()
# obj.sum(30,20)
# obj.pdt(2,5)

##SELF ARGUEMENT
class Emp:
    def read(self,a,b):
        self.x=a  #### "self.x" given to access x anywhere in other functions
        self.y=b  #### if only y, we can't access it anywhere except in read()
    def sum(self):
        print("sum is ",self.x+self.y)  ### to get x& y from read(),want to give self.x and self.y wherever v r using it
    def pdt(c):
        print("pdt is ",c.x*c.y) ###self can have any names."self" is not mandatory."c" also means self.
obj=Emp()
obj.read(10,20)
obj.sum()
obj.pdt()

class Emp:
    def read(self,a,b):
        self.a=a  #### LHS a is the object of the class. RHS a is the variable to which the value is passed
        self.b=b
    def sum(self):
        print("sum is ",self.a+self.b)
    def pdt(c):
        print("pdt is ",c.a*c.b)
obj=Emp()
obj.read(10,20)
obj.sum()
obj.pdt()
