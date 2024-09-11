import mysql.connector

def load_connection_details(file_path):
    try:
        with open(r"D:\Python_Training\SQL_Host_details.txt", "r") as file:
            lines = file.readlines()
            connection_details = {}
            for line in lines:
                key, value = line.strip().split('=')
                connection_details[key] = value
            return connection_details
    except FileNotFoundError:
        print("Error: The file containing the database connection details was not found.")
        exit()
    except Exception as e:
        print(f"Error: {e}")
        exit()

def connect_to_database(connection_details):
    try:
        conn = mysql.connector.connect(
            host=connection_details.get('host', '127.0.0.1'),
            user=connection_details['user'],
            password=connection_details['password'],
            database=connection_details['database']
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        exit()

def create_tables(cursor):
    product_table = '''
    CREATE TABLE IF NOT EXISTS Products (
        product_id INTEGER NOT NULL PRIMARY KEY,
        product_name TEXT NOT NULL,
        price REAL NOT NULL,
        stock INTEGER NOT NULL
    )
    '''
    cursor.execute(product_table)

    customer_table = '''
    CREATE TABLE IF NOT EXISTS Customers (
        customer_id INTEGER NOT NULL PRIMARY KEY,
        customer_name TEXT NOT NULL,
        Cus_mailid TEXT
    )
    '''
    cursor.execute(customer_table)

    order_table = '''
    CREATE TABLE IF NOT EXISTS Orders (
        order_id INTEGER NOT NULL PRIMARY KEY,
        customer_id INTEGER,
        order_date TEXT,
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    )
    '''
    cursor.execute(order_table)

    order_item_table = '''
    CREATE TABLE IF NOT EXISTS Order_item (
        order_item_id INTEGER NOT NULL PRIMARY KEY,
        order_id INTEGER,
        product_id INTEGER,
        quantity INTEGER,
        price REAL,
        FOREIGN KEY (order_id) REFERENCES Orders(order_id),
        FOREIGN KEY (product_id) REFERENCES Products(product_id)
    )
    '''
    cursor.execute(order_item_table)

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

class Order:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def place_order(self):
        cursor = None
        try:
            order_id = int(input("Enter Order ID: "))
            customer_id = int(input("Enter Customer ID: "))
            order_date = input("Enter Order Date (YYYY-MM-DD): ")
            
            cursor = self.db_connection.cursor()
            sql_order = "INSERT INTO Orders (order_id, customer_id, order_date) VALUES (%s, %s, %s)"
            order_values = (order_id, customer_id, order_date)
            cursor.execute(sql_order, order_values)

            while True:
                product_id = int(input("Enter Product ID: "))
                quantity = int(input("Enter Quantity: "))

                sql_product = "SELECT price, stock FROM Products WHERE product_id = %s"
                cursor.execute(sql_product, (product_id,))
                product = cursor.fetchone()

                if product:
                    price = product[0]
                    stock = product[1]
                    if quantity <= stock:
                        total_price = price * quantity
                        sql_order_item = "INSERT INTO Order_item (order_item_id, order_id, product_id, quantity, price) VALUES (%s, %s, %s, %s, %s)"
                        cursor.execute(sql_order_item, (order_id, order_id, product_id, quantity, total_price))

                        sql_update_stock = "UPDATE Products SET stock = stock - %s WHERE product_id = %s"
                        cursor.execute(sql_update_stock, (quantity, product_id))
                    else:
                        print(f"Error: Insufficient stock for Product ID {product_id}")
                else:
                    print(f"Error: Product ID {product_id} not found.")

                more_items = input("Add more items? (yes/no): ").strip().lower()
                if more_items != 'yes':
                    break
                

            self.db_connection.commit()
            print(f"Order '{order_id}' placed successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if cursor:
                cursor.close()

    def remove_order(self):
        cursor = None
        try:
            order_id = int(input("Enter Order ID to remove: "))

            cursor = self.db_connection.cursor()
            sql = "DELETE FROM Orders WHERE order_id = %s"
            values = (order_id,)
            cursor.execute(sql, values)
            self.db_connection.commit()
            if cursor.rowcount > 0:
                print(f"Order with ID '{order_id}' removed successfully.")
            else:
                print(f"Order with ID '{order_id}' not found.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if cursor:
                cursor.close()

    def list_orders(self):
        cursor = None
        try:
            cursor = self.db_connection.cursor()
            sql = "SELECT * FROM Orders"
            cursor.execute(sql)
            orders = cursor.fetchall()
            for order in orders:
                print(f"Order ID: {order[0]}, Customer ID: {order[1]}, Order Date: {order[2]}")
                cursor.execute("SELECT * FROM Order_item WHERE order_id = %s", (order[0],))
                order_items = cursor.fetchall()
                for item in order_items:
                    print(f"\tProduct ID: {item[2]}, Quantity: {item[3]}, Price: {item[4]}")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if cursor:
                cursor.close()

class ECommerceSystem:
    def __init__(self, db_connection):
        self.product = Product(db_connection)
        self.customer = Customer(db_connection)
        self.order = Order(db_connection)

def main():
    connection_details = load_connection_details("db_connection.txt")
    db_connection = connect_to_database(connection_details)
    
    cursor = None
    try:
        cursor = db_connection.cursor()
        create_tables(cursor)

        ecommerce_system = ECommerceSystem(db_connection)
        
        while True:
            print("\n--- E-Commerce System Menu ---")
            print("1. Add Product")
            print("2. Remove Product")
            print("3. List Products")
            print("4. Add Customer")
            print("5. Remove Customer")
            print("6. List Customers")
            print("7. Place Order")
            print("8. Remove Order")
            print("9. List Orders")
            print("10. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                ecommerce_system.product.add_product()
            elif choice == "2":
                ecommerce_system.product.remove_product()
            elif choice == "3":
                ecommerce_system.product.list_products()
            elif choice == "4":
                ecommerce_system.customer.add_customer()
            elif choice == "5":
                ecommerce_system.customer.remove_customer()
            elif choice == "6":
                ecommerce_system.customer.list_customers()
            elif choice == "7":
                ecommerce_system.order.place_order()
            elif choice == "8":
                ecommerce_system.order.remove_order()
            elif choice == "9":
                ecommerce_system.order.list_orders()
            elif choice == "10":
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please try again.")

    finally:
        if cursor:
            cursor.close()
        db_connection.close()

if __name__ == "__main__":
    main()
