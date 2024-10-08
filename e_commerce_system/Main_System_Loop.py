# from e_commerce_system.Connection_Handling import load_connection_details
# from e_commerce_system.Customer_Operations import Customer
# from e_commerce_system.Database_Schema import create_tables
# from e_commerce_system.Order_Operations import Order
# from e_commerce_system.Product_Operations import Product

# def main():
#     connection_details = load_connection_details("connection_details.txt")
#     db_connection = connect_to_database(connection_details)

#     cursor = db_connection.cursor()
#     create_tables(cursor)
#     cursor.close()

#     product_manager = Product(db_connection)
#     customer_manager = Customer(db_connection)
#     order_manager = Order(db_connection)

#     while True:
#         print("\n1. Add Product")
#         print("2. Remove Product")
#         print("3. List Products")
#         print("4. Add Customer")
#         print("5. Remove Customer")
#         print("6. List Customers")
#         print("7. Place Order")
#         print("8. Remove Order")
#         print("9. List Orders")
#         print("10. Exit")

#         choice = input("Enter your choice: ")

#         if choice == '1':
#             product_manager.add_product()
#         elif choice == '2':
#             product_manager.remove_product()
#         elif choice == '3':
#             product_manager.list_products()
#         elif choice == '4':
#             customer_manager.add_customer()
#         elif choice == '5':
#             customer_manager.remove_customer()
#         elif choice == '6':
#             customer_manager.list_customers()
#         elif choice == '7':
#             order_manager.place_order()
#         elif choice == '8':
#             order_manager.remove_order()
#         elif choice == '9':
#             order_manager.list_orders()
#         elif choice == '10':
#             db_connection.close()
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()


from Connection_Handling import load_connection_details, connect_to_database
from Customer_Operations import Customer
from Database_Schema import create_tables
from Order_Operations import Order
from Product_Operations import Product

def main():
  
    connection_details = load_connection_details("connection_details.txt")
    
    db_connection = connect_to_database(connection_details)

    cursor = db_connection.cursor()
    create_tables(cursor)
    cursor.close()

    product_manager = Product(db_connection)
    customer_manager = Customer(db_connection)
    order_manager = Order(db_connection)

    while True:
        print("\n1. Add Product")
        print("2. Remove Product")
        print("3. List Products")
        print("4. Add Customer")
        print("5. Remove Customer")
        print("6. List Customers")
        print("7. Place Order")
        print("8. Remove Order")
        print("9. List Orders")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            product_manager.add_product()
        elif choice == '2':
            product_manager.remove_product()
        elif choice == '3':
            product_manager.list_products()
        elif choice == '4':
            customer_manager.add_customer()
        elif choice == '5':
            customer_manager.remove_customer()
        elif choice == '6':
            customer_manager.list_customers()
        elif choice == '7':
            order_manager.place_order()
        elif choice == '8':
            order_manager.remove_order()
        elif choice == '9':
            order_manager.list_orders()
        elif choice == '10':
            db_connection.close()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
