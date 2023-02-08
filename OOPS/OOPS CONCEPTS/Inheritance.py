
"""SINGLE INHERITANCE"""
# class A:
#     def displayA(self):
#         print("Base class method")
# class B(A):
#     def displayB(self):
#         print("Derived class method")
# ob=B()
# ob.displayA()
# ob.displayB()


# class A:
#     def read(self):
#        self. x=int(input("enter the no"))
#        self. y=int(input("enter the no"))
#
# class B(A):
#     def sum(self):
#         print("sum of 2 nos is ",self.x+self.y)
# ob=B()
# ob.read()
# ob.sum()

"""MULTILEVEL INHERITANCE"""
# class A:
#     def read(self):
#         self.x=int(input("enter 1st no"))
#         self.y=int(input("enter 2nd no"))
# class B(A):
#     def sum(self):
#         print("sum of nos is ",self.x+self.y)
# class C(B):
#     def avg(self):
#         print("avg of nos is ",(self.x+self.y)/2)
# ob=C()
# ob.read()
# ob.sum()
# ob.avg()


"""HIERARCHICAL INHERITANCE"""
# class A:
#     def read(self):
#         self.x=int(input("enter 1st no"))
#         self.y=int(input("enter 2nd no"))
# class B(A):
#     def sum(self):
#         print("sum of nos is ",self.x+self.y)
# class C(A):
#     def avg(self):
#         print("avg is ",(self.x+self.y)/2)
# class D(A):
#     def pdt(self):
#         print("pdt is ",self.x*self.y)
# ob=B()
# ob.read()
# ob.sum()
# ob1=C()
# ob1.read()
# ob1.avg()
# ob2=D()
# ob2.read()
# ob2.pdt()

"""MULTIPLE INHERITANCE"""
class A:
    def read(self):
        self.name=input("enter name ")
        self.age=int(input("enter age"))

class B:
    def salary(self):
        self.desg=input("enter designation")
        self.sal=int(input("enter salary"))
class C(A,B):
    def details(self):
            print("Employee Details")
            print(f'NAME:{self.name} \n AGE :{self.age} \n DESIGNATION :{self.desg} \n SALARY: {self.sal} ')
ob=C()
ob.read()
ob.salary()
ob.details()