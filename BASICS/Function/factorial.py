""""WAP to find factorial of a no. using function with return type and function parameter"""
def factorial(n):
    a=1
    for i in range(1,n+1):
        a=a*i
    return a
f=factorial(5)
print("factorial is: ",f)
