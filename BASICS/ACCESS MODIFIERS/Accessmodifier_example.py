#super class
class A:
    #public data member
     var1=None

    #protected data member
     _var2=None

    #private data member
     __var3=None

    #constructor
     def __init__(self,var1,var2,var3):

         self.var1=var1
         self._var2=var2
         self.__var3=var3

    #public member function
     def displayPublicMembers(self):
        #accessing public data members
         print("Public data member: ",self.var1)

    #protected member function
     def _displayProtectedMembers(self):
        #accessing protected data members
        print("Protected data member: ",self._var2)

    #private member function
     def __displayPrivateMembers(self):
        #accessing private data members
        print("Private Data member: ",self.__var3)

    #public member function
     def accessPrivateMembers(self):
        #accessing private member function
        self.__displayPrivateMembers()

#derived class
class B(A):

    #constructor
    def __init__(self,var1,var2,var3):
        A.__init__(self,var1,var2,var3)

    #public member function
    def accessProtectedMembers(self):
        #accessing protected member functions of super class
        self._displayProtectedMembers()

#creating objects of the derived class
obj=B("Pub_Red","Pro_White","Private_Green")

#calling public member functions of the class
obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()
#obj.accessPrivateMembers()
#object can access public member
print("Object is accessing public member : ",obj.var1)
#object can access protected member
print("Object is accessing procted member: ",obj._var2)

#object can't access private member,so it will generate attribute error
#print(obj.__var3)
print(obj._A__var3) #Accessing NAME MANGLED Variables

"""NAME MANGLING"""
"""A process in which any given identifier with one trailing underscore and two leading underscores
is textually replaced with the _CLASSNAME__Identifier is known as NAME MANGLING.
In _CLASSNAME__IDENTIFIER name,Classname is the name of the current class where identifier is present"""