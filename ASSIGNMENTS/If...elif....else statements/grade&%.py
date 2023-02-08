p=int(input("Enter the physics mark:"))
c=int(input("Enter the chemistry mark:"))
b=int(input("Enter the biology mark:"))
m=int(input("Enter the maths mark:"))
comp=int(input("Enter the computer mark:"))
sum=int(p+c+b+m+comp)
percent=(sum/500)*100
if percent>=90:
    print("GRADE-A")
elif percent>=80 and percent<90:
    print("GRADE-B")
elif percent>=70 and percent<80:
    print("GRADE-C")
elif percent>=60 and percent<70:
    print("GRADE-D")
elif percent>=40 and percent<60:
    print("GRADE-E")
else:
    print("GRADE-F")