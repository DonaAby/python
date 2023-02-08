import mymodule
while True:
    opt = int(input("1.Create\n 2.Search\n3.Remove\n4.Replace\n Enter your choice: "))
    if opt == 1:
        mymodule.create()
    elif opt==2:
        mymodule.search()
    elif opt==3:
        mymodule.delete()
    elif opt==4:
        mymodule.replace()
    else:
        print("enter valid option")
     break

from mymodule import *
while True:
    opt = int(input("1.Create\n 2.Search\n3.Remove\n4.Replace\n Enter your choice: "))
    if opt == 1:
        create()
    elif opt==2:
        search()
    elif opt==3:
        delete()
    elif opt==4:
        replace()
    else:
        print("enter valid option")
     break
