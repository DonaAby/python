def outer(fun):
    def inner(a,b):
        return fun(a+b)
    return inner
@outer
def double(n):
    print(2*n)
double(2,5)

0