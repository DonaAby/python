import datetime
print(dir(datetime))#prints all the function names in datetime
now=datetime.datetime.now()#representing a single point in time including date and time
crnt_date=datetime.date.today() #represents a date(yy-mm-dd) without time
print(crnt_date)
print(now)