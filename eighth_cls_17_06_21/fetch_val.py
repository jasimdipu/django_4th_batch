from db_conn import DBConnect

conn = DBConnect()

mysql_conn = conn.db_connector()
cursor = mysql_conn.cursor()

try:
    sql = "SELECT * FROM student_info"
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        print(i)
except Exception as e:
    print(e)

cursor.close()
mysql_conn.close()