def show_menu():
    print("....ATTENDANCE SYSTEM...")
    print(" 1. ADD STUDENT")
    print(" 2. VIEW STUDENTS")
    print(" 3. MARK ATTENDANCE")
    print(" 4. VIEW ATTENDANCE ")
    print(" 5. EXIT")

while True:
    show_menu()
    choice = input("Enter your choice : ")

    if choice=="5":
        print(" THANK YOU ")
        break

def add_student():
    roll_no= input("Enter Student Roll Number : ")
    name = input("Enter the Name :")
    file = open("students.csv","a")
    file.write(student_id + " ,")

