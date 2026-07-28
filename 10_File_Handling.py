# ==========================================
# Topic : File Handling
# Author : Pooja Singh
# GitHub : Pooja0599
# ==========================================

# ==========================================
# 1. Write to a File (w)
# ==========================================

file = open("student.txt", "w")

file.write("Name : Pooja Singh\n")
file.write("Course : Data Analytics\n")
file.write("City : Chhatarpur\n")
file.close()
print("Data Written Successfully.")

print("=" * 40)

# ==========================================
# 2. Read File (r)
# ==========================================

file = open("student.txt", "r")
content = file.read()
print("File Content :")
print(content)
file.close()

print("=" * 40)

# ==========================================
# 3. Append Data (a)
# ==========================================

file = open("student.txt", "a")
file.write("Skills : Python, SQL, Power BI\n")
file.close()
print("Data Appended Successfully.")

print("=" * 40)

# ==========================================
# 4. Read File Again
# ==========================================

file = open("student.txt", "r")
print(file.read())
file.close()

print("=" * 40)

# ==========================================
# 5. Read One Line
# ==========================================

file = open("student.txt", "r")
print("First Line :")
print(file.readline())
file.close()

print("=" * 40)

# ==========================================
# 6. Read All Lines
# ==========================================

file = open("student.txt", "r")
print("All Lines :")
for line in file.readlines():
    print(line.strip())

file.close()

print("=" * 40)

# ==========================================
# 7. Using with open()
# ==========================================

with open("student.txt", "r") as file:

    print("Reading Using with open() :")
    print(file.read())

print("=" * 40)

# ==========================================
# 8. File Modes
# ==========================================

print("Common File Modes :")
print("r  -> Read")
print("w  -> Write")
print("a  -> Append")

print("=" * 40)

print("File Handling Completed Successfully.")