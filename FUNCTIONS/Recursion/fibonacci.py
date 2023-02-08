def fib(n):
    if n==1:
        return n
    else:
        result=[]
        a,b=0,1
    while b<n:
        result.append(b)
        a,b=b,a+b
    return result
print(fib(5))