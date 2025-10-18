import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sandhya@1992",
        database="product_db",
        port=3306
    )
