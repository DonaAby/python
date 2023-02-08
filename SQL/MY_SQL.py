"""connect front end and back end"""
"""inserting name,age"""
# import pymysql
# db=pymysql.connect(host='localhost',user='root',password='318@Dona',database='nov_test')
# con=db.cursor()
# sqlquery="insert into t1 values(%s,%s,%s)"
# val=(13,'manju',24)
# con.execute(sqlquery,val)
# db.commit()
# print('Inserted')

"""inserting name,age etc from user"""
# import pymysql
# id=int(input("Enter the id :"))
# na=input("Enter the name :")
# ag=int(input("Enter age :"))
# db=pymysql.connect(host='localhost',user='root',password='318@Dona',database='nov_test')
# mycursor=db.cursor()
# sql="insert into t1 values(%s,%s,%s)"
# val=(id,na,ag)
# mycursor.execute(sql,val)
# db.commit()
# print("inserted successfully")

"""delete an id"""
# import pymysql
# id=int(input("Enter the id :"))
# db=pymysql.connect(host='localhost',user='root',password='318@Dona',database='nov_test')
# mycursor=db.cursor()
# sql="delete from t1 where id='%d'"%(id)
# mycursor.execute(sql)
# db.commit()
# print("deleted successfully")

"""updating"""
# import pymysql
# y=input("do u want to update?")
# if y=='yes':
#     db = pymysql.connect(host='localhost', user='root', password='318@Dona', database='nov_test')
#     id = int(input("Enter the id :"))
#     na = input("Enter the name :")
#     ag = int(input("Enter age :"))
#     c=db.cursor()
#     sql="update t1 set name='%s',Age='%d' where id='%d'"%(na,ag,id)
#     c.execute(sql)
#     db.commit()
#     print("table updated")
# elif y=='no':
#     print("exit")

"""select query to take from 1 record"""
# import pymysql
# id = int(input("Enter the id :"))
# db = pymysql.connect(host='localhost', user='root', password='318@Dona', database='nov_test')
# con=db.cursor()
# sql="select * from t1 where id='%d' "%id
# con.execute(sql)
# i=con.fetchone()
# id=i[0]
# na=i[1]
# ag=i[2]
# print(f'id={i[0]}, name={i[1]},age={i[2]}')

"""select query to take all records"""
import pymysql
db = pymysql.connect(host='localhost', user='root', password='318@Dona', database='nov_test')
con=db.cursor()
sql="select * from t1"
con.execute(sql)
data=con.fetchall()
for i in data:
    id=i[0]
    na=i[1]
    ag=i[2]
    print(f'id={id},name={na},age={ag}')