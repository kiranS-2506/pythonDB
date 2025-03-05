#ViewALLStudentData
import mysql.connector as db
def SearchStudentData():
    while True:
        try:
            con=db.connect(host='localhost',user='root',password='123456789',database='Studentinfo')
            cur=con.cursor()
            no=int(input("Enter student sno: "))
            q="select * from student where sno={}".format(no)
            cur.execute(q)
            record=cur.fetchone()
            for val in cur.description:
                print(val[0],end="\t\t")
            print()
            print("-"*50)
            for val in record:
                print(val,end="\t\t")
            print()
            ch=input("find another student Type Yes/No :").lower()
            if ch!="yes":
                break

        except db.DatabaseError as d:
            print("Error Code: ",d)
