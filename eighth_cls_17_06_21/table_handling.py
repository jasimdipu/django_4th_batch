from db_conn import DBConnect

conn = DBConnect()

mysql_conn = conn.db_connector()

cursor = mysql_conn.cursor()

sql = "CREATE TABLE student_info(id integer primary key, stu_name varchar(255), dept varchar (255))"

try:
    cursor.execute(sql)
    if cursor:
        print("student table created")
    else:
        print("Table not created")
    cursor.close()
    mysql_conn.close()
except Exception as e:
    print(e)





