
####CALCULATOR USING DECORATOR
def calculator(func):
    def addition(a,b):
        print("addition : ",a+b)
        return func(a,b)
    return addition
@calculator
def multiplication(a,b):
    print("multiplication : ",a*b)
multiplication(7,5)

def division(a,b):
    print("division : ",a/b)
division(4,8)