# ==========================================
# Topic : OOP Basics (Object-Oriented Programming)
# Author : Pooja Singh
# GitHub : Pooja0599
# ==========================================

# ==========================================
# 1. Creating a Class
# ==========================================

class Student:
    pass

print("Class Created Successfully.")

print("=" * 50)

# ==========================================
# 2. Creating an Object
# ==========================================

student1 = Student()

print("Object Created Successfully.")

print("=" * 50)

# ==========================================
# 3. Constructor (__init__)
# ==========================================

class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

student1 = Student("Pooja", 27, "Data Analytics")

print("Student Details")
print("Name   :", student1.name)
print("Age    :", student1.age)
print("Course :", student1.course)

print("=" * 50)

# ==========================================
# 4. Creating Multiple Objects
# ==========================================

student2 = Student("Rahul", 24, "Python")

print("Second Student")
print("Name   :", student2.name)
print("Age    :", student2.age)
print("Course :", student2.course)

print("=" * 50)

# ==========================================
# 5. Creating a Method
# ==========================================

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Name   :", self.name)
        print("Employee Salary :", self.salary)

emp1 = Employee("Aman", 60000)

emp1.display()

print("=" * 50)

# ==========================================
# 6. Updating Object Values
# ==========================================

emp1.salary = 70000

print("Updated Salary :", emp1.salary)

print("=" * 50)

# ==========================================
# 7. Another Class Example
# ==========================================

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def car_info(self):
        print("Brand :", self.brand)
        print("Model :", self.model)

car1 = Car("Hyundai", "Creta")

car1.car_info()

print("=" * 50)

# ==========================================
# 8. Using Multiple Objects
# ==========================================

car2 = Car("Tata", "Nexon")

car2.car_info()

print("=" * 50)

print("OOP Basics Completed Successfully.")