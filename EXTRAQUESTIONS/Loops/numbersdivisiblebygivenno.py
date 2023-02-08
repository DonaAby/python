"""Python pgm to print all nos in a range divisible by a given no. """
lower=int(input("enter lower limit"))
upper=int(input("enter upper limit"))
n=int(input("enter the no to be divided by:"))
for i in range(lower,upper+1):
    if i%n==0:
        print(i)
