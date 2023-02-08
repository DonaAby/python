"""Constructors-member functions of a class.
It is defined by __init__(self)
2 types:-  1.Non parameterized constructor
            2. Parameterized constructor"""

#non parameterized constructor/Default constructor
class A:
    def __init__(self):
        print("Non parameterized constructor")
ob=A()

#parameterized constructor
class A:
    def __init__(self,name):
        print("Parameterized constructor")
        self.na=name
    def display(self):
        print("Name is ",self.na)
ob=A("Dona")
ob.display()
