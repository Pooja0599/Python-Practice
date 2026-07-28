# ==========================================
# Project : Student Record System
# Author : Pooja Singh
# GitHub : Pooja0599
# ==========================================

students = {}

print("=" * 50)
print("       STUDENT RECORD SYSTEM")
print("=" * 50)


# ==========================================
# Add Student
# ==========================================

def add_student():
    roll_no = input("Enter Roll Number : ")
    name = input("Enter Student Name : ")
    marks = float(input("Enter Marks : "))

    students[roll_no] = {
        "Name": name,
        "Marks": marks
    }

    print("Student Added Successfully.")


# ==========================================
# View Students
# ==========================================

def view_students():

    if len(students) == 0:
        print("No Student Records Found.")

    else:
        print("\n----- Student Records -----")

        for roll, details in students.items():
            print("--------------------------------")
            print("Roll No :", roll)
            print("Name    :", details["Name"])
            print("Marks   :", details["Marks"])


# ==========================================
# Search Student
# ==========================================

def search_student():

    roll_no = input("Enter Roll Number : ")

    if roll_no in students:
        print(students[roll_no])
    else:
        print("Student Not Found.")


# ==========================================
# Update Marks
# ==========================================

def update_marks():

    roll_no = input("Enter Roll Number : ")

    if roll_no in students:

        new_marks = float(input("Enter New Marks : "))

        students[roll_no]["Marks"] = new_marks

        print("Marks Updated Successfully.")

    else:
        print("Student Not Found.")


# ==========================================
# Delete Student
# ==========================================

def delete_student():

    roll_no = input("Enter Roll Number : ")

    if roll_no in students:

        del students[roll_no]

        print("Student Deleted Successfully.")

    else:
        print("Student Not Found.")


# ==========================================
# Main Menu
# ==========================================

while True:

    print("\n===== MENU =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Your Choice : ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_marks()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("\nThank You for Using Student Record System.")
        break

    else:
        print("Invalid Choice. Please Try Again.")