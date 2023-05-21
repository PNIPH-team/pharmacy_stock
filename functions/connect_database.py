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
            cursor = connection.cursor()
            return connection,cursor
    except mysql.connector.Error as err:
        print("Error while connecting to MySQL", err)
