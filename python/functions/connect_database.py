import mysql.connector
from mysql.connector import Error


def connect_database():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='stock',
                                             user='root',
                                             port=8889,
                                             password='root', ssl_disabled=True)
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
