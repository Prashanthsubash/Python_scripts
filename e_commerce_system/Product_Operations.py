import mysql.connector
class Product:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def add_product(self):
        cursor = None
        try:
            product_id = int(input("Enter Product ID: "))
            product_name = input("Enter Product Name: ")
            price = float(input("Enter Product Price: "))
            stock = int(input("Enter Product Stock: "))
            
            if stock < 0:
                raise ValueError("Stock cannot be negative.")
            
            cursor = self.db_connection.cursor()
            sql = "INSERT INTO Products (product_id, product_name, price, stock) VALUES (%s, %s, %s, %s)"
            values = (product_id, product_name, price, stock)
            cursor.execute(sql, values)
            self.db_connection.commit()
            print(f"Product '{product_name}' added successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if cursor:
                cursor.close()

    def remove_product(self):
        cursor = None
        try:
            product_id = int(input("Enter Product ID to remove: "))
            
            cursor = self.db_connection.cursor()
            sql = "DELETE FROM Products WHERE product_id = %s"
            values = (product_id,)
            cursor.execute(sql, values)
            self.db_connection.commit()
            if cursor.rowcount > 0:
                print(f"Product with ID '{product_id}' removed successfully.")
            else:
                print(f"Product with ID '{product_id}' not found.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if cursor:
                cursor.close()

    def list_products(self):
        cursor = None
        try:
            cursor = self.db_connection.cursor()
            sql = "SELECT * FROM Products"
            cursor.execute(sql)
            products = cursor.fetchall()
            for product in products:
                print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Stock: {product[3]}")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if cursor:
                cursor.close()
