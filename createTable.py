#createTable.py
import mysql.connector as db
def createTable():
    try:
        con=db.connect(host='localhost',user='root',password='123456789',database='Studentinfo')
        cur=con.cursor()
        q="create table student(sno int primary key,name varchar(20) not null ,marks float not null,college varchar(50) not null)"
        cur.execute(q)
        print("table created verify")
    except db.DatabaseError as d:
        print("Error Code: ",d)
createTable()