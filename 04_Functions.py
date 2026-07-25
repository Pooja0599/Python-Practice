# ==========================================
# Topic : Functions
# Author : Pooja Singh
# GitHub : Pooja0599
# ==========================================

# ==========================================
# 1. Simple Function
# ==========================================

def welcome():
    print("Welcome to Python Functions")

welcome()

print("=============================================")

# ==========================================
# 2. Function with No Parameters
# ==========================================

def student():
    print("Student Name : Pooja")
    print("Course : Python")

student()

print("=============================================")

# ==========================================
# 3. Function with Parameters
# ==========================================

def greet(name):
    print("Hello", name)

greet("Pooja")
greet("Rahul")

print("=============================================")

# ==========================================
# 4. Function with Two Parameters
# ==========================================

def add(a, b):
    print("Addition =", a + b)

add(10, 20)
add(50, 40)

print("=============================================")

# ==========================================
# 5. Function with Return Value
# ==========================================

def square(num):
    return num * num

result = square(6)

print("Square =", result)

print("=============================================")

# ==========================================
# 6. Function to Find Maximum Number
# ==========================================

def maximum(a, b):

    if a > b:
        return a
    else:
        return b

print("Maximum Number =", maximum(25, 18))

print("=============================================")

# ==========================================
# 7. Function with Default Parameter
# ==========================================

def country(name="India"):
    print("Country :", name)

country()
country("Canada")

print("=============================================")

# ==========================================
# 8. Function to Check Even or Odd
# ==========================================

def check(num):

    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

check(20)
check(15)

print("=============================================")

# ==========================================
# 9. Function to Calculate Area of Rectangle
# ==========================================

def rectangle(length, width):
    area = length * width
    return area

print("Area =", rectangle(10, 5))

print("=============================================")

# ==========================================
# 10. Function to Calculate Simple Interest
# ==========================================

def simple_interest(principal, rate, time):

    si = (principal * rate * time) / 100
    return si

print("Simple Interest =", simple_interest(10000, 5, 2))

print("=============================================")

print("Functions Completed Successfully.")