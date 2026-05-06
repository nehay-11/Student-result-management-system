import mysql.connector


def connect_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="result_system"
    )

    return connection