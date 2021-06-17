import mysql.connector

db_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = db_conn.cursor()
try:
    sql = "CREATE DATABASE student"
    cursor.execute(sql)
except Exception as e:
    print(e, " database already exist")
