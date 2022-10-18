# Define connection with mysql database
import mysql.connector
from mysql.connector import Error
from config import host,database,user,port,password

# connection database function return connection and cursor parameter to check connection with database and make query using cursor
def connect_database():
    try:
        connection = mysql.connector.connect(host=host,
                                             database=database,
                                             user=user,
                                             port=port,
                                             password=password, ssl_disabled=True)
        if connection.is_connected():
            db_Info = connection.get_server_info()
            cursor = connection.cursor()
            return connection,cursor
    except Error as e:
        print("Error while connecting to MySQL", e)
