import mysql.connector


class ListVehicleCreateRetrieveUpdateDelete:
    def __init__(self):
        self.connection = mysql.connector.connect(user="root", password="root", host="localhost", database="vehicle_db")
        print(self.connection)
        self.cursor = self.connection.cursor()
        print("connected successfully")

    def list(self):
        # reading all records
        query = "select * from vehicle"
        self.cursor.execute(query)

        records = self.cursor.fetchall()
        if records:
            for row in records:
                print(row)
        else:
            print("No records")

    def create(self,brand,model,type,price,year):
        query = "insert into vehicle(brand,model,type,price,year) values(%s,%s,%s,%s,%s)"

        data = (brand,model,type,price,year)
        self.cursor.execute(query, data)
        self.connection.commit()
        print("Data Inserted")

    def retrieve(self, id):
        query = "select * from vehicle where id=%s"
        data = (id,)
        self.cursor.execute(query, data)

        record = self.cursor.fetchone()
        if record:
            print(record)
        else:
            print("No record found")

    def update(self, id,brand,model,type,price,year):
        query = "update vehicle set brand=%s,model=%s,type=%s,price=%s,year=%s where id=%s"
        data = (brand,model,type,price,year, id)
        self.cursor.execute(query, data)
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("Updated Successfully")
        else:
            print("No record found")

    def delete(self, id):
        query = "delete from vehicle where id=%s"
        data = (id,)
        self.cursor.execute(query, data)
        self.connection.commit()
        if self.cursor.rowcount > 0:  # if no updations rowcount returns 0
            print("data is deleted")
        else:
            print("No record found")


vehicle_instance = ListVehicleCreateRetrieveUpdateDelete()
# vehicle_instance.list()
# vehicle_instance.create("hyundai","verna","car",1000,2025)
# vehicle_instance.retrieve(2)
# vehicle_instance.delete(2)
# vehicle_instance.update(1,"toyota", "hyryder","car", 1500, 2027)