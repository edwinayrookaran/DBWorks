# Create a database named shop
#
# Create a table `Product` with the following fields:
#
#  `product_id` – Primary Key
#  `name`
#  `brand`
#  `category`
#  `price`
#  `stock`
#
# Write a menu-driven Python program using MySQL with the following options:
#
# text
# 1. Insert Product details
# 2. Read all Product details
# 3. Search a Product by product_id
# 4. Update the stock of a Product
# 5. Delete a Product record
# 6. Exit

# con=mysql.connector.connect(user="root",password="root",host="localhost")
# c=con.cursor()
# c.execute("create database shop")

import mysql.connector

con=mysql.connector.connect(user="root",password="root",host="localhost",database="shop")
c=con.cursor()
# c.execute('create table product(product_id int not null primary key,name varchar(20),brand varchar(20),category varchar(20),price int,stock int)')
#
# print("table created successfully")


def insert():
    productid=int(input("Enter product id:"))
    name=input("Enter name of the product:")
    brand=input("Enter brand name:")
    category=input("Enter category:")
    price=int(input("Enter price:"))
    stock=int(input("Enter stock:"))

    query="insert into product(product_id,name,brand,category,price,stock) values(%s,%s,%s,%s,%s,%s)"
    data=(productid,name,brand,category,price,stock)
    c.execute(query,data)
    con.commit()
    print("inserted")

def get():
    query="select * from product"
    c.execute(query)

    records=c.fetchall()
    if records:
        for row in records:
            print(row)
    else:
        print("No records found")

def search():
    productid=int(input("Enter product id:"))
    query="select * from product where product_id=%s"
    data=(productid,)
    c.execute(query,data)

    record=c.fetchone()
    if record:
        print(record)
    else:
        print("No record found")

def update():
    productid = int(input("Enter product id:"))
    stock=int(input("Enter updated stock:"))
    query="update product set stock=%s where product_id=%s"
    data=(stock,productid)
    c.execute(query,data)
    con.commit()
    print("Updated successfully")

def delete():
    productid = int(input("Enter product id:"))
    query="delete from product where product_id=%s"
    data=(productid,)
    c.execute(query,data)
    con.commit()
    print("deleted successfully")

while(1):
    print("1. Insert Product details")
    print("2. Read all Product details")
    print("3. Search a Product by product_id")
    print("4. Update the stock of a Product")
    print("5. Delete a Product record")
    print("6. Exit")

    ch=int(input("Enter choice:"))

    if ch==1:
        insert()
    elif ch==2:
        get()
    elif ch==3:
        search()
    elif ch==4:
        update()
    elif ch==5:
        delete()
    elif ch==6:
        exit()
    else:
        print("Invalid choice")




