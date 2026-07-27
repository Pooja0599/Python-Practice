# ==========================================
# Topic : Tuples
# Author : Pooja Singh
# GitHub : Pooja0599
# ==========================================

# ==========================================
# 1. Creating a Tuple
# ==========================================

fruits = ("Apple", "Banana", "Mango", "Orange")
print("Original Tuple :", fruits)

print("=" * 40)

# ==========================================
# 2. Accessing Elements
# ==========================================

print("First Fruit :", fruits[0])
print("Last Fruit :", fruits[-1])

print("=" * 40)

# ==========================================
# 3. Tuple Slicing
# ==========================================

print("First Two Fruits :", fruits[:2])
print("Last Two Fruits :", fruits[-2:])

print("=" * 40)

# ==========================================
# 4. Length of Tuple
# ==========================================

print("Length :", len(fruits))

print("=" * 40)

# ==========================================
# 5. Count Method
# ==========================================

numbers = (10, 20, 30, 20, 40, 20)

print("Count of 20 :", numbers.count(20))

print("=" * 40)

# ==========================================
# 6. Index Method
# ==========================================

print("Index of 30 :", numbers.index(30))

print("=" * 40)

# ==========================================
# 7. Tuple Packing
# ==========================================

student = ("Pooja", 27, "Data Analyst")

print("Packed Tuple :", student)

print("=" * 40)

# ==========================================
# 8. Tuple Unpacking
# ==========================================

name, age, role = student

print("Name :", name)
print("Age :", age)
print("Role :", role)

print("=" * 40)

# ==========================================
# 9. Membership Operator
# ==========================================

print("Apple" in fruits)
print("Grapes" in fruits)

print("=" * 40)

# ==========================================
# 10. Loop Through Tuple
# ==========================================

print("Fruits List :")

for fruit in fruits:
    print(fruit)

print("=" * 40)

# ==========================================
# 11. Nested Tuple
# ==========================================

employees = (
    (101, "Rahul"),
    (102, "Aman"),
    (103, "Neha")
)

print("Employee Records :")

for emp in employees:
    print(emp)

print("=" * 40)

# ==========================================
# 12. Tuple Concatenation
# ==========================================

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print("Concatenated Tuple :", result)

print("=" * 40)

# ==========================================
# 13. Tuple Repetition
# ==========================================

colors = ("Red", "Blue")

print(colors * 3)

print("=" * 40)

print("Tuples Completed Successfully.")