def fact(n):
    if n==1:
        return 1

    else:
        x=n*fact(n-1)
        print(x)
        return x

print(fact(5))