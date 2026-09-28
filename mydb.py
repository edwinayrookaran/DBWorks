import mysql.connector

# con=mysql.connector.connect(user="root",password="root",host="localhost")
#         #establish connection between python code and mysql server
#         #it returns a connection object
#
# print(con)
# #
# #
# c=con.cursor() #used to execute sql queries/commands
#
# #c.execute(command)
#
# #create database file
# c.execute("create database school_db")
# print("database created")


# con=mysql.connector.connect(user="root",password="root",host="localhost",database="school_db")
# c=con.cursor()
# c.execute('create table student(roll_no int not null primary key,name varchar(20),age int,place varchar(20),phone varchar(20),total_mark int)')
#
# print("table created successfully")

# c.execute('''
# insert into student(roll_no,name,age,place,phone,total_mark)
#             values(101,'arun',11,'ekm','7846378962',145),
#             (102,'amal',12,'ekm','9846384678',140),
#             (103,'anu',11,'tvm','9673867345',147),
#             (104,'hari',12,'tcr','9736456123',144),
#             (105,'manu',11,'ekm','9856389023',144)
#             ''');

# query="insert into student(roll_no,name,age,place,phone,total_mark) values(%s,%s,%s,%s,%s,%s)"
#
# data=(106,'kiran',12,'ekm','8734567329',140)
# c.execute(query,data)
#
# con.commit()    #to save data permanently inside db
# print("data inserted")

#READ OPERATION
#
# query="select * from student"
# c.execute(query)
#
# records=c.fetchall()
# if records:
#     for row in records:
#         print(row)
# else:
#     print("No Records found")

# read all attributes of a student with roll number = roll number entered by the user

# rollno=int(input("Enter roll no:"))
# query="select * from student where roll_no=%s"
# data=(rollno,)
# c.execute(query,data)
#
# record=c.fetchone()
# if record:
#         print(record)
# else:
#     print("No Records found")

# update mark of a student with roll number =roll number entered by user

# rollno=int(input("Enter roll no:"))
# mark=int(input("Enter updated mark:"))
# query="update student set total_mark=%s where roll_no=%s"
# data=(mark,rollno)
# c.execute(query,data)
#
# con.commit()
# print("Updated successfully")

# delete a record from the roll number entered by the user

# rollno=int(input("Enter roll no:"))
# query="delete from student where roll_no=%s"
# data=(rollno,)
# c.execute(query,data)
#
# con.commit()
# print("deleted successfully")

# create a new record using values entered by user
# rollno=int(input("Enter roll no:"))
# n=input("Enter name:")
# a=int(input("Enter age:"))
# p=input("Enter place:")
# ph=input("Enter phone number:")
# tm=int(input("Enter total mark:"))
#
# query="insert into student(roll_no,name,age,place,phone,total_mark) values(%s,%s,%s,%s,%s,%s)"
# data=(rollno,n,a,p,ph,tm)
# c.execute(query,data)
#
# con.commit()
# print("New record created")

























