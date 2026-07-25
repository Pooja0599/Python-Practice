# ==========================================
# Project : Student Grade System
# Author : Pooja Singh
# GitHub : Pooja0599
# ==========================================

print("===================================================")
print("        STUDENT GRADE SYSTEM")
print("===================================================")


# Function to calculate percentage
def calculate_percentage(english, maths, science):

    total = english + maths + science
    percentage = total / 3

    return total, percentage


# Function to calculate grade
def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"

    elif percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 40:
        return "D"

    else:
        return "Fail"


# User Input
student_name = input("Enter Student Name : ")

english = int(input("Enter English Marks : "))
maths = int(input("Enter Maths Marks : "))
science = int(input("Enter Science Marks : "))

# Function Calling
total, percentage = calculate_percentage(english, maths, science)

grade = calculate_grade(percentage)

print("===================================================")

print("Student Name :", student_name)
print("Total Marks  :", total)
print("Percentage   :", round(percentage, 2), "%")
print("Grade        :", grade)

print("===================================================")

print("Project Completed Successfully.")