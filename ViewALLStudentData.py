#ViewALLStudentData
import mysql.connector as db
def ViewAllStudentData():
    try:
        con=db.connect(host='localhost',user='root',password='123456789',database='Studentinfo')
        cur=con.cursor()
        q="select * from student"
        cur.execute(q)
        records=cur.fetchall()
        print(" "*10,"AllStudentData"," "*20)
        print("-"*50)
        des=cur.description
        for val in des:
            print(val[0],end="\t\t")
        print()
        print("-"*50)
        for record in records:
            for val in record:
              print(val,end="\t\t")
            print()
        print("-"*50)
    except db.DatabaseError as d:
        print("Error Code: ",d)