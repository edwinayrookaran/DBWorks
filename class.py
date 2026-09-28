# define a class to perform database operations on book table
from venv import create

# create a class named BookListCreateRetrieveUpdateDelete and define methods
# list() -- for reading all records
# create -- for creating new record
# retrieve(id) -- for reading a specific record
# update(id,data) -- for updating a specific record
# delete(id) -- for deleting a specific record

import mysql.connector

class BookListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.connection=mysql.connector.connect(user="root",password="root",host="localhost",database="library_db")
        print(self.connection)
        self.cursor=self.connection.cursor()
        print("connected successfully")
    def list(self):
        # reading all records
        query="select * from book"
        self.cursor.execute(query)

        records=self.cursor.fetchall()
        if records:
            for row in records:
                print(row)
        else:
            print("No records")
    def create(self,title,author,price,pages,language):
        query="insert into book(title,author,price,pages,language) values(%s,%s,%s,%s,%s)"

        data=(title,author,price,pages,language)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("Data Inserted")

    def retrieve(self,id):
        query="select * from book where id=%s"
        data=(id,)
        self.cursor.execute(query,data)

        records=self.cursor.fetchone()
        if records:
            print(records)
        else:
            print("No records found")
    def update(self,id,title,author,price,pages,language):
        query="update book set title=%s,author=%s,price=%s,pages=%s,language=%s where id=%s"
        data=(title,author,price,pages,language,id)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:
            print("Updated Successfully")
        else:
            print("No record found")

    def delete(self,id):
        query="delete from book where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:  # if no updations rowcount returns 0
            print("data is deleted")
        else:
            print("No record found")

book_instance=BookListCreateRetrieveUpdateDelete()
# book_instance.list()
# book_instance.create("ABC",'sam',700,350,"English")
# book_instance.retrieve(2)
# book_instance.delete(2)
book_instance.update(1,"ABC","SAM",500,250,"malayalam")

