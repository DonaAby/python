"""create list"""
l=[]
def create():
    n=int(input("enter the length of list"))
    for i in range(0,n):
        l1=int(input("enter the elements"))
        l.append(l1)
    print(l)
#create()

"""search an element in list"""
l2=[10,20,30,40,50,60]
def search():
    n=int(input("enter the number to be found"))
    if n in l2:
        print("element found")
    else:
        print("element not found")
#search()


"""remove an item from list"""
l3=[5,10,15,20,25,30]
def delete():
    n=int(input("enter the item to be removed"))
    if n in l3:
        l3.remove(n)
    else:
        print("item not found")
    print(l3)
#delete()


"""replace a particular item with another"""
l4=[2,4,6,8,10]
def replace():

    old=int(input("enter the item to be replaced"))
    new=int(input("enter the item to be added"))
    for i in range(len(l4)):
        if l4[i]==old:
           l4[i]=new
    print(l4)
#replace()


while True:
    opt=int(input("1.Create\n 2.Search\n3.Remove\n4.Replace\n Enter your choice: "))
    if opt==1:
        create()
    elif opt==2:
        search()
    elif opt==3:
        delete()
    elif opt==4:
        replace()
    else:
        print("Enter a valid option")
    break
        
