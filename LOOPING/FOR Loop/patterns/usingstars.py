# SQUARE USING *
# n=int(input("Enter the rows"))
# for i in range(n):
#     for j in range(n):
#         print("*",end="")
#     print()

# #############################################
# RIGHT ANGLED TRIANGLE USING *
# n=int(input("Enter the rows"))
# for i in range(0,n):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# ###########################################
# UPSIDE DOWN RIGHT ANGLED TRIANGLE USING *
# n=int(input("Enter the rows"))
# for i in range(n):
#
#           for j in range(n-i):
#
#               print("*",end=" ")
#           print()
# #######################################
# RIGHT ANGLED TRIANGLE ON RIGHT SIDE USING *
# n=int(input("enter the rows"))
# for i in range(n):
#     for s in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# #########################################
#UPSIDE DOWN RIGHT ANGLED TRIANGLE ON RIGHT SIDE USING *
# n=int(input("Enter the rows"))
# for i in range(n):
#     for s in range(i):
#         print("",end=" ")
#     for j in range(n-i):
#         print("*",end="")
#     print()

# ##########################################
# PYRAMID USING *
# n=int(input("Enter the rows"))
# for i in range(n):
#     for s in range(n-i-1):
#         print("",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# # ########################################
#INVERTED PYRAMID USING *
n=int(input("Enter the rows"))
for i in range(n):
    for s in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print(" * ",end=" ")
    print()
