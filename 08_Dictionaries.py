# ==========================================
# Topic : Dictionaries
# Author : Pooja Singh
# GitHub : Pooja0599
# ==========================================

# ==========================================
# 1. Creating a Dictionary
# ==========================================

student = {
    "Name": "Pooja",
    "Age": 27,
    "Course": "Data Analytics"
}
print("Original Dictionary :")
print(student)

print("=" * 40)

# ==========================================
# 2. Accessing Values
# ==========================================

print("Name :", student["Name"])
print("Age :", student["Age"])

print("=" * 40)

# ==========================================
# 3. Using get()
# ==========================================

print("Course :", student.get("Course"))

print("=" * 40)

# ==========================================
# 4. Adding a New Key
# ==========================================

student["City"] = "Chhatarpur"
print("After Adding City :")
print(student)

print("=" * 40)

# ==========================================
# 5. Updating a Value
# ==========================================

student["Age"] = 28

print("After Updating Age :")
print(student)

print("=" * 40)

# ==========================================
# 6. Dictionary Keys
# ==========================================

print("Keys :")
print(student.keys())

print("=" * 40)

# ==========================================
# 7. Dictionary Values
# ==========================================

print("Values :")
print(student.values())

print("=" * 40)

# ==========================================
# 8. Dictionary Items
# ==========================================

print("Items :")
print(student.items())

print("=" * 40)

# ==========================================
# 9. Update Method
# ==========================================

student.update({"Course": "Data Analyst"})

print("After Update :")
print(student)

print("=" * 40)

# ==========================================
# 10. Pop Method
# ==========================================

student.pop("City")

print("After Pop :")
print(student)

print("=" * 40)

# ==========================================
# 11. Popitem Method
# ==========================================

employee = {
    "ID": 101,
    "Name": "Rahul",
    "Department": "IT"
}

employee.popitem()

print("After Popitem :")
print(employee)

print("=" * 40)

# ==========================================
# 12. Membership Operator
# ==========================================

print("Name" in student)
print("Salary" in student)

print("=" * 40)

# ==========================================
# 13. Loop Through Dictionary
# ==========================================

print("Student Details :")

for key, value in student.items():
    print(key, ":", value)

print("=" * 40)

# ==========================================
# 14. Nested Dictionary
# ==========================================

employees = {
    101: {"Name": "Rahul", "Department": "HR"},
    102: {"Name": "Aman", "Department": "IT"},
    103: {"Name": "Neha", "Department": "Sales"}
}

print("Nested Dictionary :")

for emp_id, details in employees.items():
    print(emp_id, ":", details)

print("=" * 40)

# ==========================================
# 15. Dictionary Length
# ==========================================

print("Total Keys :", len(student))

print("=" * 40)

print("Dictionaries Completed Successfully.")