"""arbitary arguements"""
# def colour(*args):
#     #print(args[0])
#     for i in args:
#         print(i)
# colour("orange","white","green")

# def colour(x,*r):
#     print("normal arguement ",x)
#     for i in r:
#         print(i)
# colour("red","orange","pink","white")

"""keyword arguements"""
# def stud(st1,st2,st3):
#     print("first student",st1)
#     print("2nd st ", st2)
#     print("3rd st ",st3)
# stud(st2="dona",st1="sree",st3="saliha")

def student(**kwargs):
    for i,j in kwargs.items():
        print('%s=>%s'%(i,j) )
student(st1="anu",st2="arya",st3="amaya")

# def student(x,*args,**kwargs):
#     print("simple arguement ",x)
#     for j in args:u
#         print(j)
#     for i, j in kwargs.items():
#         print('%s=>%s'%(i,j) )
# student("anu","vimal","simi",st2="arya",st3="amaya")

""" default parameter value"""
def display(country="INDIA"):
    print("I am from ",country)
display()
display("AMERICA")

def dis(ls):
    for i in ls:
        print(i)
dis([1,2,3,4])

