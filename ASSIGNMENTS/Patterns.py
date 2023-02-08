
#DIAMOND PATTERN
#n=int(input("Enter the rows"))
# for i in range(n):
#     for s in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print(" * ",end=" ")
#     print()
# for i in range(n):
#     for s in range(i):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print(" * ",end=" ")
#     print()
# ######################################################+

#SAND GLASS PATTERN
# n=int(input("Enter the rows"))
# for i in range(n):
#     for s in range(i):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print(" * ",end=" ")
#     print()
# for i in range(n):
#     for s in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print(" * ",end=" ")
#     print()

############################################################
#INVERTED FULL HALF PYRAMID
# n=int(input("enter rows"))
# for i in range(n):
#     for s in range(i):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print(" * ",end=" ")
#     print()

#########################################################
#HALF PYRAMID WITH NUMBERS
# n=int(input("enter the number"))
# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end="")
#
#     print()

###############################################

# NUMBER PATTERN FROM 1 TO 10
# n=int(input("Enter the number"))
# for i in range(0,n,1):
#     for j in range(0,i+1,1):
#         print(j,end=" ")
#     print()
################################################
#REVERSE NUMBER PATTERN FROM 10 TO 1
# n=int(input("Enter the no."))
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()
###########################################
#ABC HOLLOW PATTERN
# n=int(input("enter the no:"))
# for i in range(0,n):
#     k = ord("A") + i
#     for j in range(0,n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print(chr(k),end=" ")
#         else:
#             print(" ",end=" ")
#     print()

######################################################
# HOLLOW DIAMOND PATTERN
# for i in range(5):
#     for j in range(5):
#         if i+j==2 or j-i==2 or i-j==2 or j+i==6:
#             print(" *",end="")
#         else:
#             print(end="  ")
#     print()

########################################################

#RIGHT ANGLED PATTERN WITH ABC..
# n=int(input("Enter the rows"))
# k=ord("A")
# for i in range(n):
#     for j in range(i+1):
#
#         print(chr(k),end=" ")
#         k=k+1
#     print()

############################################################

#EQUILATERAL TRIANGLE PATTERN USING ABC..
# n=int(input("Enter the rows"))
# k=ord("A")
# for i in range(n):
#     for s in range(n-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print(chr(k),end=" ")
#         k=k+1
#     print()

#############################################################

#CROSS NUMBER PATTERN
# #
# n=int(input("enter the rows:"))
# for i in range(1,n+1):
#     for s in range(i):
#         print(" ",end="")
#     for j in range(1):
#         print(i,end="")
#     print()
#
# for i in range(n-1,0,-1):
#         for s in range(i):
#             print(" ", end="")
#         for j in range(1):
#             print(i, end=" ")
#         print()
#
# if (i!=n-1):
#         for k in range(1,n,-2):
#
#             print(" ", end=" ")
#         else:
#
#             print(i,end=" ")
#             i=i+1

#
#
#

#####################################################
#HEART SHAPE
# m=5
# for i in range(2,m):# cutting first 2 rows for heart
#     for s in range(m-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print("* ",end="")
#
#
#
#     for b in range(m-i-1):
#         print("  ",end="")
#     for c in range(i+1):
#         print("* ",end="")
#     print()
# n=10
# for i in range(n):
#     for s in range(i):
#         print(" ",end="")
#     for j in range(n-i):
#         print("* ",end="")
#     print()

############################################################

# LETTER D PRINTING
# for i in range(7):
#     for j in range(5):
#         if(j==0) or (j==4 and (i!=0 and i!=6)) or ((i==0 or i==6) and (j>0 and j<4)):
#             print(" * ",end=" ")
#         else:
#             print("   ",end=" ")
#     print()

#############################################################

# # printing name as hollow square
str1=input("enter the name:")
st=len(str1)
#print(st)
a=str1.upper()
for i in range(st+2):
    for j in range(st):
        if i==0 or i==st+1:
            print(a[j],end=" ")
        elif j==0 or j==st-1:
            print(a[i-1],end=" ")
        else:
            print(" ",end=" ")
    print()
##########################################
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#          ch=chr(64+i)
#          if (i==1 or i==n or j==1 or j==n):
#               print(ch,end=" ")
#           else:
#               print(" ",end=" ")
#     print()


