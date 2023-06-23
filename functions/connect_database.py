# Define connection with mysql database
import mysql.connector
from mysql.connector import Error
from config import host,database,user,port,password

def connect_database():
    """
    Establishes a connection to the MySQL database and returns the connection and cursor objects.

    Returns:
    - connection: Connection object for interacting with the database.
    - cursor: Cursor object for executing SQL queries.
    """
    try:
        connection = mysql.connector.connect(host=host,
                                             database=database,
                                             user=user,
                                             port=port,
                                             password=password, ssl_disabled=True)
        if connection.is_connected():
            cursor = connection.cursor()
            return connection,cursor
    except mysql.connector.Error as err:
        print("Error while connecting to MySQL", err)
