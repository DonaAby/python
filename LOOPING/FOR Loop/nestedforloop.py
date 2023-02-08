#n=int(input("enter rows"))
# for i in range(row): #handles row
#     for j in range(i+1): # handles column
#         print("*",end=" ")
#     print()
#
# for i in range(n):
#     for j in range(n-i):
#         print("*",end =" ")
#     print()

# row=int(input("enter rows"))
# for i in range(0,row+1):
#     for j in range(row+1,):
#         print("*",end=" ")
#     print()
# n=int(input("enter the row value"))
# for i in range(n):
#     for j in range(i+1):
#         print(i+1,end=" ")
#     print()

# print("full pyramid with star(*)")
n=int(input("enter no.of rows"))
for i in range(n): # row
    for s in range(n-i-1): # space calculating
        print("",end=" ")
    for j in range(i+1): #column
        print("*",end=" ")
    print()

    #no.reverse
# n=int(input("enter rows"))
# for i in range(0,n):
#     for j in range(n-i,0,-1):
#         print(j,end=" ")
#     print()

    #no pattern
# n=int(input("enter rows"))
# for i in range(1,n+1):
#     for j in range(i):
#         print(j+1,end=" ")
#     print()
#
# n=int(input("enter value of row"))
# for i in range(n):
#   for s in range(i,n):
#     print("")
#   for j in range(i+1):
#     print(" * ",end=" ")
# print()
