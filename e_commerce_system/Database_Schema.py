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
