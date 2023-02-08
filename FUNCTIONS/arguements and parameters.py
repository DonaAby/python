#Arguements(args)/positional args
def my_function(msg1,msg2):
    print(msg1 + " " + msg2)
my_function("HI ALL","HOW ARE YOU")

#Arbitary arguements
def my_fun(*names):
    print("Hi",names,"How are u")
my_fun("Jack","Dona")
my_fun("jini")
my_fun("jain")

#Keyword Arguements
def my_function(Name1,Name2,Name3):
    print("last name is "+ Name2)
my_function("Jin",Name3="Jack",Name2="Jerin")

#Arbitary Keyword Arguements(**kwargs)
def my_function(**name):
    print("the last name is" + name["lname"])
my_function(fname="dona",lname="aby")

#Default parameter value
def my_function(country="NORWAY"):
    print("I AM FROM " + country)
my_function("INDIA")
my_function("GERMANY")
my_function()
