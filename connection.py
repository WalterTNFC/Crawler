import mysql.connector
from mysql.connector import Error

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

connection =create_db_connection("localhost", "root", "1234", "atividades")

def execute_query(connection, query):
    print(query)
    cursor = connection.cursor()
    print(cursor)
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

query = "SELECT * FROM atividades.crawler"

execute_query(connection, query)