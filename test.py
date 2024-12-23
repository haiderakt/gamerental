import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    try:
        # Attempt to connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",  # Use localhost or 127.0.0.1
            user="root",       # MySQL user (replace with your username)
            password="haiderr",  # Replace with your actual password
            database="gamrentaldb",  # Optional: specify the database
            port=33060  # Default MySQL port (use 33060 if using X Protocol)
        )
        
        # Check if the connection is successful
        if connection.is_connected():
            print("Successfully connected to MySQL")
            # Optionally, fetch server info to verify connection
            db_info = connection.get_server_info()
            print(f"MySQL server version: {db_info}")
        
    except Error as e:
        print(f"Error: {e}")
    finally:
        # Close the connection
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

# Call the function to test the connection
if __name__ == "__main__":
    connect_to_mysql()
