""""Lambda fn is a small anonymous fn
it can perform only single expression."""
x=lambda a:a+20+10
print(x(4))


y=lambda b,c:b*c
print(y(2,3))

def myfun(n):
    return lambda a:a*n
newfn=myfun(2)
print(newfn(10))
