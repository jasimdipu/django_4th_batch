from db_conn import DBConnect

conn = DBConnect()

mysql_conn = conn.db_connector()
cursor = mysql_conn.cursor()

try:
    # Delete = delete from student_info where id=?
    sql = "UPDATE student_info SET dept='Social Science' WHERE id=3"
    cursor.execute(sql)
    mysql_conn.commit()

    fetch = "SELECT * FROM student_info"
    cursor.execute(fetch)
    result = cursor.fetchall()
    for i in result:
        print(i)
except Exception as e:
    print(e)

cursor.close()
mysql_conn.close()
