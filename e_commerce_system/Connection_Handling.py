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
