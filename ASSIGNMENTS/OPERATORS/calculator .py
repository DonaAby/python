#CALCULATOR USING OPERATORS
#arithmetic operators
num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
sum=num1+num2
print(num1, "+" ,num2, "=",sum)
difference=num1-num2
print(num1,"-",num2,"=",difference)
product=num1*num2
print(num1,"*",num2,"=",product)
quotient=num1/num2
print(num1,"/",num2,"=",quotient)
modulus=num1%num2
print(num1,"%",num2,"=",modulus)
exponent=num1**num2
print(num1,"**", num2,"=",exponent)
floordivision=num1//num2
print(num1,"//",num2,"=",floordivision)

#assignment operators
num1+=num2
print(num1)
num1-=num2
print(num1)
num1=num2
print(num1)
num1*=num2
print(num1)
num1/=num2
print(num1)
num1//=num2
print(num1)

#comparison operators

print(num1>=num2)
print(num1<=num2)
print(num1==num2)
print(num1<num2)
print(num1>num2)
print(num1!=num2)

#logical operators

print(num1>num2 and num1<=num2)
print(num1<=num2 or num1>=num2)
print(not(num1>num2 or num1<num2))


-