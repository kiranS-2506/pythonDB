from StudentMenu import StudentMenu
from StudentUpdate import StudentUpdate,Studentdelete
from StudentInsert import insertrecords
from StudentSearch import SearchStudentData
from ViewALLStudentData import ViewAllStudentData
from ViewStudentData import ViewStudentData
StudentMenu()
while True:

    try:

        ch=int(input("Enter Ur choice: "))
        print("-"*50)
        match(ch):
            case 1:
                insertrecords()
            case 2:
                ViewStudentData()
            case 3:
                ViewAllStudentData()
            case 4:
                SearchStudentData()
            case 5:
                StudentUpdate()
            case 6:
                Studentdelete()
            case 7:
                print("Thanks for using code")
                break
            case _:
                print("Invalid choice try again")
    except ValueError:
        print("Don't Enter Alphabets and Special Characters ")




