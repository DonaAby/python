"""Write a Python program to access a function inside a function"""
# def outerfn(a,b):
#     def innerfn():
#         c=a+b
#         return c
#     return innerfn()
# print(outerfn(5,6))


""""Write a Python function to create and print a list where the values are
    square of numbers between 1 and 30(both included)"""
# def square(n):
#     result=[]
#     for i in range(n):
#         a=i*i
#         result.append(a)
#     print(result)
# square(31)

""""Assign a different name to function and call it through the new name"""
def func(a,b):
    print(a+b)

newname=func
newname(4,5)

"""Python function that accepts two numbers as arguments and returns the sum"""
# def sum(n1,n2):
#     s=n1+n2
#     print("sum is", s)
#     return s
# sum(10,5)

"""Python function that accepts different values as parameters and returns a list"""
def lst(a,b,c):
    l=[a,b,c]
    return l
print(lst(2,3,"dona"))

"""Python function that returns a tuple"""
def tple(a,b,c):
    t=(a,b,c)
    return t
print(tple(1,2,3))

"""Define a function that accepts 2 values and return its sum, subtraction and multiplication"""
def operations(a,b):
    print("sum : ", a+b)
    print("substraction : ",a-b)
    print("multiplication : ",a*b)
operations(5,4)

"""Define a function that accepts roll number and returns whether the student is present or absent"""
def students(rollno):
    i=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    if rollno in i:
        print("the student is present")
    else:
        print("the student is absent")
rollno=int(input("enter the roll no."))
students(rollno)

"""Define a function which counts vowels and consonant in a word"""
def fn(str1):
    str1=str1.lower()
    c=0
    v=0
    for i in range(0,len(str1)):
        if str1[i] in ['a','e','i','o','u']:
            v=v+1
        else:
            c=c+1
    print("no.of vowels is ",v)
    print("no:of consonants is ",c)

str1=input("enter the word: ")
fn(str1)

############OR
def con():
    str1 = input("enter string")
    ch=['a','e','i','o','u']
    c=0
    v=0
    str2=str1.lower()
    for i in str2:
        if i in ch:
            v=v+1
        else:
            c=c+1
    print("cons",c)
    print("vow",v)
con()

"""Define a function that accepts a number and returns whether the number is even or odd"""
def evenodd(n):
    if n%2==0:
        print("the number is even")
    else:
        print("the number is odd")
n=int(input("enter the no"))
evenodd(n)

"""Define a function in python that accepts 3 values and returns the maximum of three numbers"""
def maxi(a,b,c):
    return max(a,b,c)


print(maxi(2,4,7))
