#StudentInsert.py
import mysql.connector as db
def insertrecords():
    while True:
        try:
            con=db.connect(host='localhost',user='root',password='123456789',database='Studentinfo')
            cur=con.cursor()
            sno=int(input("enter student Sno: "))
            name=input("enter student Name: ")
            marks=float(input("enter student marks: "))
            colname=input("enter col name: ")
            q="insert into student values(%d,'%s',%f,'%s')"%(sno,name,marks,colname)
            cur.execute(q)
            con.commit()
            print("insert values verify")
            c=input("Add another record type YES or NO: ")

            if c.lower()!="yes":
                print("{} record inserted in table".format(cur.rowcount))
                break

        except db.DatabaseError as d:
            print("Error Code: ",d)
        except ValueError:
            print("Don't Enter alnums and special symbols ")
