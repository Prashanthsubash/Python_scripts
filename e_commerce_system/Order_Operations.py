import mysql.connector
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
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if cursor:
                cursor.close()
