from db_conn import DBConnect

conn = DBConnect()

mysql_conn = conn.db_connector()
cursor = mysql_conn.cursor()

try:
    sql = "INSERT INTO student_info(id, stu_name, dept) values(1, 'Hamid', 'BBA')"
    sql2 = "INSERT INTO student_info(id, stu_name, dept) values(2, 'Ahmed', 'IT')"
    sql3 = "INSERT INTO student_info(id, stu_name, dept) values(3, 'Taposh', 'SC')"
    sql4 = "INSERT INTO student_info(id, stu_name, dept) values(4, 'Abrar', 'EEE')"

    val = cursor.execute(sql)
    val = cursor.execute(sql2)
    val = cursor.execute(sql3)
    val = cursor.execute(sql4)
    mysql_conn.commit()
    cursor.close()
    mysql_conn.close()
except Exception as e:
    print(e)