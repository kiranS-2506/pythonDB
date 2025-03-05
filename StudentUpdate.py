#StudentUpdate
import mysql.connector as db
def StudentUpdate():
    while True:
        try:
            con=db.connect(host='localhost',user='root',password='123456789',database='Studentinfo')
            cur=con.cursor()
            marks=float(input("enter new marks: "))
            eno=int(input("Enter Student Sno: "))
            q="update student set marks=%f where sno=%d"%(marks,eno)
            cur.execute(q)
            con.commit()
            if cur.rowcount<=0:
                print("student Sno does not Exists--Try again")
            else:
                print("Student Marks Update")
                c = cur.rowcount + 1
            if input("update another record type YES/NO:").lower() != "yes":
                print("{} records deleted".format(c))
                break
        except db.DatabaseError as d:
             print("Error Code :",d)
        except ValueError:
            print("Dont't enter alphabets and special characters")

def Studentdelete():
    while True:
        try:
            con=db.connect(host='localhost',user='root',password='123456789',database='Studentinfo')
            cur=con.cursor()
            eno=int(input("Enter Student Sno: "))
            q="delete from student where sno=%d"%eno
            cur.execute(q)
            con.commit()
            if cur.rowcount<=0:
                print("student Sno does not Exists--Try again")
            else:
                print("Student date deleted")
                c=cur.rowcount+1
            if input("Delete another record type YES/NO:").lower() != "yes":
                print("{} records deleted".format(c))
                break
        except db.DatabaseError as d:
             print("Error Code :",d)
        except ValueError:
            print("Dont't enter alphabets and special characters")
