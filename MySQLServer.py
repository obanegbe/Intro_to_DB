import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_mysql_password'  # Replace with your actual password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database using IF NOT EXISTS to avoid failure
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error connecting to MySQL server: {e}")

    finally:
        # Clean up: close cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

# Run the function
if __name__ == "__main__":
    create_database()
