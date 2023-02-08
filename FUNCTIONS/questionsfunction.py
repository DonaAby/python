""""
1. WAP function to find the max of 3 nos.
2. WAP function to sum all the nos. in a list.
3. WAP function to multiply all the nos. in a list"""

#max of 3 nos
# n1 = int(input("enter the 1st number"))
# n2 = int(input("enter the 2nd number"))
# n3 = int(input("enter the 3rd number"))
# def maximum(n1,n2,n3):
#
#
#  d=max(n1,n2,n3)
#
#  print("max of 3 nos is", d)
# maximum(n1,n2,n3)


###sum of all nos in a list
# def sum():
#  s=0
#  for i in l2:
#   s=s+i
#   # i=i+1
#  return s
#
# l2=[1,2,3,4]
# print(sum())
 #OR
#
# def sum(l2):
#  s=0
#  for i in l2:
#   s=s+i
#   i=i+1
#  return s
# print(sum([1,2,3,4,5]))

##multiply all the nos in a list
def mul(l1):

 r=1
 for i in l1:
  r=r*i
  i=i+1
 return r
print(mul([1,2,3,4]))
