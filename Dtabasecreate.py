def databasecreate():
    import mysql.connector as db
    try:
        con=db.connect(host='localhost',user='root',password='123456789')
        cur=con.cursor()
        q="create database Studentinfo"
        cur.execute(q)
        print("Database created verify")
    except db.DatabaseError as db:
        print("Error Code: ",db)
databasecreate()
