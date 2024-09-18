class Customer:
    def __init__(self, db_connection):
        self.db_connection = db_connection
    
    def add_customer(self):
        cursor = None
        try:
            customer_id = int(input("Enter Customer ID: "))
            customer_name = input("Enter Customer Name: ")
            Cus_mailid = input("Enter Customer Email: ")
            
            cursor = self.db_connection.cursor()
            sql = "INSERT INTO Customers (customer_id, customer_name, Cus_mailid) VALUES (%s, %s, %s)"
            values = (customer_id, customer_name, Cus_mailid)
            cursor.execute(sql, values)
            self.db_connection.commit()
            print(f"Customer '{customer_name}' added successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if cursor:
                cursor.close()

    def remove_customer(self):
        cursor = None
        try:
            customer_id = int(input("Enter Customer ID to remove: "))
            
            cursor = self.db_connection.cursor()
            sql = "DELETE FROM Customers WHERE customer_id = %s"
            values = (customer_id,)
            cursor.execute(sql, values)
            self.db_connection.commit()
            if cursor.rowcount > 0:
                print(f"Customer with ID '{customer_id}' removed successfully.")
            else:
                print(f"Customer with ID '{customer_id}' not found.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if cursor:
                cursor.close()

    def list_customers(self):
        cursor = None
        try:
            cursor = self.db_connection.cursor()
            sql = "SELECT * FROM Customers"
            cursor.execute(sql)
            customers = cursor.fetchall()
            for customer in customers:
                print(f"ID: {customer[0]}, Name: {customer[1]}, Email: {customer[2]}")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if cursor:
                cursor.close()
