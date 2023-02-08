def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)
f=factorial(5)
print("the factorial is ",f)

#5*4! ->5*24=120
#4*3! ->4*6=24
#3*2! ->3*2=6
#2*1! ->2

RECURSION DATA SAVED IN STACK(LAST IN FIRST OUT)
