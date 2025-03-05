#ViewStudentData
import mysql.connector as db
def ViewStudentData():
    try:
        con=db.connect(host='localhost',user='root',password='123456789',database='Studentinfo')
        cur=con.cursor()
        q="select * from student"
        cur.execute(q)
        for val in cur.description:
            print(val[0],end="\t\t")
        print()
        print("-"*50)
        record=cur.fetchone()
        for val in record:
            print(val,end="\t\t")
        print()
    except db.DatabaseError as d:
        print("Error Code: ",d)


